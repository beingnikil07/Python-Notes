num=int(input("Enter a Number"))
if num<2:
    print("Not a Prime Number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime number")
            break
        else:
            print(" Prime Number")
