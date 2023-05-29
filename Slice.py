## A list slice is a sub-list extracted from a list
## default slice will start from 0 to till end, excluding the last one.
l = [5, 2, 3, 2]
print(l[0:3])
print(l[1:])
print(l[:3])
print(l[:])
# using slice to modify the existing content of list
l=[5,2,3,2]
l[1:3]=[3,2]
# 5, 3, 2, 2
print(l)
l=[5,2,3,2]
l[1:3]=[3,0,0,2]
# 5, 3, 0, 0, 2, 2
print(l)
l=[5,2,3,2]
l[1:3]=[9]
#5, 9, 2
print(l)
l=[5,2,3,2]
l[1:2]=[9]
#5, 9, 3, 2
print(l)
l=[5,2,3,2]
l[1:1]=[9,8,9]
#5, 9, 8, 9, 2, 3, 2
print(l)
l=[5,2,3,2]
l[1:2]=[]
#5, [], 3, 2
print(l)
l=[5,2,3,2]
l[2:]=[]
print(l)
l=[5,2,3,2]
print(l[:2])
l[:2]=[]
l[:]=[]
print(l)
#5,2
print(l)

