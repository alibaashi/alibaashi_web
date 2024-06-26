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

def main():
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            add_contact(name, phone, email)
            print("Contact added successfully!")
        
        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact = find_contact(name)
            if contact:
                print("Contact found:")
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
        
        elif choice == '3':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (press enter to skip): ")
            email = input("Enter new email (press enter to skip): ")
            if update_contact(name, phone, email):
                print("Contact updated successfully!")
            else:
                print("Contact not found.")
        
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
            print("Contact deleted successfully!")
        
        elif choice == '5':
            print("Exiting Contact Book Application.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
