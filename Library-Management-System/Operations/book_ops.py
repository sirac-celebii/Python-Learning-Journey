from Database import BookDatabase

class BookOperations():
    def __init__(self):
        self.book_db = BookDatabase()

    def _get_book_id(self):
        id = self.book_db.get_book_id()
        return id

    def _get_all_books(self):
        books = self.book_db.get_all_books()

        if books:
            return books
        else:
            raise ValueError("No books found in Database !")

    def add_book(self, book):
        self.book_db.add_book(book)

    def delete_book(self, book_id):
        self.book_db.delete_book(book_id)

    def search_book(self, book_name):
        books = self.book_db.search_book(book_name)
        
        if books:
            return books
        else:
            raise ValueError ("Book not found !")
        
    def view_all_books(self):
        book_list = self._get_all_books()
        
        formatted_list = self.format_book_list(book_list)

        self.print_books(formatted_list)
            
    
    # def borrow_book(self, book_id, user_id):
    #     self.book_db.borrow_book()

    # def return_book(self, book_name, user_id):
    #     pass
    
    def format_book_list(self, book_list):
        formatted_list = []

        for book in book_list:
            formatted_list.append(f"Book Id : {book[0]} | Book Name : {book[1]} | Author : {book[2]}")

        return formatted_list
       
    def print_books(self, books):
        for book in books:
            print(book)

    def close_db(self):
        self.book_db.close()