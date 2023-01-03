'''
A set of functions to get Persian language normalized string variants
'''

import re, locale
from typing import List

def persian_numerals(num: int) -> str:
	'''
	Converts the given number to its Persian script counterpart
	
	Parameters
	----------
	num: int
		The number to be converted to Persian
	'''
	return latin_to_persian(str(num))

def latin_to_persian(latin: str, decimal_point: bool = False, question_mark: bool = False) -> str:
	
	'''
	Converts some misused latin characters in the given text to their Persian counterparts
	
	Parameters
	----------
	latin: str
		The original string to be converted to Persian

	decimal_point: bool
		Whether to convert decimal points to Persian

	question_mark: bool
		Whether to convert question marks to Persian
	'''

	if decimal_point:
		decimalSep = re.escape(locale.localeconv()["decimal_point"])
		latin = re.sub(r"(\d)" + decimalSep + "(\d)", r'\1٫\2', latin)

	if question_mark:
		latin = latin.replace('?', '؟')

	return latin.replace('1', '۱')\
		.replace('2', '۲')\
		.replace('3', '۳')\
		.replace('4', '۴')\
		.replace('5', '۵')\
		.replace('6', '۶')\
		.replace('7', '۷')\
		.replace('8', '۸')\
		.replace('9', '۹')\
		.replace('0', '۰')

def cleanup_arabic_characters(problematic: str) -> str:
	'''
	Substitutes commonly misused Arabic-specific characters such as 'ي' with theirs Persian counterparts
	
	Parameters
	----------
	problematic: str
		The string (supposedly Persian) containing Arabic characters
	'''
	return problematic.replace('ك', 'ک').replace('ي', 'ی').replace('٥', '۵').replace('٤', '۴').replace('٦', '۶')

def persian_numeral_string(num: int) -> str:
	'''
	Converts the given number to its Persian string counterpart
	
	Parameters
	----------
	num: int
		The number to be converted to Persian string
	'''

	prefix = ''

	if num < 0:
		num *= -1
		prefix = 'منفی '
	elif num == 0:
		return 'صفر'

	quints = get_quadruplets(num)

	outer_str_parts = []
	for x, q in enumerate(quints):
		str_parts = []
		for n, i in enumerate(q):
			match n:
				case 0:
					if i > 0:
						str_parts.append('{} میلیارد'.format(triplet_to_string(i)))
				case 1:
					if i > 0:
						str_parts.append('{} میلیون'.format(triplet_to_string(i)))
				case 2:
					if i > 0:
						str_parts.append('{} هزار'.format(triplet_to_string(i)))
				case 3:
					if i > 0:
						str_parts.append('{}'.format(triplet_to_string(i)))
		
		suffix_count = len(quints) - 1 - x

		suffix_arr = []
		for i in range(suffix_count):
			suffix_arr.append('تریلیون')

		suffix = ' ' + ' '.join(suffix_arr)

		joined = ' و '.join(str_parts)

		part = joined if suffix_count == 0 or len(joined) == 0 else joined + suffix

		if len(part) > 0:
			outer_str_parts.append(part)

	return prefix + ' و '.join(outer_str_parts)

def persian_ordinal_string(num: int) -> str:
	'''
	Converts the given number to its Persian ordinal string counterpart; e.g. 1 to اول
	
	Parameters
	----------
	num: int
		The number to be converted to Persian ordinal string
	'''

	if num == 0:
		return 'صفرم'
	elif num == 1:
		return 'اول'

	num_str = persian_numeral_string(num)

	if num_str.endswith(' سه'):
		return num_str[0:-2] + 'سوم'
	else:
		return num_str + 'م'

def persian_counting_ordinal_string(num: int) -> str:
	'''
	Converts the given number to its Persian counting ordinal string counterpart; e.g. 1 to اولین
	
	Parameters
	----------
	num: int
		The number to be converted to Persian counting ordinal string
	'''

	return persian_ordinal_string(num) + 'ین'

def triplet_to_string(num: int) -> str:
	if num < 1 or num > 999:
		raise ValueError(num)

	hundreds = num // 100
	tens = (num - (hundreds * 100)) // 10
	ones = (num - (hundreds * 100 + tens * 10))

	all = [hundreds, tens, ones]
	strings = []

	for n, i in enumerate(all):
		match n:
			case 0:
				match i:
					case 1:
						strings.append('صد')
					case 2:
						strings.append('دویست')
					case 3:
						strings.append('سیصد')
					case 4:
						strings.append('چهارصد')
					case 5:
						strings.append('پانصد')
					case 6:
						strings.append('ششصد')
					case 7:
						strings.append('هفتصد')
					case 8:
						strings.append('هشتصد')
					case 9:
						strings.append('نهصد')
			case 1:
				match i:
					case 2:
						strings.append('بیست')
					case 3:
						strings.append('سی')
					case 4:
						strings.append('چهل')
					case 5:
						strings.append('پنجاه')
					case 6:
						strings.append('شصت')
					case 7:
						strings.append('هفتاد')
					case 8:
						strings.append('هشتاد')
					case 9:
						strings.append('نود')
			case 2:
				match i:
					case 0:
						if tens == 1:
							strings.append('ده')
					case 1:
						if tens == 1:
							strings.append('یازده')
						else:
							strings.append('یک')
					case 2:
						if tens == 1:
							strings.append('دوازده')
						else:
							strings.append('دو')
					case 3:
						if tens == 1:
							strings.append('سیزده')
						else:
							strings.append('سه')
					case 4:
						if tens == 1:
							strings.append('چهارده')
						else:
							strings.append('چهار')
					case 5:
						if tens == 1:
							strings.append('پانزده')
						else:
							strings.append('پنج')
					case 6:
						if tens == 1:
							strings.append('شانزده')
						else:
							strings.append('شش')
					case 7:
						if tens == 1:
							strings.append('هفده')
						else:
							strings.append('هفت')
					case 8:
						if tens == 1:
							strings.append('هجده')
						else:
							strings.append('هشت')
					case 9:
						if tens == 1:
							strings.append('نوزده')
						else:
							strings.append('نه')

	return ' و '.join(strings)

def get_triplets(num: int) -> List[int]:
	res = []

	while num > 0:
		next = num // 1000
		triplet = num - (next * 1000)
		res.insert(0, triplet)
		num = next

	return res

def get_quadruplets(num: int) -> List[List[int]]:
	triplets = get_triplets(num)

	res = []

	while len(triplets) > 0:
		inner = []

		for _ in range(4, 0, -1):
			if len(triplets) == 0:
				inner.insert(0, 0)
				continue

			num = triplets.pop()
			inner.insert(0, num)

		res.insert(0, inner)

	return res
