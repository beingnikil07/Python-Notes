num=int(input("Enter a Number"))
sum=0
i=1
while (i<num):
    if num%i==0:
        sum=sum+i
    i=i+1

if num==sum:
    print("Perfect Number")
else:
    print("Number is not a perfect number")