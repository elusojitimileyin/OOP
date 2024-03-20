from unittest import TestCase

from OOP.diarys import Diary


class TestDiary(TestCase):

    def test_diary_isLocked(self):
        new_diary = Diary("userName", "password"))
        self.assertTrue(self, new_diary.lockDiary())

    def test_diary_isLocked_unlock(self):
        new_diary = Diary("userName", "password")
        self.assertTrue(self, new_diary.lockDiary())
        new_diary.unlockDiary("password")
        self.assertTrue(self,new_diary.unlockDiary("password"))

    def test_diary_isLocked_unlock_add_to_diary(self):
        new_diary = Diary("userName", "password")
        self.assertTrue(self, new_diary.lockDiary())
        new_diary.unlockDiary("password")
        self.assertTrue(self,new_diary.unlockDiary("password"))
        new_diary.addDiary()
