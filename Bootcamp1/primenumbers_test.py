import unittest
from primenumbers import primenumbers
class TestPrimenumbers(unittest.TestCase):
	def test_False(self):
		self.assertTrue(primenumbers(10))

if __name__=='__main__':
	unittest.main()
