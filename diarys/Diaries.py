from OOP.diarys.Diary import Diary


class Diaries:

    def __init__(self):
        self.diaries = []

    def get_diaries(self):
        return len(self.diaries)

    def add_to_diary(self, username, password):
        my_diary = Diary(username, password)
        self.diaries.append(my_diary)

    def find_diary(self, username):
        for my_diary in self.diaries:
            if my_diary.username == username:
                return my_diary
        return None

    def delete_diary(self, username, password):
        self.diaries = [my_diary for my_diary in self.diaries if
                        not (my_diary.username == username and my_diary.password == password)]
