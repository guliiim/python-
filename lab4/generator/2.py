n=int(input())

def even(n):
    for i in range(n):
        if(i%2==0):
            print(i,end=",")

even(n)