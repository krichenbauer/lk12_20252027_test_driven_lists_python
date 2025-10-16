
class Patient:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class WaitingRoom:
    def __init__(self, size=10):
        # Initialize an array with fixed size and empty slots
        self._patients = [None] * size
        self._size = size
        self._count = 0

    def add(self, p: Patient):
        """Add a patient to the waiting queue."""
        if self._count == self._size:
            raise OverflowError("Waiting queue is full.")
        self._patients[self._count] = p
        self._count += 1

    def remove(self) -> Patient:
        """Remove the first patient (FIFO) and shift remaining patients forward."""
        if self._count == 0:
            return None
        patient = self._patients[0]
        # Shift all patients one position forward
        for i in range(1, self._count):
            self._patients[i - 1] = self._patients[i]
        self._patients[self._count - 1] = None
        self._count -= 1
        return patient

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


if __name__ == "__main__":
    unittest.main()
