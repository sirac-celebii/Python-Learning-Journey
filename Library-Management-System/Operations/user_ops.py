from Database import UserDatabase

class UserOperations():
    def __init__(self):
        self.user_db = UserDatabase()

    def _get_user_id(self, user_name):
        pass

    def _get_all_users(self):
        user_list = self.user_db.get_all_users() 

        if user_list:
            return user_list
        else:
            raise ValueError("No user found in Database !")

    def add_user(self, user):
        self.user_db.add_user(user)

    def delete_user(self, user_id):
        self.user_db.delete_user(user_id)

    def search_user(self, user_name):
        user_list = self.user_db.search_user(user_name)

        if user_list:
            return user_list
        else:
            raise ValueError("User not found !")

    def view_all_users(self):
        user_list = self._get_all_users()

        formatted_list = self.format_user_list(user_list)

        self.print_users(formatted_list)
    
    def format_user_list(self, users):
        formatted_list = []

        for user in users:
            formatted_list.append(f"Id : {user[0]} | User Name : {user[1]}")

        return formatted_list   
    
    def print_users(self, users):
        for user in users:
            print(user)

    def close_db(self):
        self.user_db.close()
    
     