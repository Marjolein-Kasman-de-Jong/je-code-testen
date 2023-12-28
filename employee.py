# Opdracht 11-3 Medewerker

class Employee():
    """ Class that calculates employee salary after a raise """

    def __init__(self, first_name, last_name, salary):
        """ Store employee first name, last name and salary """
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, employee_raise = 5000):
        """ Add raise to employee salary """
        self.salary = self.salary + employee_raise