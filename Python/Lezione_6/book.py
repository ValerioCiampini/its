from typing import Self

class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title= {self.title}; Author= {self.author}; Isbn= {self.isbn}"
        
    @classmethod
    def from_string(cls, repr_str) -> Self:
        sub_str = repr_str.split(",")
        return cls(sub_str[0], sub_str[1], sub_str[2])

