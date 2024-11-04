'''
Problem 2: Logging to a File
Write a function that sets up a logger to write log messages to a file called app.log. 
Log at least two messages: one with the level WARNING and another with the level ERROR.

Expected Output:
When you open app.log, it should contain:
WARNING - This is a warning message.
ERROR - This is an error message.
'''
import logging

def logs():
    logging.basicConfig(level=logging.DEBUG)
    file_h = logging.FileHandler('logs/app.log')
    logger = logging.getLogger(__name__)
    logger.addHandler(file_h)
    logger.warning('This is a warning message.')
    logger.error('This is a error message.')

logs()