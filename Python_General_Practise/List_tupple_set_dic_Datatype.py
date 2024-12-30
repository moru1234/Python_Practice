#__________________________List_________________________________________________________
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

#__________________________Tupple_________________________________________________________
tp =(1,2,3,[4,5]) #tupple is immutable data type
print(type(tp))

print(len(tp))
print(tp[2])#get element at index 2 from tupple tp

#Key Learnings:
#Tuples are immutable: You cannot add, remove, or reassign elements in a tuple directly.
#Mutable elements in tuples: If a tuple contains a mutable object (like a list), you can modify the contents of that object.
#Example:
#tp = (1, 2, 3, [4, 5])
#tp[3][1] = 6 modifies the list [4, 5] to [4, 6], but the tuple structure remains unchanged.
#This demonstrates that tuple immutability applies only to its structure, not to the contents of its mutable elements.
#tp[2]=10 # this will give me error 
tp[3][1]=6 # though tupple is mutable but we will still be able to modify list inside tupple
print(tp)

tp=(1,) #Writing tp = (1,) does not modify the original tuple; it reassigns the variable tp to a new tuple (1,)
print(tp)


#assign multiple values
v=(3,2,'a')
(c,b,a) =v
print(a,b,c)
#__________________________Set_________________________________________________________
