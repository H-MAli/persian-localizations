# persian_localizations
A Python package to facilitate Persian language localizations.

## Install

```
pip install persian_localizations
```

## Usage
Here are a list of functions available to you through `persian_localizations`:

- `latin_to_persian(latin, decimal_point=False, question_mark=False)`: Lets you convert some latin characters to their Persian counterparts:
```python
# required imports
from persian_localizers import latin_to_persian

# Turn any occurrence of a lating digit character to its Persian equivalent
latin_to_persian('من 69 سال دارم!') # Returns 'من ۶۹ سال دارم!'

# The same function can handle decimal marks as well, if directed to do so
latin_to_persian('69.420، همین‌جوری!', decimal_point=True) # Returns '۶۸٫۴۲۰، همین‌جوری!' 

# You can also change latin (LTR) question marks to Persian (RTL)
latin_to_persian('چی شد?', question_mark=True) # Returns 'چی شد؟'
```
- `persian_numerals(num)`: Lets you convert an `int` value to its Persian counterpart:
```python
# required imports
from persian_localizers import persian_numerals

# Turn 123 to Persian-script string
persian_numerals(123) # Returns '۱۲۳'
```
- `cleanup_arabic_characters(problematic)`: Lets you clean-up a Persian `str` value containing some unintended Arabic characters:
```python
# required imports
from persian_localizers import cleanup_arabic_characters

# Changes Arabic letter ي (non-existent in Persian) to ی
cleanup_arabic_characters('مي‌روم') # Returns 'می‌روم'
```
- `persian_numeral_string(num)`: Converts an `int` value to its written-out form in Persian:
```python
# required imports
from persian_localizers import persian_numeral_string

persian_numeral_string(1234) # Returns 'هزار و دویست و سی و چهار'
```
- `persian_ordinal_string(num)`: Converts an `int` value to its written-out form in Persian in ordinal form (اول, دوم, etc.):
```python
# required imports
from persian_localizers import persian_ordinal_string

persian_ordinal_string(25) # Returns 'بیست و پنجم'
```
- `persian_counting_ordinal_string(num)`: Converts an `int` value to its written-out form in Persian in counting ordinal form (اولین, دومین, etc.):
```python
# required imports
from persian_localizers import persian_counting_ordinal_string

persian_counting_ordinal_string(1121) # Returns 'یک هزار و صد و بیست و یکمین'
```

## Contributing

Your Pull Request submissions are welcome!

## License

Apache License © Mohammad Ali Haghshenas

See [LICENSE](./LICENSE) for more.