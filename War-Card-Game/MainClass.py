import CardClass as CC
import PlayerClass as PC
import GameClass as GC

import random


rütbeler = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Kız", "Vale", "As"]
semboller = ["Sinek", "Kupa", "Maça", "Karo"]

def kartlarlari_karistir(kartlar):
    random.shuffle(kartlar) # -> hiçbir şeyi return etmez , sadece listeyi karar
    return kartlar

def kartlari_dagit(kartlar): 
        deste1 = kartlar[: int(len(kartlar) / 2)]
        deste2 = kartlar[int(len(kartlar) / 2) :]

        return deste1, deste2

def oyunu_baslat(B1, B2):
    game = GC.Game(B1, B2)
    game.baslat()

def oyunu_hazirla():
    kartlar = [CC.Card(rütbe, sembol) for rütbe in rütbeler for sembol in semboller]
    for rütbe in rütbeler:
        for sembol in semboller:
            kartlar.append(CC.Card(rütbe, sembol))
    
    karilmis_kartlar = kartlarlari_karistir(kartlar)
    deste_B1, deste_B2 = kartlari_dagit(kartlar= karilmis_kartlar)

    B1 = PC.Player("bilgisayar1", deste_B1)
    B2 = PC.Player("bilgisayar2", deste_B2)

    oyunu_baslat(B1, B2)
    return()
    
def secim(menu):

    print("\n".join(menu))

    while True:
        try:
            secim = int(input("Seçim ->"))
            if secim < 1 or secim > len(menu):
                print("lütfen geçerli bir seçim yapın !")
                continue
        except:
            print("lütfen geçerli bir seçim yapın !")
            continue
        else:
            return secim


def menu():
    menu = ["1-) Oyuna başla",
                  "2-) Çıkış yap"]
    
    kullanici_secimi = secim(menu)

    match(kullanici_secimi):
        case 1:
            oyunu_hazirla()
        case 2:
            print("Cikis yapiliyor....")
            exit()


if __name__ == "__main__":
    menu()