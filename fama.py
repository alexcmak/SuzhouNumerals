# python chinese numeral 
# Suzhou FaMa 蘇州碼子 numerals

# translate into 花碼 'fama' symbols, determine unit.


#0	〇
#1	〡
#2	〢
#3	〣
#4	〤
#5	〥
#6	〦
#7	〧
#8	〨
#9	〩
#10	〸

#万 千 百 十

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



def readWholeNumberFromUser():
	isValidWord = False
	str = ""
	hasDollar = False

	while not isValidWord:
		str = input("Please enter a number or dollar value:")

		if (str.startswith('$')):
			hasDollar = True
			str = str[1:]

		if int(str) > 10000:
			print(f"Sorry, number is too big, less than 10000 digits please.")
			continue
		else:
			# check for all digit
			if (str.isdigit()):
				isValidWord = True

	return str, hasDollar

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
def map_num(n):

	if (n == '0'):
		unit = '〇'
	elif (n == '1'):
		unit = '〡'
	elif (n == '2'):
		unit = '〢'
	elif (n == '3'):
		unit = '〣'
	elif (n == '4'):
		unit = '〤'
	elif (n == '5'):
		unit = '〥'
	elif (n == '6'):
		unit = '〦'
	elif (n == '7'):
		unit = '〧'
	elif (n == '8'):
		unit = '〨'
	elif (n == '9'):
		unit = '〩'
	else:
		unit = ''


	return unit


def fama(number):

	for i,c in enumerate(number):
		print(map_num(c), end='')

	print()



def main():

	number = readWholeNumberFromUser()

	fama(number[0])
	unit = determineUnit(number)
	print(unit, end="")

	if (number[1] == True):
		print('元')

	print()



if __name__ == "__main__":
	main()