import unittest

class Patient:
    def __init__(self, name: str, surname: str, age: int, next = None):
        self._name = name.strip()
        self._surname = surname.strip()
        self._age = abs(age)
        self._next = next

    def get_name(self) -> str:
       return self._name
    
    def get_surname(self) -> str:
       return self._surname
    
    def get_age(self) -> int:
       return self._age
    
    def set_name(self, name: str):
       self._name = name

    def set_surname(self, surname: str):
       self._surname = surname

    def set_age(self, age: int):
       self._age = age

    def set_next(self, p):
        self._next = p

    def get_next(self):
        return self._next

class WaitingRoom:
    def __init__(self, size = 10):
        self.first = None
        self.last = None
        self.count = 0
        self.size = size

    def add(self, p: Patient):
        """Add a patient to the waiting queue."""
        if self.get_count() == self.size:
            raise OverflowError("Waiting queue is full.")
              
        if self.first == None:
            self.first = p
            self.last = p
            self.count += 1
        else:
            self.last.set_next(p)
            self.last = p
            self.count += 1

    def remove(self) -> Patient:
        """Remove the first patient (FIFO) and shift remaining patients forward."""
        if self.count == 0:
            return None
        p = self.first
        self.first = p.get_next()
        self.count -= 1
        return p
    
    def get_count(self) -> int:
        return self.count

class TestWaitingRoom(unittest.TestCase):
    def test_add_and_remove_single_patient(self):
        room = WaitingRoom()
        p = Patient("John", "Doe", 30)

        self.assertEqual(room.get_count(), 0)

        room.add(p)

        self.assertEqual(room.get_count(), 1)

        removed = room.remove()
        self.assertEqual(removed, p)

        self.assertEqual(room.get_count(), 0)

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

    def test_add_four_patients(self):
        room = WaitingRoom()
        patients = [Patient("a"*i, "b"*i, i) for i in range(4)]
        
        for p in patients:
            room.add(p)

        self.assertEqual(room.get_count(), 4)

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

    def test_space_in_constructor(self):
       p = Patient(" Stefan", "Müller ", 20)
       self.assertEqual(p.get_name(), "Stefan")
       self.assertEqual(p.get_surname(), "Müller")

    def test_negative_age(self):
       p = Patient("Stefan", "Müller", -20)
       self.assertEqual(p.get_age(), 20)

if __name__ == "__main__":
    unittest.main()
