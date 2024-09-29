import unittest
import fama

# python famaTest.py

class TestFama(unittest.TestCase):

	def __init__(self, methodName='runTest'):
		super().__init__(methodName)

		self.checker = fama.fama()

	def test_isAmountValid(self):
		result = self.checker.isAmountValid( 0)
		self.assertEqual(result, True)
		esult = self.checker.isAmountValid(23.12)
		self.assertEqual(result, True)
		result = self.checker.isAmountValid(-4)
		self.assertEqual(result, False)
		result = self.checker.isAmountValid(9999999)
		self.assertEqual(result, False)
        
	def test_determineUnit(self):
		result = self.checker.determineUnit('12345')
		self.assertEqual(result, '万')

		result = self.checker.determineUnit('9991')
		self.assertEqual(result, '千')

		result = self.checker.determineUnit('312')
		self.assertEqual(result, '百')

		result = self.checker.determineUnit('22')
		self.assertEqual(result, '十')


	def test_parseAmount(self):

		number_dollar = [123, False]
		result = self.checker.parseAmount(number_dollar)
		self.assertEqual(result[0],'123')
		self.assertEqual(result[1], '0')

		number_dollar = [123.45, False]
		result = self.checker.parseAmount(number_dollar)
		self.assertEqual(result[0],'123')
		self.assertEqual(result[1], '45')
		
		number_dollar = [0.25, True]  # $0.25
		result = self.checker.parseAmount(number_dollar)
		self.assertEqual(result[0],'0')
		self.assertEqual(result[1], '25')
		self.assertEqual(result[2], '毫')

	def test_fama_number(self):
		number = '4567'
		result = self.checker.fama_number(number)
		self.assertEqual(result, '〤〥〦〧')


if __name__ == "__main__":
    unittest.main()
