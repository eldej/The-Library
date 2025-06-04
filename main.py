from data import Book

# Add a new book entry to the list of books or update the qty of an existing one.
# No inputs; user inputs all book data
# No outputs; function modifies book list
def add_book():
    title = input('Title:\n')               # Lines 6-17 gather title, author, and ISBN for the new book
    author = input('Author(s):\n')
    goodisbn = False
    while not goodisbn:                     # While loop ensures ISBN is formatted correctly
        isbn = input('ISBN:\n')
        if len(isbn) == 10:
            isbn = f' {isbn} '              # Puts spaces on either side of a legacy ISBN.
            goodisbn = True
        elif len(isbn) == 13 and isbn.isdigit():
            isbn = f' {isbn} '              # Puts spaces on either side of a modern ISBN.
            goodisbn = True
        else:
            print('Please enter a valid ISBN.')

    for i in books:
        if f' {i.isbn} ' == isbn:           # Checks whether that book is already owned
            i.qty += 1
            print('Book added!\n')
            return
    books.append(Book(title, author, isbn.strip(' '), 'Unread', '-', 1))   # Adds the book to the library if it is not already there
    print('Book added!\n')
    return

# Modify a book's reading status in the library.
# No inputs; user inputs isbn and new status
# No outputs; function modifies library file
def chg_reading_status():
    isbn_in = input('What is the ISBN of this book?\n')
    isbn = f" {isbn_in} "
    for i in books:
        if f' {i.isbn} ' == isbn:
            i.readstate = input("What is this book's read status?\n")
            print('Status Changed!\n')
            return
    print('Your book could not be found.\n')
    return

# Modify a book's lending status in the library.
# No inputs; user inputs ISBN and lendee
# No outputs; function modifies library file
def lend_book():
    isbn_in = input('What is the ISBN of this book?\n')
    isbn = f" {isbn_in} "
    for i in books:
        if f' {i.isbn} ' == isbn:
            i.lendstate = input("Who are you lending this to?\n")
            print('Status Changed!\n')
            return
    print('Your book could not be found.\n')
    return

# Searches library by ISBN.
# No inputs; ISBN inputted by user
# No outputs; function modifies library file
def search_library():
    isbn_in = input('What is the ISBN of this book?\n')
    isbn = f" {isbn_in} "
    for i in books:
        if f' {i.isbn} ' == isbn:
            print("\nYour book:")
            print(f'{i.__str__()}\n')
            return
    print('Your book could not be found.\n')

# Driver file. Launches library and iterates until user is done.
# No inputs
# No outputs; only library.txt file is modified.
if __name__ == "__main__":
    books = []
    workingfile = input('file:\n')
    with open(workingfile) as lib:
        for line in lib:                    #Creates a list[Book] with attributes specified in the working file
            atts = line.split(' | ')
            books.append(Book(atts[0], atts[1], atts[2], atts[3], atts[4], int(atts[5])))

    while True:
        action = input("What do you want to do today? (add, status, lend, search, done):\n").strip()
        if action == 'add':
            add_book()
        elif action == 'status':
            chg_reading_status()
        elif action == 'lend':
            lend_book()
        elif action == 'search':
            search_library()
        elif action == 'done':
            with open(workingfile, 'w') as lib:
                for i in books:
                    lib.write(f'{i.__repr__()}\n')
            exit()
        else:
            print('Please enter one of the listed options.\n\n')