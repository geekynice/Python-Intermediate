import logging

#initializing a logger 
logger = logging.getLogger(__name__)

#setting the handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#setting the level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#formatting our logs
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

#setting the format to both
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#adding handlers
logger.addHandler(stream_h)
logger.addHandler(file_h)

#displaying warning
logger.warning("This is a warning message.")
logger.error("This is a error message.")

'''
result:
__main__ - WARNING - This is a warning message.
__main__ - ERROR - This is a error message.
'''