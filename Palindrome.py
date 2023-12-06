num=int(input("Enter a Number:"))
sum=0
temp=num;
while temp>0:
    digit=temp%10
    sum=sum*10+digit
    temp=temp//10

if num==sum:
    print("Number is Palindrome")
else:
    print("Not Palindrome")