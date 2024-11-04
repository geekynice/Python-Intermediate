import logging

#setting a basic configuration for our logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

import helper_for_logger

'''
result:
10/21/2024 17:41:01 - helper_for_logger - DEBUG - This is a debug message
10/21/2024 17:41:01 - helper_for_logger - INFO - This is a info message
10/21/2024 17:41:01 - helper_for_logger - WARNING - This is a warning message
10/21/2024 17:41:01 - helper_for_logger - ERROR - This is a error message
10/21/2024 17:41:01 - helper_for_logger - CRITICAL - This is a critical message
'''