import tkinter as tk
import customtkinter as ctk
from customtkinter import *
from tkinter import * 
import pymssql
import pandas as pd 


# collegamento db
conn = pymssql.connect(server='5.172.64.20\sqlexpress', user='porta.matteo', password='xxx123##', database='porta.matteo')

window = ctk.CTk()

# specifiche finestra
window.geometry("600x600")
window.title("Hello TkInter!")
window.resizable(False, False)  # L'utente non può modificare la grandezza della finestra 


ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
# funzioni
'''
def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1)

def second_function():
    text = "Nuovo Messaggio! Nuova Funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1)




# bottoni
first_button = tk.Button(text="Saluta!", command=first_print)
first_button.grid(row=0, column=0, sticky="W")

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")
'''

label1 = tk.Label(window,text='Opzioni',fg="white",bg="#212325",font=("Helvetica", 24))
label1.grid(row=0, column=1 ,columnspan=2,sticky="N")


def add_utente():
    if nome_input.get() != '' and cognome_input != '':
        nome_text = nome_input.get()
        cognome_text = cognome_input.get()
        cursor = conn.cursor(as_dict=True)
        q = 'INSERT INTO test(nome,cognome) VALUES(%(nome)s, %(cognome)s)' 
        p = {"nome": f"{nome_text}","cognome": f"{cognome_text}"}
        cursor.execute(q, p)
        conn.commit()

        
        response_label = ctk.CTkLabel(master=window,text='Utente aggiunto',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")
                
    else:
        response_label = ctk.CTkLabel(master=window,text='Devi inserire il tuo nome e congome',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")

def delete_utente():
    if nome_input.get() != '' and cognome_input != '':
        nome_text = nome_input.get()
        cognome_text = cognome_input.get()
        cursor = conn.cursor(as_dict=True)
        q = 'DELETE FROM test WHERE nome = %(nome)s AND cognome = %(cognome)s' 
        p = {"nome": f"{nome_text}","cognome": f"{cognome_text}"}
        cursor.execute(q, p)
        conn.commit()

        
        response_label = ctk.CTkLabel(master=window,text='Utente Cancellato',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")
                
    else:
        response_label = ctk.CTkLabel(window,text='Devi inserire il tuo nome e congome',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")

# Aggiungi Utente


#  INPUT NOME
nome_input = ctk.CTkEntry(master=window,border_width=3,fg_color="white",text_color="#2DA775",border_color="#2DA775")
nome_input.grid(row=2, column=0, sticky="WE",padx=10,pady=10)

#  INPUT COGNOME
cognome_input = ctk.CTkEntry(master=window,border_width=3,fg_color="white",text_color="#2DA775",border_color="#2DA775")
cognome_input.grid(row=2, column=1, sticky="WE",padx=10,pady=10)


invio_input = ctk.CTkButton(master=window,text="Aggiungi Utente", command=add_utente)
invio_input.grid(row=3, column=0)

# Cancella Utente
invio_input = ctk.CTkButton(master=window,text="Cancella Utente", command=delete_utente)
invio_input.grid(row=3, column=1)

window.mainloop()