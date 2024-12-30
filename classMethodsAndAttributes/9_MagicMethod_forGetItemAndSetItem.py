class Employee:
    company ="Apple"
    
    def __init__(self, name,age):
       self._data ={"Name":name, "Age":age,"Company":Employee.company} #_ indicates private data of the class
    def __getitem__(self,key):
         if key in self._data:
             return self._data[key]
         raise KeyError(f"{key} is not present in data")             
    def __setitem__(self,key,value):
        if key =="age":
            if not isinstance(value,int):
                raise TypeError(f"{value} is not an integer")
        self._data[key]=value
        
john = Employee("john",23)
print(john["Name"])#__getitem__
john["role"]="IT" #__setitem
#john["age"]="30" #__setitem =>TypeError: 30 is not an integer
john["age"]=30 
print(vars(john))

