l = [5, 2, 3]
# To add the one or more element at the end of list
l.append(9)
print(l)
l1 = [20, 30]
l.append(l1)
print(l)
print(l[4])
print(l[4][1])
l1 = [5, 2, 3]
l2 = [7, 8, 9]
l1.extend(l2)
print(l2)
print(l1)
### Insert the element at index position, if the index position is out of range then it will add at end of index
l=[7,8,9]
print("hello")
l.insert(20,3)
l=[5,2,3,3]
l.insert(50,9)
print(l)
l.insert(0,20)
print(l)
## Deleting an element
    ## by the position, If the position is out of range then will get index out of range
l=[5,2,3,2]
del l[0]
print(l)
#del l[20]; will get IndexError: out of range
print(l)


