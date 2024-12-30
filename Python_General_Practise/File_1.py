#a= 1
#A=2
#print(a is not A)
a=1
print (type(a))
b=0x10
print(type(b))
c=complex(1,3)
print(type(c))
#__________________________________________
print(1+1)
print(2-2)
print(3*3)
print(5/3)
print(2**4)#Exponentiation - Raises the first number to the power of the second.
print(5//4)#Floor Division - Divides the first number by the second and returns the integer quotient
print(5%4)#Modulus  - Divides the first number by the second and returns the remainder.
#____________________________________________________________
#print(float.__doc__)
#print(int.__doc__)

print(int("1010",base =2)) # Output is 10
s1 = ':dog:\n'
s2 = "Hello World"
s3 ="""Hello Google"""
print(type(s1), type(s2),type(s3))
print(s1,"\n",s2,"\n",s3,"\n")
print(len(s1),len(s2),len(s3))
#____________________________________________________________
print("abc"+"."+"study") # string concatination
s = "study and practice"
print(s)
print('{0}:{1}'.format(s[:-5],s[-8]))
#'{0}:{1}'.format(s[:-5], s[-8]) becomes "study and pra:p".
#s[:-5]: Slices the string to exclude the last 5 characters. Result: "study and pra".
#s[-8]: Gets the 8th character from the end. Result: "p".
#'{0}:{1}'.format(...): Formats the string by replacing {0} with "study and pra" and {1} with "p"

#
#print(str.__doc__)
print(str(3))
print(str(3.14))
#________________________________
byt = b'abc' #b'abc' creates a byte literal, which is a sequence of bytes (raw binary data) instead of a regular string.
print(type(byt))
print(byt[0]) #output is 97 which is ASCII value for a
#____________________________________________________________

