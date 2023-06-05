import tkinter as tk
import customtkinter as ctk
from tkinter import * 
import pymssql


ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# collegamento db
#192.168.40.16\SQLEXPRESS
#5.172.64.20\sqlexpress
conn = pymssql.connect(server='192.168.40.16\SQLEXPRESS', user='porta.matteo', password='xxx123##', database='porta.matteo')
labels = []
window = ctk.CTk()

# specifiche finestra
window.geometry("800x600")
window.title("Tkinter Poots GUI")
window.resizable(False, False)  # L'utente non puÃ² modificare la grandezz a della finestra 

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1) 
window.columnconfigure(3, weight=1) 
window.columnconfigure(4, weight=1) 
window.columnconfigure(5, weight=1) 

def add_utente(new_user):
    if new_user[0] == '' or new_user[1] == '' or new_user[2] == '':
        return print('vuoto')
    cursor = conn.cursor(as_dict=True)

    p = {"name": f"{new_user[0]}","email": f"{new_user[1]}"}
    q = 'SELECT * FROM utente WHERE Username like %(name)s and Email = %(email)s' 
    cursor.execute(q, p)
    user = cursor.fetchall()
    if user != []:
        return print('esiste gia')

    p = {"name": f"{new_user[0]}","email": f"{new_user[1]}","pwd": f"{new_user[2]}"}
    q = 'INSERT INTO utente VALUES(%(name)s, %(email)s, %(pwd)s)' 
    cursor.execute(q, p)
    conn.commit()
    # Chiude la connessione al server SQL
    cursor.close()
    return remove_label("")


def finestra_crea():
    # Toplevel object which will
    # be treated as a new window
    newWindow = ctk.CTkToplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Finestra di Ricerca")
 
    # sets the geometry of toplevel
    newWindow.geometry("400x200")
 
    newWindow.columnconfigure(0, weight=1)

    name = ctk.CTkEntry(newWindow,placeholder_text="Username")
    name.grid(row=0, column = 0, pady=7,sticky="WE")

    email = ctk.CTkEntry(newWindow,placeholder_text="Email")
    email.grid(row=1, column =0, pady=7,sticky="WE")

    pwd = ctk.CTkEntry(newWindow,placeholder_text="Password")
    pwd.grid(row=2, column =0, pady=7,sticky="WE")


    def click():
        new_user = []
        new_user.append(name.get())
        new_user.append(email.get())
        new_user.append(pwd.get())

        #richiamo la funzione crea
        add_utente(new_user)



    buttn = ctk.CTkButton(newWindow, text='Crea Utente', command=click)
    buttn.grid(row=3, column = 0, pady=7,sticky="WE") 
# a button widget which will open a
# new window on button click
btn = ctk.CTkButton(window,text ="Crea",command = finestra_crea)
btn.grid(row=0, column=5,padx=20,pady=20,sticky="E")

def getInput():
   
    inputUtente = input.get()  
    print(inputUtente)
    return remove_label(inputUtente)

def remove_label(x):
    global labels
    for label in labels:
        label.destroy()

    labels = []

    return visualizza_utenti(x)

def visualizza_utenti(x):
    print(x)
    cursor = conn.cursor()
    # Esegue la query per recuperare gli utenti
    
    if x == "":    
         cursor.execute('SELECT * FROM utente')
    else:
        cursor.execute(f"SELECT * FROM utente WHERE Username LIKE '{x}%'")
        
        

    users = cursor.fetchall()

    # Chiude il cursor
    cursor.close()
    
   
    # Visualizza gli utenti nella finestra
    
    lista = []
    for i, user in enumerate(users):
        for j, value in enumerate(user):
            print(j,value)
            label = ctk.CTkLabel(window, text=value)
            label.grid(row=i+2, column=j,sticky="W",padx=10, pady=10)
            lista.append(value) if j == 0 else None
            labels.append(label)
         
        modifica = ctk.CTkButton(master=window,text="Modifica" ,command=lambda x=lista[i]: finestra_modifica(x))
        modifica.grid(row=i+2,column=4,sticky="WE",padx=20)
        labels.append(modifica)
        cancella = ctk.CTkButton(master=window,text="Cancella",hover_color='#52170b',fg_color='red' ,command=lambda x=lista[i]: cancella_utente(x))
        cancella.grid(row=i+2,column=5,sticky="WE",padx=20)
        labels.append(cancella)
        

            

    print(lista)

