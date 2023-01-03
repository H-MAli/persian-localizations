import unittest
from src import *

class TestPersianNumerals(unittest.TestCase):
	def runTest(self):
		per = persian_numerals(1234567890)
		self.assertEqual(per, '۱۲۳۴۵۶۷۸۹۰', 'Persian numeral string is in an incorrect form')

		per = persian_numerals(1111111111)
		self.assertEqual(per, '۱۱۱۱۱۱۱۱۱۱', 'Persian numeral string is in an incorrect form')

class TestLatinToPersian(unittest.TestCase):
	def runTest(self):
		latin = 'Hello, 007!'
		per = latin_to_persian(latin)
		self.assertEqual(per, 'Hello, ۰۰۷!', 'Latin numerals are not correctly translated into their Persian counterparts')

class TestLatinToPersianDecimalPoints(unittest.TestCase):
	def runTest(self):
		latin = 'I bought 69.420 Bitcoins today!'
		perDecimal = latin_to_persian(latin, True)
		per = latin_to_persian(latin)

		self.assertEqual(per, 'I bought ۶۹.۴۲۰ Bitcoins today!', 'Latin to Persian string conversion (decimal point test) discarding decimal point does not work')
		self.assertEqual(perDecimal, 'I bought ۶۹٫۴۲۰ Bitcoins today!', 'Latin to Persian string conversion (decimal point test) does not work')

class TestLatinToPersianQuestionMarks(unittest.TestCase):
	def runTest(self):
		latin = 'Will it rain today?'
		perQ = latin_to_persian(latin, question_mark=True)
		per = latin_to_persian(latin)

		self.assertEqual(per, latin, 'Latin to Persian string conversion (question mark test) discarding question mark does not work')
		self.assertEqual(perQ, 'Will it rain today؟', 'Latin to Persian string conversion (question mark test) does not work')

class TestCleanupArabicCharacters(unittest.TestCase):
	def runTest(self):
		ar = 'كجا مي‌ري؟'
		per = cleanup_arabic_characters(ar)

		self.assertEqual(per, 'کجا می‌ری؟')

class TestCleanupArabicNumbers(unittest.TestCase):
	def runTest(self):
		ar = 'نفر شماره‌ی ٤٥٦ برنده است!'
		per = cleanup_arabic_characters(ar)

		self.assertEqual(per, 'نفر شماره‌ی ۴۵۶ برنده است!')

class TestPersianNumeralString(unittest.TestCase):
	def runTest(self):
		num = 1234567890
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیارد و دویست و سی و چهار میلیون و پانصد و شصت و هفت هزار و هشتصد و نود', 'Simple Persian numeral string not working')

		num = 1000000000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیارد')
		
		num = 1000000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیون')
		
		num = 1000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک هزار')
		
		num = 3003
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'سه هزار و سه')
		
		num = 426000000427
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'چهارصد و بیست و شش میلیارد و چهارصد و بیست و هفت')
		
		num = 405
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'چهارصد و پنج')
		
		num = 9873451
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'نه میلیون و هشتصد و هفتاد و سه هزار و چهارصد و پنجاه و یک')
		
		num = 800000005
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'هشتصد میلیون و پنج')
		
		num = 700000070
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'هفتصد میلیون و هفتاد')
		
		num = 1212121212
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیارد و دویست و دوازده میلیون و صد و بیست و یک هزار و دویست و دوازده')
		
		num = 456852000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'چهارصد و پنجاه و شش میلیون و هشتصد و پنجاه و دو هزار')

class TestPersianBigNumeralString(unittest.TestCase):
	def runTest(self):
		num = 10000000000000000001
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'ده میلیون تریلیون و یک', 'Big Persian numeral string not working')
		
		num = 1000000000000000000000000000000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیون تریلیون تریلیون')
		
		num = 1000000000001000000000001000000000001000000000001001001
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'یک میلیون تریلیون تریلیون تریلیون تریلیون و یک میلیون تریلیون تریلیون تریلیون و یک میلیون تریلیون تریلیون و یک میلیون تریلیون و یک میلیون و یک هزار و یک')
		
		num = 111222333444555666777888999000
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'صد و یازده هزار و دویست و بیست و دو تریلیون تریلیون و سیصد و سی و سه میلیارد و چهارصد و چهل و چهار میلیون و پانصد و پنجاه و پنج هزار و ششصد و شصت و شش تریلیون و هفتصد و هفتاد و هفت میلیارد و هشتصد و هشتاد و هشت میلیون و نهصد و نود و نه هزار')
		
		num = 13987415000333
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'سیزده تریلیون و نهصد و هشتاد و هفت میلیارد و چهارصد و پانزده میلیون و سیصد و سی و سه')

class TestPersianNegativeNumeralString(unittest.TestCase):
	def runTest(self):
		num = -10000000000000000001
		per_str = persian_numeral_string(num)

		self.assertEqual(per_str, 'منفی ده میلیون تریلیون و یک')

class TestPersianOrdinalString(unittest.TestCase):
	def runTest(self):
		num = 1521
		ordinal = persian_ordinal_string(num)

		self.assertEqual(ordinal, 'یک هزار و پانصد و بیست و یکم')

		num = 33
		ordinal = persian_ordinal_string(num)

		self.assertEqual(ordinal, 'سی و سوم')

		num = 1
		ordinal = persian_ordinal_string(num)

		self.assertEqual(ordinal, 'اول')

		num = 0
		ordinal = persian_ordinal_string(num)

		self.assertEqual(ordinal, 'صفرم')

class TestPersianCountingOrdinalString(unittest.TestCase):
	def runTest(self):
		num = 1521
		ordinal = persian_counting_ordinal_string(num)

		self.assertEqual(ordinal, 'یک هزار و پانصد و بیست و یکمین')

		num = 33
		ordinal = persian_counting_ordinal_string(num)

		self.assertEqual(ordinal, 'سی و سومین')

		num = 1
		ordinal = persian_counting_ordinal_string(num)

		self.assertEqual(ordinal, 'اولین')

		num = 0
		ordinal = persian_counting_ordinal_string(num)

		self.assertEqual(ordinal, 'صفرمین')
