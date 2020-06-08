# 4. Create a list of thousand number using range and xrange and see the difference between each other.

list1=xrange(1,1001) #Didn't work in python3 #
print (type(list1))
print(list1)
list2=range(1,1001)
print(list2)
print (type(list2))

#Python2
#xrange gives xrange object
#range gives a static list
#xrange is really useful when we have to generate large range as it doesn't take too much memory space unlike range, since xrange creates values as you need them


#Python3
#xrange is not available in python3
#Range gives a class 'range'

