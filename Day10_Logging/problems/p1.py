'''
Problem 1: Basic Logging Configuration
Write a function that configures the logging system with a basic configuration 
that logs messages with level INFO or higher. Log a simple message to demonstrate the setup.

Expected Output:
For example, the output could be:
2024-10-21 18:15:00,000 - INFO - This is an info message.
'''
import logging
def info():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    logger = logging.getLogger(__name__)
    
    return logger.info("This is an info message.")

info()
    