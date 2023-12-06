def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)

#teking n
n=int(input("input a number till you want to print fibbonacci series:"))
if n<=0:
    print("Enter a positive number")
else:
    for i in range(n):   #by default range function starting index is 0
        print(fib(i),end=" ")
    