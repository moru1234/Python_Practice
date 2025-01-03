class Climber:
    default_grade ="v1"
    def __init__(self, fname, lname, maxgrade):
        self.fname = fname
        self.lname = lname
        self._maxgrade = maxgrade

#define a getter called for maxgrade 
    @property
    def maxgrade(self):
        return self._maxgrade
#define a setter - parse the input starts with v, and is second char is digit ? (assume input is v9) 
    @maxgrade.setter
    def maxgrade(self, grade):
        if grade.startswith("v") and grade[-1].isdigit():
            self._maxgrade = grade

#define a deleter - set the maxgrade back to default value - default_grade            
    @maxgrade.deleter
    def maxgrade(self):
        self._maxgrade = Climber.default_grade

adam = Climber("Adam", "Saxena", "v9")  
print(adam.maxgrade)
adam.maxgrade="v8"
print(adam.maxgrade)

del adam.maxgrade
print(adam.maxgrade)