import tkinter as tk
from tkinter import ttk, messagebox
import time
import datetime

pomodoro_length = 25 * 60

pomodoro_length_str = datetime.timedelta(seconds= pomodoro_length)

time_since_start = None
start_time = None
time_left = None

root = tk.Tk()
root.resizable(False, False)

window_width = 400
window_height = 200

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

x = ((screen_width // 2) - (window_width // 2))
y = ((screen_height // 2) - (window_height // 2))


root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.title("Pomodoro App")

label = tk.Label(text= "Pomodoro Counter V2.0")
label.pack()

counter_frame = tk.Frame(root)
counter_frame.place(relx= 0.5, rely= 0.5, anchor= "center")

timer_label = ttk.Label(counter_frame, text= pomodoro_length_str, font = ("ds-digital", 50, "bold"))
timer_label.grid(row= 0, column= 0, pady= 5)


def reset_timer():
    global pomodoro_length, time_since_start, time_left, start_time

    pomodoro_length = 25 * 60
    time_since_start = None
    start_time = None
    time_left = None

    timer_label.configure(text= pomodoro_length_str)

def continue_timer():
    global start_time, time_left, pomodoro_length
    pomodoro_length = time_left
    start_time = time.time()
    continue_btn.grid_remove()
    # start_btn.grid()
    timer()

def start_timer():
    global start_time
    start_time = time.time()
    start_btn.grid_remove()
    timer()

def stop_timer():
    global start_time
    start_time = None #
    # start_btn.grid_remove()
    continue_btn.grid()

def timer():
    global start_time, time_since_start, time_left
    if start_time is not None:
        time_since_start = time.time() - start_time
        time_left = max(0, pomodoro_length - time_since_start)

        time_left_str = str(datetime.timedelta(seconds= time_left)) # second cinsinden kalan sureyi saat/dakika/saniye çevir
        time_left_str = time_left_str.split(".")[0]
        timer_label.config(text= time_left_str)

    
        root.after(1000, timer)
    
    if time_left is not None and time_left <= 0:
        stop_timer()
        reset_timer()

        root.deiconify()
        root.attributes("-topmost", True)
        root.lift() # -> pencereyi en üste çıkar (?)
        root.focus_force() # Focus verir (aktif pencere yapar)

        root.after(100, lambda : root.attributes("-topmost", False))
        start_btn.grid()
        continue_btn.grid_remove()

        

btn_frame = ttk.Frame(counter_frame)
btn_frame.grid(row= 1, column= 0, columnspan= 2, pady= 10)

start_btn = ttk.Button(btn_frame, text= "Start", width= 10, command= start_timer)
start_btn.grid(row= 0, column= 0, padx= 5)

stop_btn = ttk.Button(btn_frame, text= "Stop",  width= 10, command= stop_timer)
stop_btn.grid(row= 0, column= 1, padx= 5)

continue_btn = ttk.Button(btn_frame, text= "Continue", width= 10, command= continue_timer )
continue_btn.grid(row= 0, column= 2, padx= 5)
continue_btn.grid_remove()

root.mainloop()
