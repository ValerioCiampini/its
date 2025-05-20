from book import Book
from typing import Self

class Member:
    def __init__(self, nome:str, member_id:str):
        self.nome = nome
        self.member_id = member_id
        self._borrow_book:list[Book] = []

    def borrow_book(self, book:Book):
        self._borrow_book.append(book)

    def return_book(self, book:Book):
        if book in self._borrow_book:
            self._borrow_book.remove(book)

    def __str__(self):
        return f"Name = {self.nome}; Member id = {self.member_id}"
    
    @classmethod
    def from_string(cls, in_str) -> Self:
        subs = in_str.split(",")
        return cls(subs[0], subs[1])