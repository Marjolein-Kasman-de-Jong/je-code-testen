import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Tests for the class Employee """
    
    def setUp(self):
        """ Create an instance of Employee for use in all test methods """
        self.employee1 = Employee('Marjolein', 'Kasman', 20000)
    
    def test_give_default_raise(self):
        """ Test that a default raise is given to employee1 if no custom raise
        is provided """
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 25000)
    
    def test_give_custom_raise(self):
        """ Test that a custom raise is given to employee1 if a custom raise
        is provided """
        self.employee1.give_raise(7500)
        self.assertEqual(self.employee1.salary, 27500)

unittest.main()