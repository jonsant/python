import unittest
from ch11_3_employee import Employee

class EmployeeTests(unittest.TestCase):
	"""Test the Employee Class"""
	
	def setUp(self):
		self.my_employee = Employee("anton", "tj", 1000)
	
	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.annual_salary, 6000)
		
	def test_give_custom_raise(self):
		self.my_employee.give_raise(8000)
		self.assertEqual(self.my_employee.annual_salary, 9000)
		
unittest.main()
