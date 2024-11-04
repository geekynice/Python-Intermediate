import logging
#initializing a logger 

logger = logging.getLogger(__name__)

#Types of logging message:
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is a error message")
logger.critical("This is a critical message")