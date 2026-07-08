from Operations import BookOperations, UserOperations
from Database import BookDatabase, UserDatabase
from Models import User, Book

from Utils.helper import clear

class Main():
    def __init__(self):
        self.book_operations = BookOperations()
        self.user_operations = UserOperations()

    def start(self):
        self.main_menu()

    def main_menu(self):
        menu = [
            "Book operations menu",
            "User operations menu",
            "Exit"
        ]

        while True:
            clear()
            choice = self.get_choice(menu)
            self.forwarding(choice, role = "main")

    def book_ops_menu(self):
        menu = [
            "Add book",
            "Delete book",
            "Search book",
            "View all books",
            "Return to Main Menu"
        ]

        while True:
            clear()
            choice = self.get_choice(menu)
            if choice == 5:
                break
            self.forwarding(choice, role= "book_ops")
            


    def user_ops_menu(self):
        menu = [
            "Add user",
            "Delete user",
            "Search user",
            "View all users",
            "Return to Main Menu"
        ]

        while True:
            clear()
            choice = self.get_choice(menu)
            if choice == 5:
                break
            self.forwarding(choice, role= "user_ops")
            
    
    def continue_to_menu(self):
            choice = input("To keep adding, press Enter.\n" + 
                            "To return to the menu, enter any character.\n" +
                            "-> ")
            
            return choice.strip() == ""

    def get_choice(self, menu):
        while True:
            for index, row in enumerate(menu):
                print(f"{index + 1}-) {row}")
            try:
                choice = int(input("Enter choice -> "))
                if choice <= 0 or choice > len(menu):
                    clear()
                    print("Invalid choice, please try again.\n")
                    continue
                break
            except ValueError:
                clear()
                print("Invalid choice, please try again.\n")
                continue
        clear()
        return choice   

    def forwarding(self, choice, role):
        match(choice, role):
        #=============MAIN=============================================
            case (1, "main"): # Bokk Opertaions menu
                self.book_ops_menu()

            case (2, "main"): # User Operaions menu
                self.user_ops_menu()

            case (3, "main"): # Ends the program
                self.user_operations.close_db()
                self.book_operations.close_db()
                exit()
        #============Book Operations==================================
            case (1, "book_ops"): # Add book
                while True:
                    try:
                        new_book = Book(
                                name = input("Book name -> "),
                                author= input("Author -> ")
                            )
    
                        self.book_operations.add_book(new_book)
                    except ValueError as e:
                        print(e)
                        input("Press Enter to continue...")
                        break
                    
                    print("Book added successfully !")
                    if not self.continue_to_menu():
                        break

                    clear()

            case (2, "book_ops"): # Delete book
                while True:
                    book_name = input("Book name -> ")

                    try:
                        books = self.book_operations.search_book(book_name)
                    except ValueError as e:
                        print(e)
                        input("Press Enter to continue...")
                        break
                    
                    book_list = self.book_operations.format_book_list(books)

                    choice = self.get_choice(book_list)
                    
                    self.book_operations.delete_book(books[choice -1][0])
                    print("Book deleted successfully !")

                    if not self.continue_to_menu():
                        break

                    clear()

            case (3, "book_ops"): # Search book
                book_name = input("Book name -> ")

                try:
                    book_list = self.book_operations.search_book(book_name)
                except ValueError as e:
                    print(e)
                    
                    input("Press Enter to continue...")
                    return
                
                formatted_list = self.book_operations.format_book_list(book_list)
                self.book_operations.print_books(formatted_list)

                input("Press Enter to continue...")

            case (4, "book_ops"): # View all books
                self.book_operations.view_all_books()

                input("Press Enter to continue...")

            case (5, "book_ops"): #Return to Main menu
                return 
        
        #=============User Operations=================================
            case (1, "user_ops"): # Add user
                while True:
                    new_user = User(
                        name= input("User Name -> ")
                    )
                    
                    try:
                        self.user_operations.add_user(new_user)
                    except ValueError as e:
                        print(e)
                        input("Press Enter to continue...")
                        return

                    print("User added successfuly !")
                    if not self.continue_to_menu():
                        break

                    clear()

            case (2, "user_ops"): # Delete user
                while True:
                    user_name = input("User name -> ")

                    try:
                        user_list = self.user_operations.search_user(user_name)
                    except ValueError as e:
                        print(e)
                        input("Press Enter to continue...")
                        return

                    formatted_list = self.user_operations.format_user_list(user_list)

                    clear()
                    choice = self.get_choice(formatted_list)

                    self.user_operations.delete_user(user_list[choice - 1][0])

                    print("User deleted successfully !")
                    if not self.continue_to_menu():
                        break
                    
                    clear()


            case (3, "user_ops"): # Search user
                user_name = input("User name -> ")  
                
                try:
                    user_list = self.user_operations.search_user(user_name)
                except ValueError as e:
                    print(e)
                    input("Press Enter to continue...")
                    return
                
                clear()
                formatted_list = self.user_operations.format_user_list(user_list)

                self.user_operations.print_users(formatted_list)
                
                input("Press Enter to continue...")

            case (4, "user_ops"): # View all users
                self.user_operations.view_all_users()
                
                input("Press Enter to continue...")
                      
            case (5, "user_ops"): # Return to Main menu
                return

app = Main()
app.start()