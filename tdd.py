import unittest

class Patient:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name.strip()
        self.surname = surname.strip()
        self.age = abs(age)

    def get_name(self) -> str:
       return self.name
    
    def get_surname(self) -> str:
       return self.surname
    
    def get_age(self) -> int:
       return self.age
    
    def set_name(self, name: str):
       self.name = name

    def set_surname(self, surname: str):
       self.surname = surname

    def set_age(self, age: int):
       self.age = age

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
