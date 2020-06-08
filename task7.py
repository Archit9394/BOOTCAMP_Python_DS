# 7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

string1="Python is an interpreted language"

vowel=["a","e","i","o","u"]

def reverse(string1):
    string2=""
    for i in range(len(string1)-1,0,-1):
        if string1[i] not in vowel:
            string2+=string1[i]
    return string2

result=reverse(string1)
print (result)