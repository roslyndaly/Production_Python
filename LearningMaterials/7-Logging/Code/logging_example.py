"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_file_handler = logging.FileHandler('custom_logging.log')
custom_file_handler.setLevel(logging.INFO)
custom_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
custom_file_handler.setFormatter(custom_file_formatter)
logger.addHandler(custom_file_handler)


custom_stream_handler = logging.StreamHandler()
custom_stream_handler.setLevel(logging.WARNING)
custom_stream_formatter = logging.Formatter('line %(lineno)d. - %(levelname)s - %(message)s')
custom_stream_handler.setFormatter(custom_stream_formatter)
logger.addHandler(custom_stream_handler)

logger.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logger.info("This is a info message") # General information about the progress or state of the program
logger.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logger.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logger.critical("This is a critical message") # A critical error that may cause the program to terminate or result in system instability
