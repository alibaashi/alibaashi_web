# contact_book.py

contacts = []  # Global list to store contacts

def add_contact(name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})

def find_contact(name):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None

def update_contact(name, phone=None, email=None):
    for contact in contacts:
        if contact['name'] == name:
            if phone:
                contact['phone'] = phone
            if email:
                contact['email'] = email
            return True
    return False

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]

