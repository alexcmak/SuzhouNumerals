# python Suzhou Numerals 蘇州碼子
#
# Alex Mak
#

from fama import fama

Fama = fama()

def readAmount():
	isValidWord = False
	value = ""
	amount = 0

	while not isValidWord:
	
		hasDollar = False
		amount = input("Please enter amount:")

		if (amount.startswith('$')):
			hasDollar = True
			amount = amount[1:]

		value = float(amount)

		if (Fama.isAmountValid(value) == False):
			print(f"Sorry, invalid number 0 to 100000 please.")
			continue
		else:
			isValidWord = True

	return value, hasDollar

def main():

	number_dollar = readAmount()
	number_dollar = Fama.parseAmount(number_dollar)
	number = number_dollar[0]
	remainder = number_dollar[1]

	#print(number)
	#print(remainder)

	if (int(number) >= 0):
		Fama.fama_number(number)

	if (int(remainder) > 0):
		Fama.fama_number(remainder)
	print()
	

	unit = Fama.determineUnit(number)
	print(unit, end="")

	print(number_dollar[2])

	print()

if __name__ == "__main__":
	main()
