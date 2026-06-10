# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: Bram KvO 114412
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
    gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(ingevoerde_klantnaam.get())
    print(gevonden_klanten)

    invoerveldKlantnaam.delete(0, END)
    invoerveldKlantNr.delete(0, END)
    for rij in gevonden_klanten: 
        invoerveldKlantNr.insert(END, rij[0]) 
        invoerveldKlantnaam.insert(END, rij[1])


def zoekPizza():
    gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(ingevoerde_pizzanaam.get())
    print(gevonden_pizza)

    invoerveldPizza.delete(0, END)
    for rij in gevonden_pizza: 
        listboxMenu.insert(END, rij)

def toonMenuInListbox():
    listboxMenu.delete(0, END) #maak de listbox leeg
    listboxMenu.insert(0, "ID Gerecht Prijs")
    pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
    for regel in pizza_tabel:
        listboxMenu.insert(END, regel)

def haalGeselecteerdeRijOp(event):
    #bepaal op welke regel er geklikt is
    geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
    #haal tekst uit die regel
    geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
    #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
    invoerveldGeselecteerdePizza.delete(0, END) 
    #zet tekst in veld
    invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)

### --------- Hoofdprogramma  ---------------

venster = Tk()
venster.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
venster.wm_title("MC Pizzeria")

knopsluit = Button(venster, text="sluiten", width=12, command=venster.destroy)
knopsluit.grid(row=17, column=4)

labelintro = Label(venster, text="welcome")
labelintro.grid(row=0, column=0, sticky="W")

labelklant = Label(venster, text="klantnaam: ")
labelklant.grid(row=1, column=0, sticky="W")

ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(venster, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")

invoerveldKlantNr = Entry(venster)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

knopZoekKlant = Button(venster, text="zoek klant", width=12, command=zoekKlant)
knopZoekKlant.grid(row=1, column=4)

pizzalabel = Label(venster, text="pizza naam:")
pizzalabel.grid(row=3, column=0, sticky="W")

ingevoerde_pizzanaam = StringVar()
invoerveldPizza = Entry(venster, textvariable=ingevoerde_pizzanaam)
invoerveldPizza.grid(row=3, column=1, sticky="W")

knopZoekPizza = Button(venster, text="Zoek pizza", width=12, command=zoekPizza)
knopZoekPizza.grid(row=3, column=4)

labelMogelijkheden = Label(venster, text="Mogelijkheden:")
labelMogelijkheden.grid(row=4, column=0)

listboxMenu = Listbox(venster, height=6, width=50)
listboxMenu.grid(row=4, column=1, rowspan=6, columnspan=2, sticky="W")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)

listBoxScrollbar = Scrollbar(venster, orient=VERTICAL)
listBoxScrollbar.grid(row=4, column=3, rowspan=6, sticky="NS")

listboxMenu.config(yscrollcommand=listBoxScrollbar.set)
listBoxScrollbar.config(command=listboxMenu.yview)

knopToonPizza = Button(venster, text="Toon alle pizza's", command=toonMenuInListbox)
knopToonPizza.grid(row=4, column=4)

labelPizzaSelecteerd = Label(venster, text="Geselecteerde pizza:")
labelPizzaSelecteerd.grid(row=10, column=0, sticky="W")

selecteerdePizza = StringVar()
invoerveldGeselecteerdePizza = Entry(venster, textvariable=selecteerdePizza)
invoerveldGeselecteerdePizza.grid(row=10, column=1, sticky="W")


#reageert op gebruikersinvoer, deze regel als laatste laten staan
venster.mainloop()
