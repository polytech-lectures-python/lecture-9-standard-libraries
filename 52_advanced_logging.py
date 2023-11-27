import logging

# create logger
logger = logging.getLogger('advanced_logging')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create file handler and set level to info
fh = logging.FileHandler('4_logging.log')
fh.setLevel(logging.INFO)

# create formatters
formatter1 = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatters
ch.setFormatter(formatter1)
fh.setFormatter(formatter2)

# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

# application code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
