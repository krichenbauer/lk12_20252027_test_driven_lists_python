class Patient:
    def __init__(self, name:str, surname:str, age:int):
        self._name=name.strip()
        self._surname=surname.strip()
        self._age=int(str(age).lstrip('-0b'))
        self.next:Patient = None
    def set_next(self,p):
        self.next = p

    def get_next(self):
        return self.next

    def get_name(self):
        return self._name
    def get_surname(self):
        return self._surname
    def get_age(self):
        return self._age

class WaitingRoom:

    def __init__(self, size=10):
        self._size=size

        self._first: Patient = None
        self._last: Patient = None
        self._count: int = 0
        self._size: int = size

    def add(self,p:Patient):
        if self._count+1 > self._size:
            raise(OverflowError)
        else:
            if self._last != None:
                self._last.set_next(p)
                self._last = p
                self._count += 1
            else:
                self._last=p
                self._first=p
                self._count += 1

    def remove(self):
        if self._count == 0:
            return None
        else:
            p = self._first
            self._first=p.get_next()
            self._count-=1
            if self._first is None:
                self._last=None
            return p

    def get_count(self):
        return self._count







import unittest

class TestPatient(unittest.TestCase):
    def test_get_name_returns_correct_value(self):
       p = Patient("John", "Doe", 30)
       self.assertEqual(p.get_name(), "John")
    def test_get_surname_returns_correct_value(self):
       p = Patient("Jane", "Smith", 25)
       self.assertEqual(p.get_surname(), "Smith")
    def test_get_age_returns_correct_value(self):
       p = Patient("Alice", "Brown", 40)
       self.assertEqual(p.get_age(), 40)
    def test_multiple_patients_independent_values(self):
       p1 = Patient("Tom", "Miller", 20)
       p2 = Patient("Eva", "Schneider", 35)
       self.assertEqual(p1.get_name(), "Tom")
       self.assertEqual(p2.get_name(), "Eva")
       self.assertNotEqual(p1.get_surname(), p2.get_surname())
       self.assertNotEqual(p1.get_age(), p2.get_age())
    def test_trimmer(self):
        p = Patient(" John", "Doe ", 30)
        self.assertEqual(p.get_name(), "John")
        self.assertEqual(p.get_surname(), "Doe")
        self.assertEqual(p.get_age(), 30)
    def test_initialization_with_bad_age(self):
        p = Patient("Bob", "Brown", "-00025")
        self.assertEqual(p._age, 25)  # '-00025' → int(25)

    def test_set_next_links_patients(self):
        p1 = Patient("John", "Doe", 40)
        p2 = Patient("Jane", "Doe", 38)
        p1.set_next(p2)
        self.assertIs(p1.next, p2)

class TestWaitingRoom(unittest.TestCase):

    def test_add_and_remove_single_patient(self):
        room = WaitingRoom()
        p = Patient("John", "Doe", 30)

        self.assertEqual(room.get_count(), 0)

        room.add(p)

        # After adding one patient, count should be 1
        self.assertEqual(room.get_count(), 1)

        # Removing should return the same patient
        removed = room.remove()
        self.assertEqual(removed, p)

        # Now the queue should be empty again
        self.assertEqual(room.get_count(), 0)

        # Removing again should return None
        self.assertIsNone(room.remove())

    def test_two_patients(self):
        room = WaitingRoom()
        patients = [Patient(f"Name{i}", f"Surname{i}", 20+i) for i in range(2)]
        for p in patients:
            room.add(p)
        self.assertEqual(room.get_count(), 2)
        for expected in patients:
            self.assertIs(room.remove(), expected)
        self.assertEqual(room.get_count(), 0)

    def test_five_patients(self):
        room = WaitingRoom()
        patients = [Patient(f"Name{i}", f"Surname{i}", 20+i) for i in range(5)]
        for p in patients:
            room.add(p)
        self.assertEqual(room.get_count(), 5)
        for expected in patients:
            self.assertIs(room.remove(), expected)
        self.assertEqual(room.get_count(), 0)

    def test_eight_patients(self):
        room = WaitingRoom()
        patients = [Patient(f"Name{i}", f"Surname{i}", 20+i) for i in range(8)]
        for p in patients:
            room.add(p)
        self.assertEqual(room.get_count(), 8)
        for expected in patients:
            self.assertIs(room.remove(), expected)
        self.assertEqual(room.get_count(), 0)

    def test_overflow_raises(self):
        room = WaitingRoom(size=3)
        for i in range(3):
            room.add(Patient(f"N{i}", f"S{i}", 30+i))
        self.assertEqual(room.get_count(), 3)
        with self.assertRaises(OverflowError):
            room.add(Patient("Too", "Many", 99))

    def test_alternating_add_remove(self):
        room = WaitingRoom(size=5)

        p1 = Patient("A", "One", 40)
        p2 = Patient("B", "Two", 41)
        p3 = Patient("C", "Three", 42)

        # Add p1, remove -> should be p1
        room.add(p1)
        self.assertIs(room.remove(), p1)
        self.assertEqual(room.get_count(), 0)

        # Add p1, p2; remove -> p1; add p3; remove -> p2; remove -> p3
        room.add(p1)
        room.add(p2)
        self.assertIs(room.remove(), p1)
        room.add(p3)
        self.assertIs(room.remove(), p2)
        self.assertIs(room.remove(), p3)
        self.assertEqual(room.get_count(), 0)
        self.assertIsNone(room.remove())



if __name__ == "__main__":
    unittest.main()
