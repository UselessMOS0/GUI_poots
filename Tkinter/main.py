import tkinter as tk
import customtkinter as ctk
from tkinter import * 
import pymssql



# collegamento db
conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='porta.matteo', password='xxx123##', database='porta.matteo')

window = ctk.CTk()

# specifiche finestra
window.geometry("800x600")
window.title("Tkinter Poots GUI")
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

#label1 = tk.Label(window,text='Opzioni',fg="white",bg="#212325",font=("Helvetica", 24))
#label1.grid(row=0, column=1 ,columnspan=2,sticky="N")


def visualizza_utenti():
    cursor = conn.cursor()

    # Esegue la query per recuperare gli utenti
    cursor.execute('SELECT * FROM utente')
    users = cursor.fetchall()

    # Chiude la connessione al server SQL
    conn.close()

    # Visualizza gli utenti nella finestra
    for i, user in enumerate(users):
        for j, value in enumerate(user):
            label = ctk.CTkLabel(window, text=value)
            label.grid(row=i+1, column=j,sticky="W",padx=10, pady=10)
            modica = ctk.CTkButton(master=window,text="Modifica")
            modica.grid(row=i+1,column=4,sticky="E",padx=20)
            cancella = ctk.CTkButton(master=window,text="Cancella")
            cancella.grid(row=i+1,column=7,sticky="E")
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
'''

# V ISUALIZZA UTENTI 
visualizza_utenti()

header1 = ctk.CTkLabel(master=window, text="Id ",font=('Chaparral Pro', 18, 'bold'))
header1.grid(row=0, column=0,padx=10,sticky="W")
header2 = ctk.CTkLabel(master=window, text="Username ",font=('Chaparral Pro', 18, 'bold'))
header2.grid(row=0, column=1,padx=10,sticky="W")
header3 = ctk.CTkLabel(master=window,padx=10, text="Email ",font=('Chaparral Pro', 18, 'bold'))
header3.grid(row=0, column=2,padx=10,sticky="W")
header4 = ctk.CTkLabel(master=window, text="Password ",font=('Chaparral Pro', 18, 'bold'))
header4.grid(row=0, column=3,padx=10,sticky="W")

window.mainloop()