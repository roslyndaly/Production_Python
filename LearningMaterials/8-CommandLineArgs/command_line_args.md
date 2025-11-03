# Command Line Arguments

When running a Python file as a script we have been running the following syntax:

> python my_script.py

This command executes the Python file named `my_script.py`. However, what we can do is provide arguments, known as **command line arguments**, when executing the file, which allows users to customise the file at runtime without modifying the code itself.

Three common libraries for doing this are:

- `sys`: you get bare-bones access to the command-line text through `sys.argv`. [Here's a nice article on using this as your base.](https://realpython.com/python-command-line-arguments/)
- `argparse`: this is the 'Python Standard library' offering, and what we'll use here.   [docs](https://docs.python.org/3/library/argparse.html)
- `click`: This is a newer library which may, in time, become the new standard. [docs](https://click.palletsprojects.com/en/8.1.x/why/)

We will use `argparse` due to its versatility and ease of use.

## Using `argparse` for Command-Line Arguments

```Python
"""A script to demonstrate the argparse"""
import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument('--name', '-n', 
                    nargs = '?', 
                    default= 'NoName', 
                    help='Name of user')
parser.add_argument('--age', '-a', 
                    default = 'NoAge', 
                    help='Age of user')

# Parse arguments
args = parser.parse_args()

# Access argument values
user_name = args.name
user_age = args.age

print(f'{user_name} is {user_age} years old')
```

In this example:

- We import the `argparse` module.
- `ArgumentParser` is a class provided by the `argparse` module that helps in defining what arguments the script should accept from the command line. Here, we create an instance of `ArgumentParser` named parser.
- We use the `add_argument()` method of the `ArgumentParser` object (`parser`) to specify what arguments our script should accept. In this script:
  - `--name` and `-n` are the argument names. `--name` is the long form of the argument, while `-n` is the short form.
  - `nargs='?'` specifies that the argument can have 0 or 1 values. If no value is provided, the default value will be used.
  - `default='NoName'` specifies the default value for the argument if no value is provided.
  - `help='Name of user'` provides a brief description of what the argument is for.

  - Similarly, we define another argument `--age` with the same configuration, but there are many different parameters you could include when [adding arguments](https://docs.python.org/3/library/argparse.html#quick-links-for-add-argument).
- We parse the command line arguments using `parse_args()` method, which returns an object `args` which contains the argument values as attributes.
- We access the values of the arguments using the attributes of the args object.

You can run this script from the command line like this:

> python my_script.py --name Monica --age 27

This will print:
> Monica is 27 years old

## Concept Check: Combine Command Line Arguments with Logging

Amend the script below to allow the log levels for the FileHandler and the StreamHandler to be passed as arguments from the command line, rather than it always being `INFO` and `ERROR` respectuvely. (The default for both should be `DEBUG`). I.e from the command line, you could run:

> python command_line_logging_script.py --fh_level DEBUG --st_level INFO

```Python
# command_line_logging_script.py
"""A script to demonstarte the logging module"""
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")

custom_file_handler = logging.FileHandler('custom_loging.log')
custom_file_handler.setLevel("INFO")

custom_stream_handler = logging.StreamHandler()
custom_stream_handler.setLevel("ERROR")

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
```
