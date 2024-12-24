class Motorbike:
    wheels =2
    def __init__(self,colour,price):
        self.wheels =10
        self.colour = colour
        self.price = price


bikea=Motorbike("Red",10000)
bikeb = Motorbike("White",11000)
print("the bike coulour is ", bikea.colour,bikea.price,bikea.wheels) #in python print statement it need to be separated with ,

