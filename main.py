# Add a new book entry to the library.txt file or update the qty of an existing one.
# No inputs; user inputs all book data
# No outputs; function modifies library file
def add_book() -> None:
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

    with open('library.txt') as lib:
        blist = lib.readlines()
        bstr = ''.join(blist)

        if isbn in bstr:                                # Checks whether that book is already owned
            for i in range(len(blist)):
                if isbn in blist[i]:
                    book = blist[i].split(' | ')
                    count = int(book[5]) + 1
                    book[5] = str(count)
                    blist[i] = f'{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} | {book[5]}'

            with open('library.txt', 'w') as lib:
                lib.writelines(blist)

        else:
            with open('library.txt', 'a') as lib:       # Adds the book to the library if it is not already there (append mode as opposed to write mode)
                lib.write(f'\n{title} | {author} |{isbn}| Unread | - | 1')

# Modify a book's reading status in the library.
# No inputs; user inputs isbn and new status
# No outputs; function modifies library file
def chg_reading_status():
    isbn = ' ' + input('What is the ISBN of this book?\n') + ' '
    status = input("What is this book's read status?\n")
    with open('library.txt') as lib:
        blist = lib.readlines()
        bstr = ''.join(blist)
        if isbn in bstr:                                # Checks whether that ISBN is in the library
            for i in range(len(blist)):
                if f'{isbn}' in blist[i]:
                    book = blist[i].split(' | ')
                    book[3] = status
                    blist[i] = f'{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} | {book[5]}'

            with open('library.txt', 'w') as lib:       # Reconstruct whole file
                lib.writelines(blist)

        else:
            print('Your book could not be found.')

# Modify a book's lending status in the library.
# No inputs; user inputs ISBN and lendee
# No outputs; function modifies library file
def lend_book():
    isbn = ' ' + input('What is the ISBN of this book?\n') + ' '
    status = input("Who are you lending this to? \n")
    with open('library.txt') as lib:
        blist = lib.readlines()
        bstr = ''.join(blist)
        if isbn in bstr:                                # Checks whether that ISBN is in the library
            for i in range(len(blist)):
                if f'{isbn}' in blist[i]:
                    book = blist[i].split(' | ')
                    book[4] = status
                    blist[i] = f'{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} | {book[5]}'

            with open('library.txt', 'w') as lib:  # Reconstruct whole file
                lib.writelines(blist)

        else:
            print('Your book could not be found.')

# Searches library by ISBN.
# No inputs; ISBN inputted by user
# No outputs; function modifies library file
def search_library():
    goodisbn = False
    while not goodisbn:  # While loop ensures ISBN is formatted correctly
        isbn = input('ISBN:\n')
        if len(isbn) == 10 or len(isbn) == 13 and isbn.isdigit():
            goodisbn = True
        else:
            print('Please enter a valid ISBN.')

    with open('library.txt') as lib:
        blist = lib.readlines()
        for line in blist:
            terms = line.split(' | ')
            if terms[2] == isbn: # Check each line for a match
                print(f"Your Book \n Title: {terms[0]} \n Author: {terms[1]} \n Reading Status: {terms[3]} \n Lent to: {terms[4]} \n Copies: {terms[5]}")
                return

    print('Your book could not be found.')

# Driver file. Launches library and iterates until user is done.
# No inputs
# No outputs; only library.txt file is modified.
if __name__ == "__main__":
    # library = open("library.txt")         ### I think the file should be opened in a case by case basis, using 'w' and 'r' when necessary.
    # split_lib = library.readlines()
    finish = False
    while finish is False:
        action = input("What do you want to do today? (add, status, lend, search, done):\n")
        if action == 'add':
            add_book()
        elif action == 'status':
            chg_reading_status()
        elif action == 'lend':
            lend_book()
        elif action == 'search':
            search_library()
        elif action == 'done':
            finish = True
            exit()
        else:
            print('Please enter one of the listed options.\n\n')