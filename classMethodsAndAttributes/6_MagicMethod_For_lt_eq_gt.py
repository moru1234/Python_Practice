class House:
    def __init__(self,bedrooms):
        self.bedrooms =bedrooms
    def __eq__(self,other) ->bool:
        return (self.bedrooms ==other.bedrooms)
    
    def __gt__(self,other) ->bool:
        return (self.bedrooms>other.bedrooms)
        
    def __lt__(self,other) ->bool:
        try:
            return (self.bedrooms<other.bedrooms)
        except AttributeError:
            raise ValueError("This resulted into value error!")
        
        


Ram_house =House(2)        
Sham_house = House(4)
print(Ram_house == Sham_house) #check for equality
print(Ram_house> Sham_house)
print(Ram_house< Sham_house)
print(Ram_house<49)#AttributeError: 'int' object has no attribute 'bedrooms'
    
        
