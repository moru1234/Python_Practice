# Class Method Practise

# Create a Employee class
# Class has attributes as company, bonus_amount, pay_risepercent
# instance attributes, name pay, role
# class method - change is bonus ammount and pay risepercent
#instance method - show pay with bonus and increase annual pay.

class Emp:
    companyName = "Bosh"
    companyBonus = 10000
    companyPayRise =3

    def __init__(self,name, pay, role):
        self.name= name
        self.pay =pay
        self.role = role

    def showPayWithBonus(self):
        return f"The payment of bonus is {self.companyBonus} and increase in payment is {self.companyPayRise}"        

    @classmethod
    def changeCompanyDetails(cls,bonus, payrise):
        cls.companyBonus = bonus
        cls.companyPayRise = payrise


E1= Emp("Moru",100,"Eng")
print(E1.showPayWithBonus())
E1.changeCompanyDetails(1000,4)
print(E1.showPayWithBonus())

