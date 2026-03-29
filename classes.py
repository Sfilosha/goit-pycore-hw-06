from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        self.phones = list(filter(lambda phone: phone.value != number, self.phones))
    
    def edit_phone(self, old_number: str, new_number: str):
        old_phone_number = self.find_phone(old_number)
        if not old_phone_number:
            print(f"Phone number {old_number} not found.")
            return
        new_phone_number = Phone(new_number)
        old_phone_number.value = new_phone_number.value
    
    def find_phone(self, number: str):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

# TESTING 
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john) 
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")
book.delete("Jane")
