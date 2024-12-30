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

st = {'s','e','t'} #A set is an unordered collection of unique elements. Mutable: 
print(type(st))

print(len(st))
st =set()# print empty set - In Python, {} is reserved for dictionaries. To avoid ambiguity, you must use set() to create an empty set.
st.add(1)
print(st, len(st))
st={}#Note: {} creates an empty dictionary, not a set
print(type(st))

#_____________
st1=set(['s','e','t','1'])
st1.add('W')
st1.add('O')
st1.update(['!','!']) #st1.update(['!', '!']) attempts to add '!' twice, but sets store unique elements, so only one '!' is added.
print(st1) # {'O', '1', '!', 't', 's', 'e', 'W'} = The order of elements is arbitrary and does not match the insertion order. - When printing a set, Python internally determines the display order based on its hash table structure.

st1.discard('t')
print(st1)
#st1.remove('T') # Raises KeyError if 'T' is not in the set
print(st1.pop())
st1.clear()
#___________________________________________________________Dic______________________
dic ={}
print(type(dic))

dic ={'k1':'v1','k2':'v2','k3':'v3'}
print(len(dic))

print(dic['k1'])
print(dic.get('k1'))

print(dic.get('k4','v0')) #The get() method allows you to specify a default value if the key is not found.
print(dic)

dic['k3'] ='v2'
print(dic)

print('k2' in dic)