def modifica_utente(new_user,x):
    
    if new_user[0] == '' or new_user[1] == '' or new_user[2] == '':
        return print('vuoto')
    cursor = conn.cursor()

    p = {"name": f"{new_user[0]}","email": f"{new_user[1]}"}
    q = 'SELECT * FROM utente WHERE Username like %(name)s and Email = %(email)s' 
    cursor.execute(q, p)
    user = cursor.fetchall()
    if user != []:
        return print('esiste gia')

    # Esegue la query per recuperare gli utenti
    p = {"name": f"{new_user[0]}","email": f"{new_user[1]}","pwd": f"{new_user[2]}"}
    cursor.execute(f'UPDATE utente SET Username = %(name)s, Email = %(email)s, password = %(pwd)s WHERE Id = {x}', p)
    conn.commit()
    # Chiude la connessione al server SQL
    cursor.close()
    return remove_label("")

def finestra_modifica(x):

    cursor = conn.cursor()
    # Esegue la query per recuperare gli utenti
    cursor.execute(f'SELECT * FROM utente WHERE id = {x}')
    [user] = cursor.fetchall()
    cursor.close()

    newWindow = ctk.CTkToplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Finestra di Ricerca")
 
    # sets the geometry of toplevel
    newWindow.geometry("400x200")

    newWindow.columnconfigure(0, weight=1)

    name = ctk.CTkEntry(newWindow,placeholder_text=f"{user[1]}")
    name.grid(row=0, column = 0, pady=7,sticky="WE")

    email = ctk.CTkEntry(newWindow,placeholder_text=f"{user[2]}")
    email.grid(row=1, column = 0, pady=7,sticky="WE")

    pwd = ctk.CTkEntry(newWindow,placeholder_text=f"{user[3]}")
    pwd.grid(row=2, column = 0, pady=7,sticky="WE")

        
    def click():
        new_user = []
        new_user.append(name.get())
        new_user.append(email.get())
        new_user.append(pwd.get())

        #richiamo la funzione modifica
        modifica_utente(new_user,x)



    buttn = ctk.CTkButton(newWindow, text='Modifica',command=click)
    buttn.grid(row=3, column = 0, pady=7,sticky="WE")

    return x  

input = ctk.CTkEntry(window,width=400,height=35)
input.grid(row=0,columnspan=3, sticky=W,padx= 10,pady= 10)

getButton = ctk.CTkButton(window,text="Cerca", command=getInput)
getButton.grid(row=0,column=3,sticky=W)

def cancella_utente(x):
    print(x)
    cursor = conn.cursor()
    # Esegue la query per recuperare gli utenti
    cursor.execute(f'DELETE FROM utente WHERE Id = {x}')
    conn.commit()
    # Chiude la connessione al server SQL
    cursor.close()

    return remove_label("")

header1 = ctk.CTkLabel(master=window, text="Id ",font=('Chaparral Pro', 18, 'bold'))
header1.grid(row=1, column=0,padx=10,pady=10,sticky="W")
header2 = ctk.CTkLabel(master=window, text="Username ",font=('Chaparral Pro', 18, 'bold'))
header2.grid(row=1, column=1,padx=10,pady=10,sticky="W")
header3 = ctk.CTkLabel(master=window,padx=0,pady=10, text="Email ",font=('Chaparral Pro', 18, 'bold'))
header3.grid(row=1, column=2,padx=10,pady=10,sticky="W")
header4 = ctk.CTkLabel(master=window, text="Password ",font=('Chaparral Pro', 18, 'bold'))
header4.grid(row=1, column=3,padx=10,pady=10,sticky="W")

visualizza_utenti("")
window.mainloop()