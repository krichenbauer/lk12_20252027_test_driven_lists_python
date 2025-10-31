import unittest

from patient import Patient, TestPatient


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
    
    def set_next(self, nextNode:"Node"):
        self._next = nextNode

    def get_next(self):
        return self._next
    
    def get_data(self):
        return self._data

    def get_count(self, cur):
        if self._next == None:
            ''' Noone behind, so return current counter + me'''
            return cur+1
        else:
            ''' At least one more, so tell him/her to count on'''
            return self._next.get_count(cur+1)
    
    def add(self, data):
        if self._next == None:
            self._next = Node(data)
        else:
            self._next.add(data)
    

    

class WaitingRoom:
    def __init__(self, size = 10):
        self._first = None
        self._size = size

    def add(self, data):
        """Add a patient to the waiting queue."""
        if self.get_count() == self._size:
            raise OverflowError("Waiting queue is full.")
              
        if self._first == None:
            self._first = Node(data)
        else:
            self._first.add(data)
    
    def push(self, data):
        new_node = Node(data)
        new_node.set_next(self._first)
        self._first = new_node



    def remove(self) -> Patient:
        """Remove the first patient (FIFO) and shift remaining patients forward."""
        if self.get_count() == 0:
            return None
        else:
            old_first_node = self._first
            self._first = old_first_node.get_next()
            return old_first_node.get_data()
    
    def get_count(self) -> int:
        if self._first == None:
            return 0
        else:
            return self._first.get_count(0)
        

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
    
    def test_add_and_remove_four_patients_lifo(self):
        
        room = WaitingRoom()
        
        p7 = Patient("Helena", "Doe", 31)
        p17 = Patient("John", "Doe", 30)
        p34 = Patient("Maria", "Moser", 76)
        p2195 = Patient("Max", "Mustermann", 19)
        
        self.assertEqual(room.get_count(), 0)

        room.push(p2195)
        room.push(p34)
        room.push(p17)
        room.push(p7)

        self.assertEqual(room.get_count(), 4)

        removed = room.remove()
        self.assertEqual(removed, p7)
        self.assertEqual(room.get_count(), 3)

        removed = room.remove()
        self.assertEqual(removed, p17)
        self.assertEqual(room.get_count(), 2)

        removed = room.remove()
        self.assertEqual(removed, p34)
        self.assertEqual(room.get_count(), 1)

        removed = room.remove()
        self.assertEqual(removed, p2195)
        self.assertEqual(room.get_count(), 0)
        self.assertIsNone(room.remove())


def test_add_and_remove_four_patients_mixed_order(self):
        
        room = WaitingRoom()
        
        p7 = Patient("Helena", "Doe", 31)
        p17 = Patient("John", "Doe", 30)
        p34 = Patient("Maria", "Moser", 76)
        p2195 = Patient("Max", "Mustermann", 19)
        
        self.assertEqual(room.get_count(), 0)

        room.add(p2195)
        room.add(p34)
        room.push(p17)
        room.push(p7)

        self.assertEqual(room.get_count(), 4)

        removed = room.remove()
        self.assertEqual(removed, p7)
        self.assertEqual(room.get_count(), 3)

        removed = room.remove()
        self.assertEqual(removed, p17)
        self.assertEqual(room.get_count(), 2)

        removed = room.remove()
        self.assertEqual(removed, p2195)
        self.assertEqual(room.get_count(), 1)

        removed = room.remove()
        self.assertEqual(removed, p34)
        self.assertEqual(room.get_count(), 0)
        self.assertIsNone(room.remove())


if __name__ == "__main__":
    unittest.main()
