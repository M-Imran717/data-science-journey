from date import Date
from date import date1
class Loan:
    def __init__(self, BorrowedDate,  DueDate,  ReturnedDate,Fine):
        self.__BorrowedDate = BorrowedDate
        self.__DueDate = DueDate
        self.__ReturnedDate = ReturnedDate
        self.__Fine = Fine

    @property
    def Get_BorrowedDate(self):
        return self.__BorrowedDate
    @property
    def Get_DueDate(self):
        return self.__DueDate
    @property
    def Get_ReturnedDate(self):
        return self.__ReturnedDate
    @property
    def Get_Fine(self):
        return self.__Fine

    @Get_BorrowedDate.setter
    def Get_BorrowedDate(self, borrowdate):
         self.__BorrowedDate = borrowdate
    @Get_DueDate.setter
    def Get_DueDate(self, duedate):
         self.__DueDate = duedate
    @Get_ReturnedDate.setter
    def Get_ReturnedDate(self, returndate):
         self.__ReturnedDate = returndate
    @Get_Fine.setter
    def Get_Fine(self, fine):
         self.__Fine = fine

    @property
    def Cal_Total_Fine(self):
        isLate = False
        if(
           ( self.Get_ReturnedDate.Get_Year > self.Get_DueDate.Get_Year) or\
           (self.Get_ReturnedDate.Get_Year == self.Get_DueDate.Get_Year and self.Get_ReturnedDate.Get_Month > self.Get_DueDate.Get_Month) or\
           (self.Get_ReturnedDate.Get_Year == self.Get_DueDate.Get_Year and self.Get_ReturnedDate.Get_Month == self.Get_DueDate.Get_Month and self.Get_ReturnedDate.Get_Day > self.Get_DueDate.Get_Day)
        ):isLate = True

        if(isLate == True):
            yeardif = self.Get_ReturnedDate.Get_Year - self.Get_DueDate.Get_Year
            monthdif = self.Get_ReturnedDate.Get_Month - self.Get_DueDate.Get_Month
            daydif = self.Get_ReturnedDate.Get_Day - self.Get_DueDate.Get_Day
            late = yeardif * 365 + monthdif * 30 + daydif
            total_fine = late * self.Get_Fine
            return total_fine
        else:
            return 0
    def __str__(self):
        return(
            f"Loan Details : \n"
            f"BorrowedDate : {self.Get_BorrowedDate} | DueDate : {self.Get_DueDate} | ReturnedDate : {self.Get_ReturnedDate} | Per day Fine : {self.Get_Fine} | Total Fine : {self.Cal_Total_Fine}"
        ) 

date2 = Date(20,1,2026)
date3 = Date(1,2,2026)
loan1 = Loan(date1,date2,date3,50)
print(loan1)