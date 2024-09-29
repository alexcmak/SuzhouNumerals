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

		
		if (value >= 100000 or value < 0):
			print(f"Sorry, invalid number 0 to 100000 please.")
			continue
		else:
			isValidWord = True

	return parseAmount(value, hasDollar)

def parseAmount(value, hasDollar):

	money_unit = ""
	hou = int(round(value % 1,2) * 100)  # 毫仙
	yun = int(value //1)      # 元

	remainder = "0"
	sAmount = str(yun)
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
		

	return sAmount, remainder, money_unit



def determineUnit(number):

	num_of_digits = len(number)


	match num_of_digits:
		case 5:
			unit = '万'
		case 4:
			unit = '千'
		case 3:
			unit = '百'
		case 2:
			unit = '十'
		case _:
			unit = ''


	return unit


# simplistic map
digits = "〇〡〢〣〤〥〦〧〨〩"

def map_num(n):
	return digits[int(n)]

#alternates
digits2 = " 一二三"

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

	if (int(number) >= 0):
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
