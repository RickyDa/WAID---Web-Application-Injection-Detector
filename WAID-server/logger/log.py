import logging
from pathlib import Path


class Log:
    def __init__(self):
        self.__logger = self.set_logger()

    @staticmethod
    def set_logger():
        # Create a custom logger
        logger = logging.getLogger(__name__)

        # Set General level of logger
        logger.setLevel(logging.DEBUG)

        # Create handlers
        dir_path = Path(__file__).parent / "logs"
        try:
            if not Path.is_dir(dir_path):
                Path.mkdir(dir_path)
        except (IOError, SystemError) as e:
            logger.error("Couldn't create logger folder", exc_info=True)

        debug_handler = logging.FileHandler(str((dir_path / "debug.log").resolve()))
        debug_handler.setLevel(logging.DEBUG)
        warning_handler = logging.FileHandler(str((dir_path / "warning.log").resolve()))
        warning_handler.setLevel(logging.WARNING)

        # Create formatters and add it to handlers
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        debug_handler.setFormatter(log_format)
        warning_handler.setFormatter(log_format)

        # Add handlers to the logger
        logger.addHandler(debug_handler)
        logger.addHandler(warning_handler)
        return logger

    def get_logger(self):
        return self.__logger


log = Log().get_logger()
