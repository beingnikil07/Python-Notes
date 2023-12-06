num=int(input("Enter a Number:"))
sum=0
#find the cube of each digit 
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if num==sum:
    print("Armstrong number")
else:
    print("Not Armstrong")