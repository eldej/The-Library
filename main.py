

def add_book

def chg_reading_status

def lend_book

def search_library



if __name__ == "__main__":
    library = open("library.txt")
    split_lib = library.readlines()
    finish = False
    while finish is False:
        action = input("What do you want to do today? (add, read, lend, search, done): ")
        if action

