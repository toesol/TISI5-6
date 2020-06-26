import re
def TM(text):
        patterns = '^[a-z]+_[a-z]+$'
        if not re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'

a =input()
print(TM(a))