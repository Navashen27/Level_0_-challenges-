#Program to check Common Letters in Two input string 

str1=input("hey:")
str2=input("hello:")
s=list(set(str1)&set(str2))
print("The common letters are:")
for i in s:
 print(i)