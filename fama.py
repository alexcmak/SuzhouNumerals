# python Suzhou Numerals 蘇州碼子
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
	money_unit = ""
	
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

	remainder = "0"
	amount = str(yun)
	if (hasDollar == True):
		money_unit = '元'
		remainder = str(hou)

		if (yun == 0):
			money_unit = '毫'
			remainder = str(hou)

			if (hou < 9):
				money_unit = '仙'
				remainder = str(hou)
	else:
		remainder = str(hou)
		

	return amount, remainder, money_unit



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
digits = "〇〡〢〣〤〥〦〧〨〩"

def map_num(n):
	return digits[int(n)]

#alternates
digits2 = "〇一二三〤〥〦〧〨〩"

def map_num2(n):
	return digits2[int(n)]

def fama(number):

	numeric_number = []
	fama_number = []
	for i,c in enumerate(number):
		numeric_number.append(c)
		fama_number.append(map_num(c))

	i = 0  
	while i < len(numeric_number)-1:
		n = int(numeric_number[i])
		next_n = int(numeric_number[i+1])

		if (n >= 1 and n <= 3) and (next_n >= 1 and next_n <= 3):
			fama_number[i+1] = map_num2(next_n)

		i += 2

	print("".join(fama_number), end = "")


def main():

	number_dollar = readAmount()
	number = number_dollar[0]
	remainder = number_dollar[1]

	#print(number)
	#print(remainder)

	if (int(number) > 0):
		fama(number)

	if (int(remainder) > 0):
		fama(remainder)
	print()
	

	unit = determineUnit(number)
	print(unit, end="")

	print(number_dollar[2])


	print()


if __name__ == "__main__":
	main()
