import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')

# 2024-10-21 17:51:58,601 - simpleExample - DEBUG - debug message
# 2024-10-21 17:51:58,601 - simpleExample - INFO - info message