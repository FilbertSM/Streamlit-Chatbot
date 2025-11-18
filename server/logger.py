import logging

def setup_logger(name="gaia"):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s ")
    ch.setFormatter(formatter)

    # Duplicate Log Handler
    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger

logger = setup_logger()