import datetime
import os

#os.getcwd()

class LMS:
    """ This class is used to keep record of the books library
    It has total 4 modules "Display Books","Issue Books","Return Book","Add Book"  """

    def __init__(self,list_of_books,library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        Id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name":"","Issue_date":"","Status":"Available"}})
            Id = Id +1

    def display_books(self):
        print("--------------------------- list of Books----------------------------------")
        print("Books ID","\t","Title")
        print("----------------------------------------------------------------------------")
        for key ,value  in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"-[",value.get("Status"),"]")

    def Issue_books(self):
        book_id = input("Enter book id please?: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if book_id in self.books_dict.keys():
            if not self.books_dict[book_id]["Status"]== "Available":
                print("This book is already issued to {self.books_dict[book_id]["lender_name"]}\
                on {self.books_dict[book_id]["Issue_date"]}")
                return self.Issue_books()

            elif self.books_dict[book_id]["Status"]== "Available":
                your_name = input("Enter your name:")
                self.books_dict[book_id]['lender_name']= your_name
                self.books_dict[book_id]["Issue_date"]= current_date
                self.books_dict[book_id]["Status"]= "Already Issued"
                print("The book has been success fully issued")

            else:
                print("Book ID not found!!!")
                return self.Issue_books()


    def add_books(self):
        new_book = input("Enter the Book's Title:")
        if new_book == "":
            return self.add_books()
        elif len(new_book) > 25:
            print("The length is too long!!! not more than 25 characters")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update(str(int(max(self.books_dict))+1):{"books_title":new_book,"lender_name":"","Issue_date":"","Status":"Aavailable"})
                print("This book '{new_book}' has been added succesfully!!!!")
    def return_book(self):
        book_id = input("Enter the book ID:")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"]== "Available":
                print("You have not issued this book. Please check again on the Book ID.")
                return self.return_book()
            elif 




l =LMS("list_of_books.txt","Dipayan's Library")
print(l.display_books())


#instantiating the class
#print(LMS("list_of_books.txt","Dipayan's Library"))
