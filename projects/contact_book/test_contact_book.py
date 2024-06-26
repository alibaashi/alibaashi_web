# test_contact_book.py

from contact_book import add_contact, find_contact, update_contact, delete_contact, contacts

def setup_function():
    """ This function runs before each test case to ensure a clean state. """
    global contacts
    contacts.clear()

def test_add_contact():
    add_contact('Alice', '12345', 'alice@example.com')
    assert len(contacts) == 1
    assert contacts[0]['name'] == 'Alice'
    assert contacts[0]['phone'] == '12345'
    assert contacts[0]['email'] == 'alice@example.com'

def test_find_contact():
    add_contact('Bob', '67890', 'bob@example.com')
    contact = find_contact('Bob')
    assert contact is not None
    assert contact['name'] == 'Bob'
    assert contact['phone'] == '67890'
    assert contact['email'] == 'bob@example.com'

def test_update_contact():
    add_contact('Charlie', '11111', 'charlie@example.com')
    update_contact('Charlie', '22222', 'charlie_new@example.com')
    contact = find_contact('Charlie')
    assert contact['phone'] == '22222'
    assert contact['email'] == 'charlie_new@example.com'

def test_delete_contact():
    add_contact('David', '33333', 'david@example.com')
    delete_contact('David')
    contact = find_contact('David')
    assert contact is None
