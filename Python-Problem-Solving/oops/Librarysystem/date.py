class Date:
    def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year 
        
    @property
    def Get_Day(self):
        return self.__day
    
    @property
    def Get_Month(self):
        return self.__month
    
    @property
    def Get_Year(self):
        return self.__year
    
    @Get_Day.setter
    def Get_Day(self,day):
        self.__day = day

    @Get_Month.setter
    def Get_Month(self,month):
        self.__month = month

    @Get_Year.setter
    def Get_Year(self,year):
        self.__year = year
    def __str__(self):
        return f"{self.Get_Day}/{self.Get_Month}/{self.Get_Year}"

date1 = Date(1,1,2026)
print(date1)
        