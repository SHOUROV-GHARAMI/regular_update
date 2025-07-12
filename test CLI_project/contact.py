
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_csv(self):
        return f"{self.name},{self.phone},{self.email},{self.address}\n"

    @staticmethod
    def from_csv(line):
        name, phone, email, address = line.strip().split(',')
        return Contact(name, phone, email, address)


