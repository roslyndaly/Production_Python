def add_contact(address_book, name, email):
    address_book[name] = email

def delete_contact(address_book, name):
    if name in address_book:
        del address_book[name]

def get_contact_email(address_book, name):
    return address_book.get(name, None)
