import unittest
from solution import solution

class TestSolution(unittest.TestCase):
	def test_addition(self):
		self.assertTrue(solution(10,20,"+"),30)


if __name__=='__main__':
	unittest.main()