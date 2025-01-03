class Employee:
    def __init__(self, name, surname,age):
        self.name = name
        self.surname = surname
        self._age = age #private attribute
        #self.fullname = f"{self.name}.{self.surname}@gmail.com"

    @property
    def age(self):
        return self._age  

    @age.setter
    def age(self,new_age):
        if isinstance(new_age,int):
            if (new_age>18 and new_age<65):
                self._age = new_age
        raise ValueError (f"The age is not between 18 to 65")                

    @age.deleter
    def age(self):
        self._age =None
    @property
    def email(self):
       return f"{self.name}.{self.surname}@gmail.com"

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"


john = Employee("John", "Smith",40)
## Getter code
print(john.email)
john.surname = "Sazena"
print(john.surname)
print(john.email)

print(f"full name is {john.fullname}")
## Setter code

print(f"The john age is :{john.age}")
john._age = 30
print(f"The john new set age is :{john.age}")

## deleter code
del john.age
print(f"The john age is deleted :{john.age}")


