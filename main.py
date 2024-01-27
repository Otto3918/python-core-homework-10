from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def name(self, value):
        self.value = str(value)


class Phone(Field):
    def __init__(self, value):
        self.value = value
        if not value.isdigit():
            raise ValueError(f'В номере "{value}" недопустимый символ')
        if len(value) != 10:
            raise ValueError(f'В номере "{value}" должно быть 10-ть цифр')
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phone = Phone(phone)
        self.phones.append(self.phone)

    def remove_phone(self, phone):
        self.phone = Phone(phone)
        for p in self.phones:
            if p.value == self.phone.value:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        self.old_phone = Phone(old_phone)
        self.new_phone = Phone(new_phone)
        for p in self.phones:
            if p.value == self.old_phone.value:
                p.value = self.new_phone.value
                return True 
        raise ValueError       

    def find_phone(self, phone):
        self.phone = Phone(phone)
        for p in self.phones:
            if p.value == self.phone.value:
                return p
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, user):
        self.user = user
        return self.data.setdefault(self.user)
    
    def delete(self, user):
        self.user = user
        self.data.pop(self.user, None)
    
    
try:
    # Створення нової адресної книги
    book = AddressBook()
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # Додавання запису John до адресної книги
    book.add_record(john_record)
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    
    ivan_record = Record("Ivan")
    ivan_record.add_phone("0000000001")
    ivan_record.add_phone("0000000002")
    ivan_record.add_phone("0000000003")
    book.add_record(ivan_record)
    ivan = book.find("Ivan")
    r = ivan.find_phone("0000000002")
    print(r)
    ivan.remove_phone("0000000002")
    
    
    # Виведення всіх записів у книзі
    # for name, record in book.data.items():
        # print(record)
    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)     # Виведення: Contact name: John, phones: 1112223333;    5555555555
                    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")      # Виведення: 5555555555
    
    jane = book.find('Jane')
    found_phone = jane.find_phone("9876543210")
    print(f"{jane.name}: {found_phone}")      # Виведення: 9876543210
                                              

    book.delete("Jane")                       # Видалення запису Jane
        
except ValueError:
     pass    
