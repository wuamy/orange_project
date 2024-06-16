import logging

class LogGen:
  @staticmethod
  def logger():
    logger = logging.getLogger()
    fileHandler = logging.FileHandler('.\\logs\\automation.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    return logger
