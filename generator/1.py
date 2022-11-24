n=int(input())
def square(n):
    for i in range(n):
        yield i**2

for i in square(n):
    print(i)
