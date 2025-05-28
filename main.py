def add_book():
    title = input('Title:\n')               #Lines 6-17 gather title, author, and ISBN for the new book
    author = input('Author(s):\n')
    goodisbn = False
    while not goodisbn:                     #While loop ensures ISBN is formatted correctly
        isbn = input('ISBN:\n')
        if len(isbn) == 10:
            isbn = f' {isbn} '              #Puts spaces on either side of a legacy ISBN.
            goodisbn = True
        elif len(isbn) == 13:
            goodisbn = True
        else:
            print('Please enter a valid ISBN.')
    with open('library.txt') as lib:
        bstr = lib.read()
        blist = bstr.split('\n')                        #For some reason the .readlines function wasn't working
        if isbn in bstr:                                #Checks whether that book is already owned
            with open('library.txt', 'w') as lib:       #If it is, the quantity is increased by 1
                for i in range(len(blist)):
                    if f'{isbn}' in blist[i]:
                        book = blist[i].split(' | ')
                        count = int(book[5]) + 1
                        book[5] = str(count)
                        blist[i] = f'{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} | {book[5]}'
                for j in range(len(blist) - 1):         #Since we use write mode here, the whole file must be reconstructed
                    lib.write(blist[j])
                    lib.write('\n')
                lib.write(blist[len(blist) - 1])
        else:
            with open('library.txt', 'a') as lib:       #Adds the book to the library if it is not already there (append mode as opposed to write mode)
                lib.write(f'\n{title} | {author} | {isbn} | Unread | - | 1')


def chg_reading_status():
    isbn = input('What is the ISBN of this book?\n')    #Since books may have the same title, we check ISBN
    if len(isbn) == 10:
        isbn = f' {isbn} '                              #Puts spaces on either side of a legacy ISBN.
    status = input("What is this book's read status?\n")
    with open('library.txt') as lib:
        bstr = lib.read()
        blist = bstr.split('\n')                        #For some reason the .readlines function wasn't working
        if isbn in bstr:                                #Checks whether that ISBN is in the library
            with open('library.txt', 'w') as lib:
                for i in range(len(blist)):
                    if f'{isbn}' in blist[i]:
                        book = blist[i].split(' | ')
                        book[3] = status
                        blist[i] = f'{book[0]} | {book[1]} | {book[2]} | {book[3]} | {book[4]} | {book[5]}'
                for j in range(len(blist) - 1):         #Since we use write mode here, the whole file must be reconstructed
                    lib.write(blist[j])
                    lib.write('\n')
                lib.write(blist[len(blist) - 1])
        else:
            print('Your book could not be found.')

# def lend_book
#
# def search_library



if __name__ == "__main__":
    # library = open("library.txt")         ###I think the file should be opened in a case by case basis, using 'w' and 'r' when necessary.
    # split_lib = library.readlines()
    finish = False
    while finish is False:
        action = input("What do you want to do today? (add, status, lend, search, done):\n")
        if action == 'add':
            add_book()
            finish = True
        elif action == 'status':
            chg_reading_status()
            finish = True
        elif action == 'lend':
            lend_book()
            finish = True
        elif action == 'search':
            search_library()
            finish = True
        elif action == 'done':
            finish = True
            exit()
        else:
            print('Please enter one of the listed options.\n\n')