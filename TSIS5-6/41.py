import re
text1 = '**//Python Exercises// - 12. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))