# Searching an element in list
"""We need to find the element is avilable in the list or not, If avilable then how many number of occurenc"""
# 1. Checking for existence
# in and not in operator are used to get the result in Boolean
l = [5, 2, 3]
print(5 in l)
print(9 in l)
print(9 not in l)
l = ["a", "b", "a", "c", "b", 5, 4, 6, 6, 5, 1]
###How many numbers of occurrence available in the list
print(l.count(1))
print(l.count('b'))
print(l.count('c'))
print(l.count(78))
##### Now we need to find out the position of  an element of first occurence available in the list
# condition, If an element is not available in the list then will get value error
l=[1,9,4,3,5,0,8,9,1,0]
print(l.index(9))
print(l.index(0))
#print(l.index(23))
# l.index(x,i) where i is the start of element
#print(l.index(9,1))
#l.index(x,i,j), where j is the last of element to search, excluding the last element
l=[5,2,3,2]
print(l.index(2,0,2))



