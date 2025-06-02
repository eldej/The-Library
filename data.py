class Book:
    def __init__(self, title:str, author:str, isbn:str, readstate:str, lendstate:str, qty:int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.readstate = readstate
        self.lendstate = lendstate
        self.qty = qty

    def __str__(self) -> str:
        if self.lendstate != '-':
            str_lent = f"{self.lendstate} has borrowed this book."
        else:
            str_lent = 'This book is available.'

        total = (f'{self.title} by {self.author}:\n'
                 f'There are {self.qty} copies of this book.\n'
                 f'Availability: {str_lent}\n'
                 f'This book is {self.readstate}.')

        return total

    def __repr__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.readstate} | {self.lendstate} | {self.qty}"

    def __eq__(self, other) -> bool:
        if self == other:
            return True
        if self.isbn == other.isbn:
            return True
        else:
            return False
