from OOP.diarys.Entry import Entry
from OOP.exceptions.invalid_pin_exception import InvalidPinException


class Diary:
    def __init__(self, username, password):
        if not username:
            raise ValueError("Username cannot be empty.")
        if not password:
            raise ValueError("Password cannot be empty")
        self.username = username
        self.password = password
        self.is_Locked = True
        self.entries = []

    def is_Locked(self):
        return self.is_Locked

    def lock_diary(self, password):
        if self.get_password() != self.password:
            self.is_Locked = True

    def get_number_of_entries(self):
        return len(self.entries)

    def unlock_diary(self, password):
        if self.get_password() == password:
            self.is_Locked = False
        else:
            raise InvalidPinException("Wrong Password. Kindly Enter Your Password Again")

    def get_password(self):
        return self.password

    def create_entry(self, Id, title, body):
        if self.is_Locked:
            raise ValueError("Diary is already locked")
        new_entry = Entry(Id, title, body)
        self.entries.append(new_entry)
        return new_entry

    def delete_entry(self, Id):
        if self.is_Locked:
            raise ValueError("Diary is already locked. cannot delete entry")
        for entry in self.entries:
            if entry.Id == Id:
                self.entries.remove(entry)
                return True
        raise ValueError(f"No entry with Id {Id} found")

    def find_entry(self, Id):
        if self.is_Locked:
            raise ValueError("Diary is already locked. cannot find entry")
        for entry in self.entries:
            if entry.Id == id:
                return entry
        raise ValueError(f"No entry with Id {Id} found")

    def update_entry(self, Id, title, body):
        if self.is_Locked:
            raise ValueError("Diary is already locked. cannot update entry")
        for entry in self.entries:
            if entry.Id == Id:
                entry.title = title
                entry.body = body
                return True
        raise ValueError(f"No entry with Id {Id} found")
