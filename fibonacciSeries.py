num=int(input("Enter a Number till you want to print febbonacci series:"))
n1=0
n2=1
sum=0
if num<=0:
    print("Please enter number greater than zero")
else:
    for i in range(0,num):    #range function always stars from 0 
        print(sum,end=" ")      
        #Now swap the values 
        n1=n2
        n2=sum
        sum=n1+n2
