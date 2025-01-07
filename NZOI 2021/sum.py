import logging

logging.basicConfig(level=logging.DEBUG)

def sumAdd(a,b):
    logging.debug(f'sum: {a}+{b}')
    return a+b