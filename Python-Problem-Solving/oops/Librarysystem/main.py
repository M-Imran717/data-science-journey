from book import Book
from loan import Loan
from librarian import Librarian
from date import Date
from borrower import Borrower

#import there objects 
from book import book1
from loan import loan1
from librarian import librarian1
from date import date1
from borrower import borrower1

class Library:
    def __init__(self):
        self.__books = []
        self.__librarian = []
        self.__borrower = []
  
    def Add_Book(self,book):
        self.__books.append(book)
  
    def Add_Librarian(self,librarian):
        self.__librarian.append(librarian)
    
    def Add_Borrower(self,borrower):
        self.__borrower.append(borrower)

    def __str__(self):
        books = "\n".join([str(c) for c in self.__borrower])
        librarians = "\n".join([str(c) for c in self.__librarian])
        borrowers = "\n".join([str(c) for c in self.__borrower])
        return (
            f"Books : \n"
            f"{books} \n"
            f"Librarians : \n"
            f"{librarians} \n"
            f"Borrowers : \n"
            f"{borrowers}"
        )

library1 = Library()
library1.Add_Book(book1)
library1.Add_Librarian(librarian1)
library1.Add_Borrower(borrower1)
print(library1) 