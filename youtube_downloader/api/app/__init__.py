import os
import logging


def setup_logging(level=logging.DEBUG):
    logging.basicConfig(level=level,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

    return logging.getLogger()





