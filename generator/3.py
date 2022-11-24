n=int(input())

def f(n):
    for i in range(1,n):
        if ((i%3==0) and (i%4==0)):
            print(i)

f(n)