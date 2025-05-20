from book import Book

if __name__ == '__main__':
    book_st = "La divina commedia, D. Alighieri, 99999969"
    divina_commedia = Book.from_string(book_st)
    print(divina_commedia)