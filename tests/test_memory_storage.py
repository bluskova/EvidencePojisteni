from unittest import TestCase

from src.dataStorage.memory_storage import MemoryStorage
from src.person import Person


class TestMemoryStorage(TestCase):
    def test_number_of_records(self):
        registry = MemoryStorage()
        person = Person('Jan', 'Novak', 10, 123456789)
        registry.add_person(person)
        assert(registry.number_of_records() == 1)

    def test_add_person(self):
        self.fail()

    def test_remove_person(self):
        self.fail()

    def test_count_person_registered(self):
        self.fail()

    def test_get_persons(self):
        self.fail()

    def test_get_all_persons(self):
        self.fail()
