def reverseStr(s):
    if len(s)==0:
        return s
    else:
        return reverseStr(s[1:])+s[0]
    
str="NIKHIL KUMAR RANA"
print(reverseStr(str))