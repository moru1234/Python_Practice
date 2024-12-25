class Laptop:
    brand = "Dell"
    def __init__(self,Ram:int,processor:str)->None:
        self.Ram=4
        self.processor ="Snapdraggon"

    @classmethod
    def updateBrandofLaptop(cls,name)->None:
        if (name.isalpha() and (len(name)<10)): #isalpha is a function in for string in python to check all are alphabets
            cls.brand =name
        else:
            raise (f"The laptop brand has length of character is more than 10")                    



basicLaptop = Laptop(5,"Quantum")
basicLaptop.updateBrandofLaptop("Mores")

print(f"The laptop of brand {basicLaptop.brand} has ram {basicLaptop.Ram} and processor is {basicLaptop.processor}")