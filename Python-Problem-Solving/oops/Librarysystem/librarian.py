from person import Person
from date import Date
class Librarian(Person):
    def __init__(self, IdNo, Name, Address, DOB, Sal, Email):
        super().__init__(IdNo, Name, Address, DOB)
        self.__Sal = Sal
        self.__Email = Email
    @property
    def Get_Sal(self):
        return self.__Sal
    @property
    def Get_Email(self):
        return self.__Email
    @Get_Sal.setter
    def Get_Sal(self,sal):
        self.__Sal = sal
    @Get_Email.setter
    def Get_Email(self,email):
        self.__Email = email
    def __str__(self):
        return super().__str__() + f" | Salary : {self.Get_Sal} | Email : {self.Get_Email}"


date1 = Date(1,1,2023)
librarian1 = Librarian('102','Hamza','Rawalpindi',date1,50000,'Hamza123@gmail.com')
print(librarian1)