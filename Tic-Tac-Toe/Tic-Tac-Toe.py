import os
import math

def clear():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def check_board(board, mark):
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True
         
    return((board[0][0] == board[1][0] == board[2][0] == mark) or
    
    (board[0][1] == board[1][1] == board[2][1] == mark )or

    (board[0][2] == board[1][2] == board[2][2] == mark) or

    (board[0][0] == board[1][1] == board[2][2] == mark) or

    (board[0][2] == board[1][1] == board[2][0] == mark))

    


def start_game(u1, u2):
    move_counter = 0
    current_player = ""

    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    if u1["mark"] == "X":
        current_player = u1
    else:
        current_player = u2
    print("\n")

    while move_counter != 9:
        for row in board:
            print(" | ".join(row))
            
        while True:
            
            print(f"\n\n{current_player['name']}'s Turn !")
            try:
                move = int(input("Seçim ->"))
                if move <= 0 or move >= 10:
                    print("Hatalı giriş")
                    continue
                break
            except ValueError:
                print("Hatalı giriş")
                clear()
                continue

        index = move - 1
        row = index // 3
        column = index  % 3
        
        if not board[row][column].isnumeric():
            clear()
            print("Bu hücre zaten dolu !")
            input()
            continue
        else:
            board[row][column] = current_player["mark"]
        
        check_win = check_board(board, current_player["mark"])

        if check_win == True:
            clear()
            print(f"{current_player["name"]} oyunu kazandı  !")
            print("Ana menüye geri dönülüyor...")
            input()
            main_menu()

        if current_player == u1:
            current_player = u2
        else:
            current_player = u1

        move_counter += 1

    clear()
    print(f"Kazanan yok !")
    print("Ana menüye geri dönülüyor...")
    input()
    main_menu()


def choose_mark(u1, u2):
    isValid = False
    
    while isValid == False:

        choose = input( "X ve ya Y , birini seç -> ").upper()
        clear()

        if "X" in choose:
            isValid = True
            print(f"{u1["name"]} Önce başlayacak !")

            u1["mark"] = "X"
            u2["mark"] = "Y"
        elif "Y" in choose:
            isValid = True
            print(f"{u2["name"]} Önce başlayacak !")

            u1["mark"] = "Y"
            u2["mark"] = "X"
        else:
            print("Hatalı seçim ! Tekrar dene ")
            continue
    input()
    clear()
    start_game(u1, u2)
        
def main_menu():
    clear()
    u1 = {
        "name" : "",
        "mark" : ""
          }

    u2 = {
        "name" : "",
        "mark" : ""
        }

    options = [
        "1-) Oyuna başla",
        "2-) Çıkış yap"
    ]

    print("\n".join(options))
    
    secim = int(input("Seçim -> "))
        
    match(secim):
        case 1:
            u1["name"] = input("Oyuncu 1 ismi -> ")
            u2["name"] = input("Oyuncu 2 ismi -> ")

            choose_mark(u1, u2)
        case 2:
                exit()




if __name__ == "__main__":
    main_menu()