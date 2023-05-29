l=[5,2,3]
print(l[0])
####Accesing list of an element
print(l[1])
print(l[-1])
print(l)
######Elemnet of a list can be freely modified
l=[5,2,3]
l[0]=0
print(l)
l[0]=l[1] + l[2]
print(l)
######counting list element
l=[5,2,3]
print(len(l))
l=[5]
print(type(l))
print(len(l))
l=[]
print(len(l))
####Iterating through list element
for i in [5,3,2]:
    print(i)