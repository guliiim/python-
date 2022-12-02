import re
s = input()

print(re.search(r"[a-z]+_[a-z]+", s))