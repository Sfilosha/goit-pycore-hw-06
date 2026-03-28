from collections import UserDict
from dataclasses import dataclass, field

@dataclass
class Field:
    value: any

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value: str):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)

@dataclass
class Record:
    name: Name
    phones: list[Phone] = field(default_factory=list)

    def add_phone(self, number: str):
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        self.phones = list(filter(lambda p: p != number, self.phones))
    
    def edit_phone(self, old_number: str, new_number: str):
        phone = self.find_phone(old_number)
        if phone:
            phone = new_number
        else:
            print(f"Phone number {old_number} not found.")
            return
    
    def find_phone(self, number: str):
        phone = next(filter(lambda p: p == number, self.phones), None)
        if phone:
            return phone
        else: 
            print(f"Phone number not found.")
            return


    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


@dataclass
class AddressBook(UserDict):
    data: dict[str, str] = field(default_factory=dict)

    def add_record(self, record: Record):
        self.data[record.name] = record

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
