import tkinter as tk
from customtkinter import *
from tkinter import * 
import pymssql
import pandas as pd 

# collegamento db
conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='porta.matteo', password='xxx123##', database='porta.matteo')

window = tk.Tk()

# specifiche finestra
window.geometry("600x600")
window.title("Hello TkInter!")
window.resizable(False, False)  # L'utente non può modificare la grandezza della finestra 


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

def add_utente():
    if nome_input.get() != '' and cognome_input != '':
        nome_text = nome_input.get()
        cognome_text = cognome_input.get()
        cursor = conn.cursor(as_dict=True)
        q = 'INSERT INTO test(nome,cognome) VALUES(%(nome)s, %(cognome)s)' 
        p = {"nome": f"{nome_text}","cognome": f"{cognome_text}"}
        cursor.execute(q, p)
        conn.commit()

        
        response_label = tk.Label(window,text='Utente aggiunto',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")
                
    else:
        response_label = tk.Label(window,text='Devi inserire il tuo nome e congome',font=("Helvetica", 15))
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

        
        response_label = tk.Label(window,text='Utente Cancellato',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")
                
    else:
        response_label = tk.Label(window,text='Devi inserire il tuo nome e congome',font=("Helvetica", 15))
        response_label.grid(row=4, columnspan=2, sticky="WE")

# Aggiungi Utente
label1 = tk.Label(window,text='Opzioni')
label1.grid(row=0, columnspan=2)

#  input nome
nome_input = tk.Entry()
nome_input.grid(row=2, column=0, sticky="WE",padx=10,pady=10)

#  input cognome
cognome_input = tk.Entry()
cognome_input.grid(row=2, column=1, sticky="WE")

invio_input = tk.Button(text="Aggiungi Utente", command=add_utente)
invio_input.grid(row=3, column=0)

# Cancella Utente
invio_input = tk.Button(text="Cancella Utente", command=delete_utente)
invio_input.grid(row=3, column=1)

window.mainloop()