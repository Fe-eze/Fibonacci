# A function that finds the first n fibonacci numbers given a value of n
def fib(n):
    a = 0
    b = 1
    print("displaying the first ", n, " fibonacci numbers: \n")
    print(a)
    print(b)
    for i in range(0,n-2):
        c = a+b
        print(c)
        a=b
        b=c
