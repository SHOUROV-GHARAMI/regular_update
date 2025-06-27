# storage.py

from contact import Contact

FILENAME = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(FILENAME, 'r') as f:
            for line in f:
                if line.strip():
                    contacts.append(Contact.from_csv(line))
    except FileNotFoundError:
        open(FILENAME, 'w').close()
    return contacts

def update_contact(contacts):
    with open(FILENAME, 'w') as f:
        for contact in contacts:
            f.write(contact.to_csv())

def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
        for contact in contacts:
            f.write(contact.to_csv())