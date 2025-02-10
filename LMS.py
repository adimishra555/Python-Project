class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn}) - {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id})"


class Student(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"You did not borrow '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has no borrowed books.")


class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}' to the library.")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"Librarian {self.name} removed '{book.title}' from the library.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"Book '{book.title}' not found in the library.")

    def list_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                print(book)
        else:
            print("The library has no books.")

if __name__ == "__main__":
    library = Library()
    book1 = Book("100 Days of Code", "Angela Yahu", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")
    book3 = Book("Master your python ", "Harper Lee", "9780061120084")

  
    librarian = Librarian("Alice", "L001")
    librarian.add_book(library, book1)
    librarian.add_book(library, book2)
    librarian.add_book(library, book3)
  
    library.list_books()

    student = Student("John", "S001")
    student.borrow_book(book1)
    student.borrow_book(book2)

    student.list_borrowed_books()

    student.return_book(book1)

    student.list_borrowed_books()
    librarian.remove_book(library, book3)
    library.list_books()
