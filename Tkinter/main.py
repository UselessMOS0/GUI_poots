import tkinter as tk
import customtkinter as ctk
from tkinter import * 
import pymssql



# collegamento db
conn = pymssql.connect(server='192.168.40.16\sqlexpress', user='porta.matteo', password='xxx123##', database='porta.matteo')

window = ctk.CTk()

# specifiche finestra
window.geometry("800x600")
window.title("Tkinter Poots GUI")
window.resizable(False, False)  # L'utente non può modificare la grandezza della finestra 

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)




# text = tk.Text(window, height=10)
# text.grid(row=0, column=0, sticky=tk.EW)
# scrollbar = tk.Scrollbar(window, orient='vertical', command=text.yview)
# scrollbar.grid(row=0, column=1, sticky=tk.NS)
# text['yscrollcommand'] = scrollbar.set

# # add sample text to the text widget to show the screen
# for i in range(1,50):
#     position = f'{i}.0'
#     text.insert(position,f'Line {i}\n');


ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = ctk.CTkToplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Finestra di Ricerca")
 
    # sets the geometry of toplevel
    newWindow.geometry("500x800")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window")
 
 
    label = Label(window,
                text ="This is the main window", font=("Helvetica", 18))
 
    Frm = ctk.CTkFrame(newWindow)
    Label(Frm,text='Enter Word to Find:').pack(side=LEFT)
    modify = ctk.CTkEntry(Frm)

    modify.pack(side=LEFT, fill=BOTH, expand=1)

    modify.focus_set()

    buttn = ctk.CTkButton(Frm, text='Find')
    buttn.pack(side=RIGHT)
    Frm.pack(side=TOP)

    txt = Text()

    txt.insert('1.0','''Enter here...''')
    txt.pack(side=BOTTOM)




# a button widget which will open a
# new window on button click
btn = ctk.CTkButton(master=window,
             text ="Ricerca",
             command = openNewWindow).grid(row=10, column=3,padx=20,pady=20,sticky="W")

             



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



Label(window,text='Enter Word to Find:')



def visualizza_utenti():
    cursor = conn.cursor()

    # Esegue la query per recuperare gli utenti
    cursor.execute('SELECT * FROM utente')
    users = cursor.fetchall()

    # Chiude la connessione al server SQL


    # Visualizza gli utenti nella finestra
    lista = []
    for i, user in enumerate(users):
        for j, value in enumerate(user):
            print(j,value)
            label = ctk.CTkLabel(window, text=value)
            label.grid(row=i+1, column=j,sticky="W",padx=10, pady=10)
            lista.append(value) if j == 0 else None

        modifica = ctk.CTkButton(master=window,text="Modifica" ,command=lambda x=lista[i]: modifica_utente(x))
        modifica.grid(row=i+1,column=4,sticky="E",padx=20)
        cancella = ctk.CTkButton(master=window,text="Cancella" ,command=lambda x=lista[i]: cancella_utente(x))
        cancella.grid(row=i+1,column=7,sticky="E")
    print(lista)


def modifica_utente(x):
    print(x)
    return x 

def cancella_utente(x):
    print(x)
    cursor = conn.cursor()

    # Esegue la query per recuperare gli utenti
    cursor.execute(f'DELETE FROM utente WHERE Id = {x}')
    conn.commit()
    # Chiude la connessione al server SQL


    return x


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
header1.grid(row=0, column=0,padx=10,pady=10,sticky="W")
header2 = ctk.CTkLabel(master=window, text="Username ",font=('Chaparral Pro', 18, 'bold'))
header2.grid(row=0, column=1,padx=10,pady=10,sticky="W")
header3 = ctk.CTkLabel(master=window,padx=10, text="Email ",font=('Chaparral Pro', 18, 'bold'))
header3.grid(row=0, column=2,padx=10,pady=10,sticky="W")
header4 = ctk.CTkLabel(master=window, text="Password ",font=('Chaparral Pro', 18, 'bold'))
header4.grid(row=0, column=3,padx=10,pady=10,sticky="W")




window.mainloop()