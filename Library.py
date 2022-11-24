# create a library class
#display book
#lend book -(who owns the book if not present)
#add book
#return book


#dipayans Library = library(list of books,library_name)

#dictionary (books :name of person)

#creating a mnain function











class library:
    def __init__(self,list,name):

        self.booklist = list
        self.name = name
        self.lendDict = {}


    def displaybooks(self):
        print(f"We have the following books in our library:{self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("The Database has been updated. You can take your book now")
        else:
            print(f"This book is already being borrowed by {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("The Boom has been added to the list")
    
    def returnbook(self,book):
        self.lenDict.pop(book)

    
if __name__ == '__main__':
    first1 = library(['Basic Python','Data Analytics','Tableau','Java','C++',],"Dipayan")

    while(True):
        print(f"Welcome to the {first1.name} library. Enter Your choice to continue")
        print("1. Display Book list")
        print("2. Lend a Book ")
        print("3. Add a Book ")
        print("4. Return a Book ")

        user_choice  = int(input())

        if user_choice == 1:
            first1.displaybooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            first1.lendbook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")

            first1.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return")
            first1.returnbook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!= "c" and user_choice2!="q"):
            user_choice2 = input()

            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
        
        
