# python chinese numeral 
# Suzhou FaMa 蘇州碼子 numerals
#
# Alex Mak
#
# translate into 花碼 'fama' symbols, determine unit.

# Numerals:
# 〇〡〢〣〤〥〦〧〨〩
# 0123456789

# Units: 万 千 百 十

# 2076
#
# 〢〇〧〦
# 千

# 10
# 〡〇
# 〸

# 44
# 〤〤
# 十

# 97015
# 〩〧〇〡〥
# 万

# 10,000
# 〡 〇〇
# 万

#100,000 

#十〇〇
#万


def readAmount():
	isValidWord = False
	value = ""
	yun = 0
	
	while not isValidWord:
	
		hasDollar = False
		value = input("Please enter amount:")

		if (value.startswith('$')):
			hasDollar = True
			value = value[1:]

		a = float(value)
		hou = int(round(a % 1,2) * 100)  # 毫仙
		yun = int(a //1)      # 元
		
		if (yun) > 10000:
			print(f"Sorry, number is too big, less than 100000 digits please.")
			continue
		else:
			isValidWord = True

		#print(yun)
		#print(hou)

	return str(yun), hasDollar



def determineUnit(number):

	num_of_digits = len(number)

	if (num_of_digits == 5):
		unit = "万"
	elif (num_of_digits == 4):
		unit = "千"
	elif (num_of_digits == 3):
		unit = "百"
	elif (num_of_digits == 2):
		unit = "十"
	else:
		unit = ""

	return unit


# simplistic map
# handle 1, 2, 3 alternates later

digits = "〇〡〢〣〤〥〦〧〨〩"

def map_num(n):
	return digits[int(n)]



def fama(number):

	for i,c in enumerate(number):
		print(map_num(c), end='')

	print()



def main():

	number_dollar = readAmount()
	number = number_dollar[0]

	fama(number)
	unit = determineUnit(number)
	print(unit, end="")

	if (number_dollar[1] == True):
		print('元')

	print()


if __name__ == "__main__":
	main()