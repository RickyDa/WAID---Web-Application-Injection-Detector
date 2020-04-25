import joblib as jlb
from waf import log
from tensorflow.keras.models import load_model
from pathlib import Path
from tensorflow.keras.preprocessing import sequence
import numpy as np

base_path = Path(__file__).parent
models_path = str(base_path / "./models/")


class Classifier:

    def __init__(self):
        # load Tokenizers & vectorizer
        self.vectorizer = jlb.load(models_path + '/vectorizer.joblib')
        self.vectorizer2 = jlb.load(models_path + '/vectorizer2.joblib')
        self.tokenizer = jlb.load(models_path + '/LSTM - waid-tokenizer.pickle')

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
        self.lstm = load_model(models_path + '/LSTM - waid-model.h5')
        self.lstm.load_weights(models_path + '/LSTM - waid-weights.h5')

    def predict(self, payload):
        # TODO: make this block parallel
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

            # print(results)
            # counts = np.bincount(results)
            # print(counts, np.argmax(counts))
    
            if np.argmax(np.bincount(results)) == 1:
                log.info("{Classifier predict True")
                return True
        log.info("{Classifier predict False")
        return False

    def predict_rnn(self, val):
        max_log_length = 1024
        seq = self.tokenizer.texts_to_sequences([val])
        log_entry_processed = sequence.pad_sequences(seq, maxlen=max_log_length)
        return self.lstm.predict(log_entry_processed).astype('uint8')
