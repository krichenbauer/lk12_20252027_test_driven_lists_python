class Patient:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self._next = None

    def set_next(self, p):
        self._next = p

    def get_next(self):
        return self._next

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age



class WaitingRoom:
    def __init__(self, size=10):
        # Initialize an array with fixed size and empty slots
        self._patients = []
        self.size = size
        self.first = None
        self.last = None
        self._count = 0

    def add(self, p: Patient):
        if self.first is None:
            self.first = p
            self.last = p
            self._count += 1


        else:
            if self._count + 1 > self.size:
                    raise (OverflowError)
            self.last.set_next(p)
            self.last = p
            self._count += 1


    def remove(self) -> Patient:
        if self.first is None:
            return None
        else:
            tempP = self.first
            self.first = self.first.get_next()
            self._count -= 1
            return tempP



    def get_count(self) -> int:
        """Return the number of patients currently waiting."""
        return self._count


import unittest
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

    def test_add_remove_1(self):
        room = WaitingRoom(size=5)

        p1 = Patient("A", "One", 40)
        p2 = Patient("B", "Two", 41)
        p3 = Patient("C", "Three", 42)

        room.add(p1)
        self.assertEqual(room.get_count(), 1)
        room.add(p2)
        self.assertEqual(room.get_count(), 2)

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


if __name__ == "__main__":
    unittest.main()



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
