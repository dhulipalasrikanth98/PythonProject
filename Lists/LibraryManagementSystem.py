class Library:
    def __init__(self,bookslist,library_name) -> None:
        self.bookslist=bookslist
        self.library_name=library_name
    def lend_book(self,book_name):
        if book_name in self.bookslist:
            print("book lend is",book_name)
            self.bookslist.remove(book_name)
        else:
            print("Book not found")
    def returnbooks(self,book_name):
        self.bookslist.append(book_name)
    def displaybook(self,s):
        print(f"there are total {len(s)} books  in this library")
        print("they are")
        for i,j in enumerate(s):
            print(i+1,j)
    def addbook(self,book_name):
        self.bookslist.append(book_name)
srikanth_library = Library(['compound effect','how to influence people',
                            'Law of attraction','Life of biographies'],"srikanth library")
srikanth_library.displaybook(srikanth_library.bookslist)
srikanth_library.addbook("python programming")

# srikanth_library.displaybook(srikanth_library.bookslist)
srikanth_library.lend_book("python programming")
srikanth_library.displaybook(srikanth_library.bookslist)