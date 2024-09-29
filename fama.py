# fama class
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

class fama:

	def __init__(self):
		pass


	def isAmountValid(self, amount):
		if (amount >= 100000 or amount < 0):
			return False

		return True


	def parseAmount(self, number_dollar):

		value = number_dollar[0]
		hasDollar = number_dollar[1]

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


	def determineUnit(self, number):

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
	def map_num(self, n):
		digits = "〇〡〢〣〤〥〦〧〨〩"
		return digits[int(n)]

	#alternates
	def map_num2(self, n):
		digits2 = " 一二三"
		return digits2[int(n)]

	def fama_number(self, number):

		numeric_number = []
		fama_number = []
		for i,c in enumerate(number):
			numeric_number.append(c)
			fama_number.append(self.map_num(c))

		i = 0  
		while i < len(numeric_number)-1:
			n = int(numeric_number[i])
			next_n = int(numeric_number[i+1])

			if (n >= 1 and n <= 3) and (next_n >= 1 and next_n <= 3):
				fama_number[i+1] = self.map_num2(next_n)

			i += 2

		print("".join(fama_number), end = "")



