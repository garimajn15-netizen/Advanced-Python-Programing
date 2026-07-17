class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"  '{self.title}' by {self.author} - {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def display(self):
        books = ", ".join(b.title for b in self.borrowed) if self.borrowed else "None"
        print(f"  {self.name} - Borrowed: {books}")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added to library.")

    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print(f"Patron '{name}' registered.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron
        return None

    def borrow_book(self, patron_name, title):
        patron = self.find_patron(patron_name)
        book = self.find_book(title)

        if not patron:
            print("Patron not found.")
            return
        if not book:
            print("Book not found.")
            return

        if book.available:
            book.available = False
            patron.borrowed.append(book)
            print(f"'{title}' issued to {patron_name}.")
        else:
            print("Book not Available")

    def return_book(self, patron_name, title):
        patron = self.find_patron(patron_name)
        book = self.find_book(title)

        if not patron:
            print("Patron not found.")
            return
        if not book:
            print("Book not found.")
            return

        if book in patron.borrowed:
            patron.borrowed.remove(book)
            book.available = True
            print(f"'{title}' returned by {patron_name}.")
        else:
            print("Book not borrowed by this patron")

    def show_books(self):
        if not self.books:
            print("No books in library.")
            return
        print("Books in Library:")
        for book in self.books:
            book.display()

    def show_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return
        print("Registered Patrons:")
        for patron in self.patrons:
            patron.display()


def main():
    # START
    library = Library()  # Create Library Object

    while True:
        # User Selects Operation
        print("\n--- User Selects Operation ---")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. View Books & Patrons")
        print("4. Borrow Book")
        print("5. Return Book")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter patron name: ").strip()
            library.register_patron(name)

        elif choice == "3":
            library.show_books()
            library.show_patrons()

        elif choice == "4":
            patron_name = input("Enter patron name: ").strip()
            title = input("Enter book title: ").strip()
            library.borrow_book(patron_name, title)

        elif choice == "5":
            patron_name = input("Enter patron name: ").strip()
            title = input("Enter book title: ").strip()
            library.return_book(patron_name, title)

        else:
            print("Invalid choice, try again.")
            continue

        # Continue?
        cont = input("\nContinue? (Yes/No): ").strip().lower()
        if cont != "yes" and cont != "y":
            break  # END

    print("\nEND")


if __name__ == "__main__":
    main()
