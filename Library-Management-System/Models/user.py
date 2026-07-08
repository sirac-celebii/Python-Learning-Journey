class User():
    def __init__(self, name, id = None):
        self.name = name
        self.__id = id
        # self.__books = books if books is not None else []


    @property # User Name Getter
    def name(self):
        return self.__name
    
    @name.setter # User Name Setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty !")
    
        self.__name = name

    # @property # User books Getter
    # def books(self):
    #     return self.__books
    
    @property # User id Getter
    def id(self):
        return self.__id