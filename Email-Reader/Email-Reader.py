# Python Mail Organizer

import imaplib
import email
from email.header import decode_header
import re

import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.resizable(False, False)

window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width // 2) - (window_width // 2))
y = ((screen_height // 2) - (window_height // 2))

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("E-Mail Reader")

def get_account_info():
    global app_password
    mail = mail_input.get()
    password = app_password_input.get()
    
    logIn(mail, password)

def logIn(mail, password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    status , response = imap.login(mail, password)

    if status == "OK":
        fetch_mails(imap)
    else:
        print(f"Authentication Failed : {response}")
        

def fetch_mails(imap):
    imap.select("inbox")

    n = 3 # çekilecek mail sayısı

    stat, messages = imap.search(None, "ALL") # tüm mesajları getir , None -> charset;("UTF-8" gibi, None -> farketmez)

    mail_ids = messages[0].split() # mail ID'lerini çeker

    last_mails = mail_ids[-n:] # mail 198, mail 199 , mail 200 gibi eskiden yeniye

    for mail_id in reversed(last_mails): # reverse -> mail 200 , mail 199, mail 198 gibi yeniden eskiye
        res, msg = imap.fetch(mail_id, "(RFC822)") #ID'ye göre mail çek , RFC822 -> From , To, Subject, Body, Header e Attachments içerir yani mail'e ait tüm bilgiler
        for response in msg:
            if isinstance(response, tuple): # response bir Tuple midir ?
                msg = email.message_from_bytes(response[1]) # respopnse[0] -> b'1 (RFC822 {3421}) (ID, Format, Mail Boyutu(Byte)), Response[1] -> Mail Content

                From = msg["From"]

                body = get_body_part(msg)

                subject = decode_subjects(msg["Subject"])

                print(f"From : {From}")
                print(f"Subject : {subject} ")
                print(f"Body : {body}")
                print("=" * 50)

def get_body_part(msg):
    body = ""

    if msg.is_multipart():  #mesaj tek bir parçadan oluşmayabileceği için kontrol 
        for part in msg.walk():
            content_type = part.get_content_type()

            if content_type == "text/plain":
                body = part.get_payload(decode = True).decode() # bytes -> string -> text = .(decode = True).decode()
    else:
        body = msg.get_payload(decode = True).decode()

    return body

def decode_subjects(subject):
    decoded_parts = decode_header(subject)

    result = ""

    for part, encoding in decoded_parts: # Mail content ve encoding türü("UTF-8" gibi)
        if isinstance(part, bytes): # 'part' bir bytes mi ? part -> ham veri
            result += part.decode(encoding or "utf-8") # encoding arsa kullan yoksa "utf-8"
        else:
            result += part

    return result

# def number_of_mails(messages):
#     mail_ids = messages[0].split()

#     print(f"Mail sayısı : {len(mail_ids)}")
#     return mail_ids

form_frame = ttk.Frame(root)
form_frame.place(relx= 0.5, rely = 0.5, anchor= "center")


mail_label = ttk.Label(form_frame, text= "E-Mail")
mail_label.grid(row= 0 ,column= 0, padx= 1)

mail_input = ttk.Entry(form_frame, width= 25)
mail_input.grid(row= 0, column= 1, pady= 5)

app_password_label = ttk.Label(form_frame, text= "App Password")
app_password_label.grid(row= 1, column= 0, padx= 1)

app_password_input = ttk.Entry(form_frame, show= "*", width= 25)
app_password_input.grid(row= 1, column= 1, pady= 5)

submit_btn = ttk.Button(form_frame, text= "Submit", width= 10, command= get_account_info)
submit_btn.grid(row= 2, column= 1, pady= 5)


root.mainloop()