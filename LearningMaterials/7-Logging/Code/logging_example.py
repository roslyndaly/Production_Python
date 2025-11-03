"""A script to demonstarte the logging module"""
import logging

logging.basicConfig(filename='log_example', level="ERROR")


logging.debug("This is a debug message") # Detailed information, typically useful for debugging purposes
logging.info("This is a info message") # General information about the progress or state of the program
logging.warning("This is a warning message") # Indication of a potential problem or a non-fatal issue that deserves attention
logging.error("This is a error message") # A more severe problem that prevents the program from executing a particular function or task
logging.critical("This is a critical message") # A critical error that may cause the program to terminate or result in system instability
