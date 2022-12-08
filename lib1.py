# the schema contains 
#status check checks my book _id status first then returns it
# issue book
#schema book_id =  [book_name ,user_name ,date ,avaliabklity,userid]


class lMS:
        def __init__(self):
                self.book_map = {}
       
    
        def status_check(self ,book_id):
                return self.book_map[book_id][3] 
                        

        def issue_book(self, book_id, user_name,user_id):
                if self.status_check(book_id) is True:
                        self.book_map[book_id][1] = user_name
                        self.book_map[book_id][4] = user_id
                        self.book_map[book_id][3] = False
                        return True
                else:
                        return False
                        

        def return_book(self,book_id ,user_id):
                if self.status_check(self,book_id) is False and self.book_map[book_id][4] == user_id:
                        self.book_map[book_id][4] = None
                        self.book_map[book_id][3] = True
                        return True
                else:
                        return False

        def add_book(self,book_id, book_name):
                if book_id  in self.book_map:
                        return False
                else:
                        self.book_map[book_id]=[book_name,None,None,True,None]
                        return True


        def display_books(self):
                print("--------------------------------------")
                print (self.book_map)
                print("---------------------------------------")
                



def initialize():
        l = lMS()
        temp = {}

        #reading data into temp
        temp["book_id1"] = ["Java", None, "12/1/2022", True, None]
        temp["book_id2"] = ["Python", None, "13/2/2021", True ,None]
        temp["book_id3"] = ["C fundamentals", None, "5/6/2021", None]
        temp["book_id4"] = ["C++ fundamentals", None, "5/6/2020", None]
        temp["book_id5"] = ["Visualization", None, "8/8/2021", None]


        l.book_map = temp
        return l

def run(l):
        
        while(True):
                print("Welcome to the  library. Enter Your choice to continue")
                print("1. Display Book list")
                print("2. Issue a Book ")
                print("3. Add a Book ")
                print("4. Return a Book ")
                user_choice  = int(input())

                if user_choice == 1:
                        l.display_books()

                elif user_choice == 2:
                        book_id = input("Enter the id of the book you want to lend:")
                        user_name = input("Enter your name:")
                        user_id = input("Enter your registered id")
                        status = l.issue_book(book_id,user_name,user_id)
                        if status is True:
                                print("Book issued ")
                        else:
                                print("The book is not available!")

                elif user_choice == 3:
                        book_name = input("Enter the name of the book you want to add")

                        status = l.add_book(book_name)
                        if status is True:
                                print(" Book added succesfully!")
                        else:
                                print("Sorry cant be done")

                elif user_choice == 4:
                        book_id = input("Enter the name of the book you want to return")
                        user_id = input("Please enter your registered id")
                        status =l.return_book(book_id,user_id)
                        if status is True:
                                print("Your return is successful")
                        else:
                                print("OOPS and error occured")

                else:
                        print("Enter the correct choice")
def cleanup():
        pass

def main():
        l = initialize()
        run(l)
        cleanup()
        


if __name__ == "__main__" :
       main()







    
    
     

   
  



    
