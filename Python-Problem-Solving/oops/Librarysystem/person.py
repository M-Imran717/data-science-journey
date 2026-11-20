from date import Date
class Person:    
    def __init__(self,IdNo,Name,Address,DOB):
        self.__IdNo = IdNo
        self.__Name = Name
        self.__Address = Address
        self.__DOB = DOB
    @property
    def Get_IdNo(self):
        return self.__IdNo
    @property
    def Get_Name(self):
        return self.__Name
    @property
    def Get_Address(self):
        return self.__Address
    @property 
    def Get_DOB(self):
        return self.__DOB
    @Get_IdNo.setter
    def Get_IdNo(self,IdNo):
        self.__IdNo = IdNo
    @Get_Name.setter
    def Get_Name(self,Name):
        self.__Name = Name
    @Get_Address.setter
    def Get_Address(self,address):
        self.__Address = address
    @Get_DOB.setter
    def Get_DOB(self,dob):
        self.__DOB = dob
    def __str__(self):
        return f"IdNo : {self.Get_IdNo} | Name : {self.Get_Name} | Address : {self.Get_Address} | Date Of Birth : {self.Get_DOB}"
        
date1 = Date(2,21,2010)
person1 = Person('102',"Hamza","jarwanda kohat",date1)
print(person1)