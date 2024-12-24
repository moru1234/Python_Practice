# Class Method and instance Method

class Example:
    category ="Demo"

    def __init__(self,name):
        self.name = name

    def displayname(self): # Instance method
        return f"for this instance the name is {self.name}"
    
    @classmethod  # Class method
    def updateCategory(cls,category):
        cls.category= category
        return f"The updated category is {cls.category}"
    
    def displayCategory(self):
        return f"The category is {self.category}"


obj1=Example("Science") # Creating an instance of the class
print(obj1.displayname()) # Calling the instance method
print(obj1.updateCategory("Update")) # Calling the class method

obj2=Example("Science") # Creating an instance of the class
print(obj2.displayCategory())  #since category was updated by class method so we are seeing this Update as category.
