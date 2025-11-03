# command_line_logging_script.py
"""A script to demonstarte the logging module"""
import logging
import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser()

parser.add_argument('--log_level_console', '-c', nargs='?', default='DEBUG')
parser.add_argument('--log_level_file', '-f', nargs='?', default='DEBUG')

args = parser.parse_args()

file_level = args.log_level_file.upper()
stream_level = args.log_level_console.upper()

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

custom_file_handler = logging.FileHandler('custom_loging.log')
custom_file_handler.setLevel(file_level)

custom_stream_handler = logging.StreamHandler()
custom_stream_handler.setLevel(stream_level)

custom_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
custom_file_handler.setFormatter(custom_file_formatter)

custom_stream_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
custom_stream_handler.setFormatter(custom_stream_formatter)

logger.addHandler(custom_file_handler)
logger.addHandler(custom_stream_handler)

logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message")