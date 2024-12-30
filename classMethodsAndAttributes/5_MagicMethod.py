class ship:
    
    def __init__(self, crew:int, length:int)->None:
        self.crew = crew
        self.length = length
        
    def __str__(self):
        """ Called when we call print instance """
        return f"Inside __str__the crew is {self.crew} and is of length {self.length}"
    def __repr__(self):
        """ Called when we call print instance """
        return f"Inside __repr__the crew is {self.crew} and is of length {self.length}"

ship1= ship(4,5)        
print(vars(ship1))
print(dir(ship))
print(ship1.__sizeof__())
print(ship1) #it firstly check __str__ or __repr like these method from class
print(ship1.__str__())
print(ship1.__repr__())
