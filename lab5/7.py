import  re

s = input() # i_got_intern_at_geeksforgeeks
s = re.findall(r"[a-z]+", s) 

for i in range(len(s)): 
    s[i] = s[i].capitalize()

print("".join(s)) # IGotInternAtGeeksforgeeks