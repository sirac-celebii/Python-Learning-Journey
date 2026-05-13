class Player:
    def __init__(self, isim,  deste):
        self.isim = isim
        self.deste = deste

    def kart_cek(self):
        if self.karti_var_mi() == False:
            return []
        return self.deste.pop(0)
    
    def dort_kart_cek(self):
        kartlar = []
        while len(self.deste) != 0:
            if len(kartlar) < 4:
                kullanici_secimi = input("Bitirmek için q, kart çekmek için Enter'a basınız...\n->")
                if kullanici_secimi == "":
                    kartlar.append(self.deste.pop(0))
                    print(f"{len(kartlar)} kart çektiniz , kalan hakkınız {4 - len(kartlar)}")
            else:
                break
        return kartlar

        
    def karti_var_mi(self):
        return len(self.deste) 