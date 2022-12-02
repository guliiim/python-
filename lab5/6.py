import re

s = input()
s2 = re.sub(r"[\s,.]", ":", s)
print(s2)