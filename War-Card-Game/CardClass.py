class Card:
    def __init__(self, rütbe, sembol):

        kart_gücü = {
            "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5,
            "6" : 6, "7" : 7, "8" : 8, "9" : 9, "Kız": 10,
            "Vale" : 11, "As" : 12 
        }

        self.sembol = sembol
        self.rütbe = rütbe
        self.güc = kart_gücü[self.rütbe]
        self.isim = f"{self.sembol} {self.rütbe}"

    def __str__(self):
        return f"Kart : {self.sembol} {self.rütbe}  Güc : {self.güc}"

