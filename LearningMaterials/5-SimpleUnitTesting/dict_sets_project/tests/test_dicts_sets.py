"""
Test module for dicts and sets functionalities.
"""

from src.dict_sets import (cleanup_address_book, search_address_book, count_vowels, get_names_in_common, get_numbers_in_common, combine_address_books)


import logging

logging.basicConfig(level='ERROR',format='%(levelname)s - %(asctime)s - %(message)s - %(module)s', filename='tutorial.log', filemode = 'w')

def test_cleanup_address_book():
    address_book = {
        "john doe": "1234567890",
        "jane": "0987654",
        "alice smith": "5551234"
    }
    expected = {
        "John Doe": "1234 567890",
        "Jane": "0987654",
        "Alice Smith": "5551234"
    }
    assert cleanup_address_book(address_book) == expected

def test_search_address_book():
    address_book = {
        "John Doe": "1234567890",
        "Jane Smith": "0987654",
        "Alice Johnson": "5551234"
    }
    search_string = "Ja"
    expected = {
        "Jane Smith": "0987654"
    }
    assert search_address_book(address_book, search_string) == expected

def test_count_vowels():

    #inputs a string

    input_string = 'hello world'

    expected_output = {'a':0, 'e':1, 'i':0, 'o':2, 'u':0}

    assert count_vowels(input_string.lower()) == expected_output

def test_get_names_in_common():

    arg1 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Xander Jenkins': '462946195'}

    arg2 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Tom Van Der Sande': '462362722'}

    actual_output = get_names_in_common(arg1,arg2)

    expected_output = {'Roslyn Daly', 'David Cero'}

    assert actual_output == expected_output , f'this is actual {actual_output}, this is expected {expected_output}'

def test_get_numbers_in_common(): 

    arg1 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Xander Jenkins': '462946195'}
    arg2 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Tom Van Der Sande': '462362722'}

    actual_output = get_numbers_in_common(arg1,arg2)

    expected_output = {'9876543', '6482927018'}

    assert actual_output == expected_output

def test_combine_address_books():

    arg1 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Xander Jenkins': '462946195'}
    arg2 = {'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Tom Van Der Sande': '462362722'}


    actual_output = combine_address_books(arg1,arg2)

    expected_output = ({'Roslyn Daly': '9876543', 'David Cordero': '6482927018', 'Xander Jenkins': '462946195', 'Tom Van Der Sande': '462362722'}, {'Roslyn Daly': '9876543', 'David Cordero': '6482927018'})

    assert actual_output == expected_output

