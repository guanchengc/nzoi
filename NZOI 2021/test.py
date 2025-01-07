import logging

logging.basicConfig(level=logging.DEBUG)

def add(a, b):
    logging.debug("add")
    return a + b