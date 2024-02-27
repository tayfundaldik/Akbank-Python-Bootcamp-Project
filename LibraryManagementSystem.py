#This code written by Erdogan Tayfun Daldik.
import datetime  
class Library:
      
    def __init__(self):
        self.library = open("books.txt","a+")
        
    
    #For listing the books
    def ListBooks(self):
        bookList = []
        self.library.seek(0)
        readLib = self.library.read()
        splitLib = readLib.splitlines()
        for i in range(len(splitLib)):
           booksLib = splitLib[i]
           splittedLib = booksLib.split(",")
           splittedLib = [element.strip().title() for element in splittedLib]
           bookList.append(splittedLib)
           print(f"Book : {splittedLib[0]}, Author: {splittedLib[1]}\n")       
        
    #For adding books
    def AddBooks(self):
        #Used for current year for release_year limit
        today = datetime.date.today()
        year = today.year 
        
        while True:
            book_name = input("What is the book's name?\n").strip().title()
            #If user input is empty
            if not book_name:
                print("Book name cannot be empty. Please try with a correct name.")    
                continue
            #This limit is based by the longest book name of the world
            elif len(book_name) >27978:
                print("Given book name is too long. Please try again.")
                continue
            #Correction for user input   
            book_author = input(f"What is the name of {book_name}'s author?\n").strip().title()
            if not book_author:
                print("Author name cannot be empty. Please try again")
                continue
            #Checking for user input that contains only special characters
            elif not any(char.isalpha() for char in book_author):
                print("Author name is invalid. Please try again.")
                continue
            #Checking for user input if it is integer
            elif any(char.isdigit() for char in book_author):
                print("Author name cannot be digits. Please enter a valid name.")
                continue
            #This limit based by longest name of the world
            elif len(book_author) > 747:
                print("Given author's name is too long. Please try again.")
                continue
                 
            release_year = input(f"What is the {book_name}'s release year?\n")
            if not release_year:
                print("Release year cannot be empty. Please try again.")
                continue
            try:
                release_year1 = int(release_year)
                if release_year1 < 0 or release_year1 > year:
                    print("Given book's release year is invalid. Please try again.")
                    continue
            except:
                print("Please enter a valid year.")
                continue    
            number_pages = input(f"What is the {book_name}'s number of pages?\n")
            if not number_pages:
                print("Number of pages cannot be empty. Please try again.")
                continue
            try:
                number_pages1 = int(number_pages)
                #This limit based by most paged book of the world
                if number_pages1 < 0 or number_pages1 > 21450:
                    print("Given number is invalid. Please try again.")
                    continue
            except:
                print("Please enter a valid number.")
                continue 
            #Correcting all the inputs for books.txt       
            book = f"{book_name},{book_author},{release_year},{number_pages}\n"
            self.library.write(book)
            print("Your book is added to library successfully.")
            break
        
        
    def RemoveBooks(self):
        while True:    
            #For the correction of input
            remove = input("Which book do you want to remove?\n").strip().title()
            if not remove:
                print("Please enter a valid book.")
                continue
                
            bookList = []
            self.library.seek(0)
            readLib = self.library.readlines()
            book_found = False
            
            for book in readLib:
                # Skip empty lines
                if not book.strip():
                    continue
                
                book_details = book.strip().split(",")
                if book_details[0].strip().title() == remove and not book_found:
                    book_found = True
                    # Skip the first occurrence of the book
                    continue  
                bookList.append(book)
            
            if not book_found:
                print("Book not found.")
                continue 
            
            #Read the file from the start because code is in "a+" mode   
            self.library.seek(0)
            self.library.truncate()
            
            for book in bookList:
                self.library.write(book)
                    
            print(f"The book is successfully removed!")
            break
    
    def __del__(self):
        self.library.close()


lib = Library()
#For menu
def Menu (lib):
    isOkay = True
    while isOkay:
        choice = input("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\nq) Exit\nEnter your choice (1-3 or q) : ")
        if choice == "1":
            lib.ListBooks()
        elif choice == "2":
            lib.AddBooks()
        elif choice == "3":
            lib.RemoveBooks()        
        elif choice == "q":
            print("!!!!!Have a great day!!!!!")
            isOkay = False
        else :
            print("You typed a wrong character.\nPlease try again.")
Menu(lib)
