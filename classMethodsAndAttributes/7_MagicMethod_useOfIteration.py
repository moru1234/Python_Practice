#use __iter__() and __next__() methods to iterate over the list

class Store:
    def __init__(self, items:list):
        self.items = items
        self.counter =0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if(self.counter >len(self.items)-1):
            raise StopIteration
        
        current=self.counter
        self.counter+=1
        return self.items[current]

            
            
        
        
print(dir(Store))        
Reliance = Store(["Book","Pen","Chips"])#this iteration is done withhaving iter and next defined methods
for i in Reliance:
    print(i)

print("_______________")
for i in Reliance.items:
    print(i)
    
    
        
