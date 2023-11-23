import logging
import utils

logging.basicConfig(filename='4_logging.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('DEBUG level message')
logging.info('INFO level message')
logging.warning('WARNING level message')
logging.error('ERROR level message')
logging.critical('CRITICAL level message')

utils.f()
