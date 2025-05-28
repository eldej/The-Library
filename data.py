
class Book:
    def __init__(self, isbn:str, title:str, author:str, qty:int = 1):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.read = False
        self.lent = None
        self.qty = qty

    def __str__(self) -> str:
        if self.read == False:
            str_read = "You have not read it."
        else:
            str_read = "You have read it."

        if self.lent is not None:
            str_lent = f"{self.lent} has borrowed this book."
        else:
            str_lent = ""

        total = f"This book is {self.title} by {self.author}." + "\n" + str_read + "\n" + str_lent

        return total

    def __repr__(self):

    def __eq__(self, other):

