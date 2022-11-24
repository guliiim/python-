a=int(input())
b=int(input())

def f(a,b):
    for i in range(a,b+1):
        yield i**2

for x in f(a,b):
    print(x)
