import os

class Game:
    def __init__(self, bilgisayar1, bilgisayar2):
        self.B1 = bilgisayar1
        self.B2 = bilgisayar2
        self.kart_havuzu = []

    def temizle(self):
        os.system("cls" if os.name == "nt" else "clear")

    def savas(self):

        B1_kartlari = []
        B2_kartlari = []


        input("B1 kart çekiyor...")
        B1_kartlari = self.B1.dort_kart_cek()
        self.temizle()
        input("B2 kart çekiyor...")
        B2_kartlari = self.B2.dort_kart_cek()
        self.temizle()

        self.kart_havuzu.extend(B1_kartlari)
        self.kart_havuzu.extend(B2_kartlari)

        kart_B1 = B1_kartlari[-1] 
        kart_B2 = B2_kartlari[-1]  

        return self.kartlari_karsilastir(kart_B1, kart_B2)

    def kazanan_var_mi(self):
        kart_sayisi_B1 = len(self.B1.deste)
        kart_sayisi_B2 = len(self.B2.deste)

        if kart_sayisi_B1 == 0:
            return self.B2
        elif kart_sayisi_B2 == 0:
            return self.B1
        else:
            return None

    def kartlari_karsilastir(self, kart_B1, kart_B2):
        kazanan = None

        if kart_B1.güc > kart_B2.güc:
            kazanan = self.B1
        elif kart_B1.güc < kart_B2.güc:
            kazanan = self.B2
        else:
            print("Savaş !\n")
            kazanan = self.savas()

        return kazanan

    def baslat(self):
        while True:
            self.temizle()

            kart_B1 = self.B1.kart_cek()
            kart_B2 = self.B2.kart_cek()


            print(f"B1'in kartı : {kart_B1.isim:<2} || B2'nin kartı : {kart_B2.isim:<2}")


            self.kart_havuzu.append(kart_B1)
            self.kart_havuzu.append(kart_B2)

            round_kazanan = self.kartlari_karsilastir(kart_B1, kart_B2)
            
            if round_kazanan == self.B1:
                self.B1.deste.extend(self.kart_havuzu)
            else:
                self.B2.deste.extend(self.kart_havuzu)

            print(f"{round_kazanan.isim} bu round'u kazandı !")
            
            if self.B1.karti_var_mi() == False:
                print("Oyunu B2 kazandı !")
                break
            elif self.B2.karti_var_mi() == False:
                print("Oyunu B1 kazandı !")
                break
            else:
                kullanici_secimi = input("Bitirmek için q, Devam etmek için Enter'a basınız...\n->")
                if kullanici_secimi == "q":
                    print("Oyundan bitiriliyor...")
                    exit()

            self.kart_havuzu = []

            