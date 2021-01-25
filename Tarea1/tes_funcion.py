import unittest
from . import funcion


class ClassName(unittest.TestCase):
	"""docstring for ClassName"""
	def test_something(self):
		r = funcion.function(3,4)
		self.assertEqual(r,12)

if __name__ == '__main__':
	unitest.main()
		
