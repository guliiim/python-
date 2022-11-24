n=int(input())

def out(n):
    while n >=0:
        yield n
        n-=1
    
for i in out(n):
    print(i)