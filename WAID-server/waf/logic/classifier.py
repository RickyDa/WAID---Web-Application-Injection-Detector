import os
import warnings
import joblib as jlb
from waf import log
from pathlib import Path
import numpy as np
import waf.logic.rule_service as rs
from waf.database.models import Rule
from waf.database.enums import RuleType
from waf.database.enums import Action

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence


base_path = Path(__file__).parent
models_path = str(base_path / "./models/")


class Classifier:

    def __init__(self):
        # load Tokenizers & vectorizer
        self.vectorizer = jlb.load(models_path + '/vectorizer.joblib')
        self.vectorizer2 = jlb.load(models_path + '/vectorizer2.joblib')
        self.tokenizer = jlb.load(models_path + '/waid-tokenizer.pickle')

        # 1 - 2 load logistic regression
        self.logreg = jlb.load(models_path + '/logreg.joblib')
        self.logreg2 = jlb.load(models_path + '/logreg2.joblib')

        # 3 - 4 load SVMs
        self.svm = jlb.load(models_path + '/modvsvm.joblib')
        self.svm2 = jlb.load(models_path + '/modvsvm2.joblib')

        # 5 - 6 load  Random forest
        self.rf = jlb.load(models_path + '/random-forest.joblib')
        self.rf2 = jlb.load(models_path + '/random-forest2.joblib')

        # 7 - load RNN LSTM model
        self.lstm = load_model(models_path + '/waid-model.h5')
        self.lstm.load_weights(models_path + '/waid-weights.h5')

    def predict(self, payload):
        _input = np.array([])

        for _, val in payload.inspected_value.items():
            _input = np.append(_input, val)

        for val in _input:
            results = np.array([], dtype='uint8')
            v1 = self.vectorizer.transform([val])
            v2 = self.vectorizer2.transform([val])
            results = np.append(results, self.logreg.predict(v1))
            results = np.append(results, self.svm.predict(v1))
            results = np.append(results, self.rf.predict(v1))
            results = np.append(results, self.logreg2.predict(v2))
            results = np.append(results, self.svm2.predict(v2))
            results = np.append(results, self.rf2.predict(v2))
            results = np.append(results, self.predict_rnn(val))

            if np.argmax(np.bincount(results)) == 1:
                log.info(f"Classifier predict True {val} - {results}")
                rs.create(Rule(rule=payload.srcIP, type=RuleType.BLOCKED_HOST.value, action=Action.BLOCK.value))
                return True
            log.info(f"Classifier predict False for {val} - {results}")
        return False

    def predict_rnn(self, val):
        max_log_length = 1024
        seq = self.tokenizer.texts_to_sequences([val])
        log_entry_processed = sequence.pad_sequences(seq, maxlen=max_log_length)
        return self.lstm.predict(log_entry_processed).astype('uint8')
