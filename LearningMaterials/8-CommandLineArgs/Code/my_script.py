"""A script to demonstarte the argparse"""
import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument('--name', '-n', 
                    nargs = '?', 
                    #default= 'NoName', 
                    help='Name of user')
parser.add_argument('--age', '-a', 
                    #default = 'NoAge', 
                    help='Age of user')

# Parse arguments
args = parser.parse_args()

# Access argument values
user_name = args.name
user_age = args.age

print(f'{user_name} is {user_age} years old')