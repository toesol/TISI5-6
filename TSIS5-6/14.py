import re
def TM(text):
        patterns = '[a-zA-z0-9_]'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return 'Not matched!'
a = input()
print(TM(a))