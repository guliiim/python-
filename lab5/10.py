import  re

s = input() 
s = re.sub(r"([a-z]*)([A-Z])", r'\1_\2', s)

if s[0] == '_':
    s = s.replace(s[0], "", 1)

s = s.lower()
print(s)

