class Book():
    def __init__(self, name, author,  id = None,):
        self.name = name  # Access name setter
        self.author = author # Access author setter
        self.__id = id # Access id setter

    @property # Book Name Getter
    def name(self):
        return self.__name
    
    @name.setter # Book Name Setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty !")
    
        self.__name = name


    @property # Author Getter
    def author(self):
        return self.__author
    
    @author.setter # Author Getter
    def author(self, author):
        if not author.strip():
            raise ValueError("Name cannot be empty !")
    
        self.__author = author


    @property # Id Getter
    def id(self):
        return self.__id
    