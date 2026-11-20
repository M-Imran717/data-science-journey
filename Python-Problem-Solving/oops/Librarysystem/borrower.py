from person import Person
from date import Date
class Borrower(Person):
    def __init__(self, IdNo, Name, Address, DOB, Status):
        super().__init__(IdNo, Name, Address, DOB)
        self.__Status = Status
    @property
    def Get_Status(self):
        return self.__Status
    @Get_Status.setter
    def Get_Status(self,status):
        self.__Status = status
    def __str__(self):
        return super().__str__() + f" | Status : {self.Get_Status}"

date1 = Date(1,1,2020)
borrower1 = Borrower('102','Hamza','Rawalpindi',date1,True)
print(borrower1)