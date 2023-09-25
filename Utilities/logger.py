import logging
import inspect


class LogGen:

    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler(r"C:\Users\ajayj\PycharmProjects\demo_framework\Logs\logfile.log")
        format = logging.Formatter(" %(asctime)s : %(levelname)s : %(funcName)s : %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
