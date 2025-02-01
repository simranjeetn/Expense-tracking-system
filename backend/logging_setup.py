import logging

def log_setup(name , file='server.log' , level = logging.DEBUG):

    logger = logging.getLogger(name)

    # Create handlers
    logger.setLevel(level)  # set the logger level to DEBUG
    filehandler = logging.FileHandler(file)  # create a file handler
    formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler.setFormatter(formater)  # set the formatter for the file handler
    logger.addHandler(filehandler)  # add the file handler to the logger

    return logger