import unittest
from solution import solution

class TestSolution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(solution(10,20,"+"),30)
	def test_subtraction(self):
		self.assertTrue(solution(10,5,"-"),5)
	def test_subtraction(self):
		self.assertNotEqual(solution(5,10,"-"),-5)
	def test_multiplication(self):
		self.assertEqual(solution(6,3,"*"),18)
	def test_division(self):
		self.assertEqual(solution(9,3,"/"),3)
	def test_division(self):
		self.assertNotEqual(solution(3,6,"/"),0.2)

if __name__=='__main__':
	unittest.main()