#method-Using Extended slice
'''
Extended slice offers to put a “step” field as [start, stop, step], and giving no field as start and stop
indicates default to 0 and string length respectively,and “-1” denotes starting from the end and stop at the start,
hence reversing a string. 
'''
def reverse(str):
    str=str[::-1]
    return str

s="NIKHIL KUMAR RANA"
print("The original string is:",end=" ")
print(s)
print("The reversed string using extended slice method is :",end=" ")
print(reverse(s))
