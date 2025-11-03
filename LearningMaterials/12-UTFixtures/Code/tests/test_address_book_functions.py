import pytest # type: ignore
from src.address_book_functions import add_contact, delete_contact, get_contact_email

def test_add_contact(sample_address_book):
    add_contact(sample_address_book, 'John', 'john@example.com')
    assert sample_address_book['John'] == 'john@example.com'


def test_delete_contact(sample_address_book):
    delete_contact(sample_address_book, 'Bob')
    assert 'Bob' not in sample_address_book


def test_get_contact_email(sample_address_book):
    assert get_contact_email(sample_address_book, 'Alice') == 'alice@example.com'