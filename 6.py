def filter_prime(l):
    for i in range(len(l)):
        if (l[i] >= 2) & check(l[i]):
            print(l[i], end = " ")
def check(x): 
    for i in range(2,x):
        if x % i == 0:
            return False
    return True    

l = [int(x) for x in input().split()]
filter_prime(l)