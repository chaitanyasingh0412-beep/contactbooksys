import json

# Load contacts from file
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")

    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

# Search for a contact
def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    contact = contacts.get(name)

    if contact:
        print(f"Found contact - Name: {name}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"Contact {name} not found.")

# Update a contact
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    contact = contacts.get(name)

    if contact:
        phone = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")

        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email

        contacts[name] = contact
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

# Main function to run the contact book
def contact_book():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book()
