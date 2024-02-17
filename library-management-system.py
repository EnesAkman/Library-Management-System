class Library:
    def __init__(self):
        self.file=open("books.txt","a+")
        self.file.seek(0)
        self.books_list=[]
        # This for loop adjust book_list in order to access saved books in books.txt file
        for line in self.file:
            bookInfo=line.strip().split(",")
            if(len(bookInfo)==4):
                self.books_list.append(Book(bookInfo[0],bookInfo[1],bookInfo[2],bookInfo[3]))                         
    def __del__(self):
        if self.file:
            self.file.close()
    
    def add_book(self,book):
        self.file.write(f"{book.book_info()}\n")
        self.file.flush()
        self.books_list.append(book)      
    def list_books(self):
        self.file.seek(0)
        for book in self.file.read().splitlines():
            print(book.split(",")[0],book.split(",")[1])
    def remove_book(self,book_to_Be_removed):
        removed=False
        updated_books_list=[]
        #This loop makes a updated list without the removed book
        for book in self.books_list:
            if book.get_book_title()==book_to_Be_removed:
                print(f"The book with the title {book.get_book_title()} has been removed")
                removed=True
            else:
                updated_books_list.append(book)
        if removed:
            self.books_list=updated_books_list
            self.adjust_file()
        else:
            print(f"The book with the title {book_to_Be_removed} was not found")
    #This method adjust the file according to book_list in Library instance
    def adjust_file(self):
        self.file.seek(0)
        self.file.truncate()
        for book in self.books_list:
            self.file.write(f"{book.book_info()}\n")
        self.file.flush()
                    

#This class holds information about book instances
class Book:
    def __init__(self,book_title,book_author,release_date,number_of_pages):
        self.book_title=book_title
        self.book_author=book_author
        self.release_date=release_date
        self.number_of_pages=number_of_pages
    def get_book_title(self):
        return self.book_title
    def book_info(self):
        return f"{self.book_title},{self.book_author},{self.release_date},{self.number_of_pages}"
def main():
    is_terminated=False
    lib=Library()
    while(not is_terminated):
        print(
    """
    *** MENU***
    1) List Books
    2) Add Book
    3) Remove Book
    4) Exit
    """)
        user_selection=input("Enter a number from the menu: ")
        if user_selection=="1":
            lib.list_books()
        elif user_selection=="2":
            book_title_input=input("Write the book title: ")
            book_author_input=input("Write the book author: ")            
            book_release_date_input=get_digit_input("Write the release date of the book: ")
            book_page_number_input=get_digit_input("Write the number of pages of the book: ")
            lib.add_book(Book(book_title_input,book_author_input,book_release_date_input,book_page_number_input))
        elif user_selection=="3":
            book_remove_title_input=input("Write the book you want to remove: ")
            lib.remove_book(book_remove_title_input)
        elif user_selection=="4":
            print("You exit the program!")
            is_terminated=True
        else:
            print("Please enter appropriate number for accessing menu elements")
            continue
#This method gives the correct input depending on whether the entered input is a number or not.
def get_digit_input(prompt):
    user_input=input(prompt)
    if(user_input.isdigit()):
        return user_input
    else:
        while(not user_input.isdigit()):
            user_input=input("Please enter a valid number: ")  
        return user_input 
  
if __name__ == "__main__":
    main()
