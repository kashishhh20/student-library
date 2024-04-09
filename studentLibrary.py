class Library:

    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t* " +book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"\nYou have been issued {bookName}.Please keep it safe and return it within 30 days.\n")
            self.books.remove(bookName)
            return True
        else:
            print("\nSorry, This book is either not available or has already been issued to someone else. Please wait until the book is available.\n")
            return False

    def returnBook (self, bookName):
        self.books.append(bookName)
        print("\nThanks for returning this book! Hope you have enjoyed reading it. Have a great day ahead\n")               


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    student = Student()
    centralLibrary = Library(["Algorithms", "Django", "c++", "Clrs", "Python Notes", "C"])

    while (True):
        welcomeMsg = '''====Welcome to Central Library====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
    
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()

        elif a ==2:
            centralLibrary.borrowBook(student.requestBook())

        elif a ==3:
            centralLibrary.returnBook(student.returnBook())

        elif a ==4:
            print("\nThanks for choosing this library\n")
            exit()

        else:
            print("Invalid choice")