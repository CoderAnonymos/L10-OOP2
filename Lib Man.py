class Library:

    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library, {self.name}")

        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("We currently do not have the book, sorry!")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book] = user
            print("Lender Book database updated, book is available")

    def addBook(self, book):
        self.bookList.append(book)
        print(f"{book} has been added to the list successfully!")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned and is available!")
        else:
            print("Book is not lended from us.")

if __name__ == '__main__':
    books = Library(["Harry Potter", "A Beginner's Guide to Coding", "Dork Diaries", "Diary of a Wimpy Kid"], "Let's Upskill")
    user_name = input("Welcome to Let's Upskill library, please enter your name:")

    while True:
        print(f"\n Hello {user_name}, welcome to {books.name} library. Please choose an option: ")
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
        user_choice = input("Enter your choice to continue: ")

        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Please, enter a valid option from the choices above.")
            continue

        if user_choice == "1":
            books.displayBooks()
        elif user_choice == "2":
            book = input("Enter the name of the book you want to be lended: ")
            books.lendBook(user_name, book)
        elif user_choice == "3":
            book = input("Enter the name of the book you want to add: ")
            books.addBook(book)
        elif user_choice == "4":
            book = input("Enter the name of the book you want to return: ")
            books.returnBook(book)
        elif user_choice == "5":
            print(f"Thank you for using the library, {user_name}. Goodbye!")
            break