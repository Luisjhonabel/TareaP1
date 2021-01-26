import unittest
import main

class ClassName(unittest.TestCase):
	"""docstring for ClassName"""
	def test_something(self):
		resultado = main.calcular("11101+1101")
		self.assertEqual(resultado,"42")
		resultado = main.calcular("11101-1101")
		self.assertEqual(resultado,"16")
		resultado = main.calcular("11101*1101")
		self.assertEqual(resultado,"377")
		resultado = main.calcular("1100100/000010")
		self.assertEqual(resultado,"50.0")
		resultado = main.calcular("1100100or000010")
		self.assertEqual(resultado,"100")
		resultado = main.calcular("1100100and000010")
		self.assertEqual(resultado,"2")


if __name__ == '__main__':
	unittest.main()


