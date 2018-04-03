import re

s=str(input())
specialChars = len(s) - len( re.findall('[\w]', s) )
print(specialChars)