
#list Data type
l=['python',3,'in', 'one']
print(type(l)) #type of l
print(len(l)) #length of l


#slicing operations on list
print(l[0])
print(l[-1])
print(l[1:-1])
    
#Alter operations on list
print(l.append('pic'))
print(l)
print(l.insert(2,'4.1')) # here for insert 2 indicate index where we are inserting value
print(l)
print(l.extend(['!','!']))#extend() adds the elements of another list to the current list.
print(l)

print(l.pop())
print(l.pop(2))#pop operation on second index
l.remove('in')# removed 'in' from list
print(l)

del l[2]#deleted element at 2nd index
print(l)

print(l.index('pic'))# get index for element 'pic' from list
