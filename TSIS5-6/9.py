import re
def TM(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'

a =input()
print(TM(a))