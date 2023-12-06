#find all prime intervals 
lower=int(input("Enter Lower limit here :"))
upper=int(input("Enter upper limit here:"))

for num in range(lower,upper+1):
    if num>1: 
        for i in range(2,num):
             if num%2==0:
                    # Not will prime number if this condition is true
                    break
        
        else:       #here else is not in the block of if it is separate 
            print(num)   #if upper condition is not true then number will prime and we will print the number 
    