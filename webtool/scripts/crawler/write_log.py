import logging

def log_writer(message):
    logging.basicConfig(
        filename="./out.log",
        encoding='utf-8',
        level=logging.INFO,
        format='[%(asctime)s] : %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p'
    )
    logging.info(message)
