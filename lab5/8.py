import re

s = input()
print(re.findall(r"[A-Z][a-z]*", s))