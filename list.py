import unittest


class Leaf:
    def __init__(self):
        pass

    def get_length(self, counter):
        return counter
    
    def push(self, data):
        return Node(data)
    
    def get_data(self):
        return None
    
    def get_next(self):
        return self

    def search_and_remove(self, data):
        return self

class Node:
    def __init__(self, data):
        self._data = data
        self._next = Leaf()

    def get_length(self, counter):
        return self._next.get_length(counter+1)

    def get_next(self):
        return self._next
    
    def set_next(self, node):
        self._next = node

    def get_data(self):
        return self._data

    def push(self, data):
        self.set_next(self._next.push(data))
        return self

    def search_and_remove(self, data):

        if self._data == data:
            return self._next
        self._next = self._next.search_and_remove(data)
        return self
    

class List:
    def __init__(self):
        self._first = Leaf()
    
    def push(self, data):
        self._first = self._first.push(data)
    
    def unshift(self, data):
        new_first = Node(data)
        new_first.set_next(self._first)
        self._first = new_first
    
    def shift(self):
        result = self._first.get_data()
        self._first = self._first.get_next()
        return result
    
    def get_length(self):
        return self._first.get_length(0)

    def search_and_remove(self, data):
        self._first = self._first.search_and_remove(data)





class TestList(unittest.TestCase):

    def test_empty_list_has_length_zero(self):
        l = List()
        self.assertEqual(l.get_length(), 0)

    def test_push_increases_length_and_order(self):
        l = List()
        l.push(1)
        l.push(2)
        l.push(3)
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.shift(), 1)
        self.assertEqual(l.shift(), 2)
        self.assertEqual(l.shift(), 3)
        self.assertIsNone(l.shift())

    def test_unshift_inserts_at_front(self):
        l = List()
        l.push(2)
        l.push(3)
        l.unshift(1)     # Liste soll nun: 1,2,3 sein
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.shift(), 1)
        self.assertEqual(l.shift(), 2)
        self.assertEqual(l.shift(), 3)

    def test_shift_from_empty_returns_none(self):
        l = List()
        self.assertIsNone(l.shift())
        self.assertEqual(l.get_length(), 0)

    def test_mixed_operations(self):
        l = List()
        l.push(2)        # [2]
        l.unshift(1)     # [1,2]
        l.push(3)        # [1,2,3]
        self.assertEqual(l.get_length(), 3)

        self.assertEqual(l.shift(), 1)  # [2,3]
        self.assertEqual(l.get_length(), 2)
        l.unshift(0)                    # [0,2,3]
        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.shift(), 0)
        self.assertEqual(l.shift(), 2)
        self.assertEqual(l.shift(), 3)
        self.assertIsNone(l.shift())
        self.assertEqual(l.get_length(), 0)          

class Dummy:
    def __init__(self, x):
        self.x = x

class TestListWithObjects(unittest.TestCase):

    def test_objects_in_list(self):
        l = List()
        a = Dummy(10)
        b = Dummy(20)
        c = Dummy(30)

        l.push(a)
        l.push(b)
        l.unshift(c)   # Reihenfolge: c, a, b

        self.assertEqual(l.get_length(), 3)
        self.assertEqual(l.shift().x, 30)
        self.assertEqual(l.shift().x, 10)
        self.assertEqual(l.shift().x, 20)
        self.assertIsNone(l.shift())


class TestListRemove(unittest.TestCase):
    def test_search_and_remove(self):
        l = List()
        a = Dummy(10)
        b = Dummy(20)
        c = Dummy(30)

        l.push(a)
        l.push(b)
        l.search_and_remove(a)
        self.assertEqual(l.get_length(), 1)


if __name__ == "__main__":
    unittest.main()
