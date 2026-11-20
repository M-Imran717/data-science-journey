class Book:
    def __init__(self,BookNo, Title, MainAuthor, Category, TotalBooks):
        self.__BookNo = BookNo
        self.__Title = Title
        self.__MainAuthor = MainAuthor
        self.__Category = Category
        self.__TotalBooks = TotalBooks
    @property
    def Get_BookNo(self):
        return self.__BookNo
    @property
    def Get_Title(self):
        return self.__Title
    @property 
    def Get_MainAuthor(self):
        return self.__MainAuthor
    @property
    def Get_Category(self):
        return self.__Category
    @property
    def Get_TotalBooks(self):
        return self.__TotalBooks
        
    @Get_BookNo.setter
    def Get_BookNo(self,BookNo):
         self.__BookNo = BookNo
    @Get_Title.setter
    def Get_Title(self, title):
         self.__Title = title
    @Get_MainAuthor.setter 
    def Get_MainAuthor(self, author):
         self.__MainAuthor = author
    @Get_Category.setter
    def Get_Category(self, category):
         self.__Category = category
    @Get_TotalBooks.setter
    def Get_TotalBooks(self, totalbooks):
         self.__TotalBooks = totalbooks

    def __str__(self):
        return(f"Book Detail : \n"
               f"BookNo : {self.Get_BookNo} | Title : {self.Get_Title} | Main Author : {self.Get_MainAuthor} | Category : {self.Get_Category} | TotalBooks : {self.Get_TotalBooks}"
               )


book1 = Book("201","Time Is Money","Jorge Peter","Book",20)
print(book1)