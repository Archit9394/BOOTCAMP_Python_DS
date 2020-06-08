# 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab  
#     Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

dic1={}
string1="12abcbacbaba344ab"

for i in string1:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        if i in dic1:
            dic1[i]+=1
        else:
            dic1[i]=1