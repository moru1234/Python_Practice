#common magic methods
#__len__()
#__add__()

class plane:
    def __init__(self, seats, length):
        self.seats = seats
        self.length = length
    def __len__(self):
        return self.length


indigo =plane(130,60)    
print(len(indigo))#get length using method


class shape:
    def __init__(self,height,width):
        self.height =height
        self.width= width
        
    def __add__(self, other):
        return shape(self.height+other.height,self.width+other.width)
        
Rect = shape(10,5)        
Circle=shape(13,5)
C= Rect+Circle# sum of height, width
print(vars(C))
