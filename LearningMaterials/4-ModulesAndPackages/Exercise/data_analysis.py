"""
python script to clean integer lists by removing duplicates.
"""

from data_processing.cleaning import remove_duplicates
from data_processing.transforming import capitalise_strings

big_list = [
    1,
    5,
    6,
    3,
    6,
    1,
    2,
    5,
    8,
    9,
    0,
    7,
    3,
    2,
    5,
    6,
    3,
    6,
    3,
    5,
    6,
    1,
    2,
    3,
    4,
    5,
    78,
    64,
    34,
    32,
    32,
]

print(remove_duplicates(big_list))


string_list = ["my", "name", "is", "roslyn", "daly"]

print(capitalise_strings(string_list))
