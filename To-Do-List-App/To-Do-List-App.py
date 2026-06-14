# import datetime
import os
# import tkinter

# day = datetime.datetime.today().day
# month = datetime.datetime.today().month
# year = datetime.datetime.today().year


def temizle():
    #Clear the terminal
    os.system("cls" if os.name == "nt" else "clear")


def get_option(menu, msg = "\nEnter '0' to return the menu."):
    #Print options/tasks
    for index, opt in enumerate(menu, 1):
        print(f"{index}-) {opt}")

    #Get option from user
    while True:
        try:
            print(msg)
            option = int(input("Your Option -> "))
            if option < 0 or option > len(menu):
                temizle()
                print("Please enter valid number !")
                continue
            break
        except ValueError:
            temizle()
            print("Please enter a number !")
            continue
        except Exception as e:
            temizle()
            print(f"Please try again : {e} ")

    temizle()
    return(option)
 

def get_tasks():
    lines = []
    
    #Get all tasks from file then remove empty lines
    with open("Tasks.txt", mode= "r", encoding= "utf-8") as file:
        for line in file.readlines():
            line = line.rstrip("\n")
            lines.append(line)

    return(lines)

def get_input():
    subject = None
    task = None
    
    #Get subject and task from user
    while True:
        subject = input("Subject of the Task -> ")
        task = input("Task -> ")
        
        if subject == None or task == None:
            temizle()
            print("Please enter task/subject !")
            continue
        else:
            break
    
    temizle()
    return(subject ,task)

def add_task(subject, task):
    #Add task to the Tasks file
    #mode = "a" -> appen mode (adds data to end of the file)
    with open("Tasks.txt", mode= "a", encoding= "utf-8" ) as file:
        file.write(f"{subject}: {task}\n") 


def update_tasks(tasks):
    #mode = "w" -> Overwrites the file or creates a new one if it does not exist
    with open("Tasks.txt", mode= "w", encoding= "utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n") 


def delete_task(option, tasks):
    tasks.pop(option) #Removes the specific task from the tasks
    update_tasks(tasks)
    print("Task deleted succesfully !\n")
    input("\nDevam etmek için bir tuşa basınız...")
    temizle()

    if not tasks:
        print("No tasks left !")


def show_tasks(tasks):
    for index, task in enumerate(tasks, 1):
        print(f"{index}-) {task}")

    input("\nDevam etmek için bir tuşa basınız...")
    temizle()
       

def menu():
    while True:
        menu = ["Add Task",
                "Delete Task",
                "See Tasks",
                "Exit"]


        opt = get_option(menu, msg= "")

        match(opt):
            
            case 1:
                    subject, task = get_input()
                    add_task(subject, task)
            case 2:
                while True:
                    tasks = get_tasks()
                    option = get_option(tasks)
                    if option != 0:
                        delete_task((option - 1), tasks)
                    else:
                        break
            case 3:
                tasks = get_tasks()
                show_tasks(tasks)
            case 4:
                exit()
                print("Program ended successfully")


if __name__ == "__main__":
    menu()