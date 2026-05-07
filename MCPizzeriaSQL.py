# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in: Bram KvO 114412
#
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------
def maakTabellenAan():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_pizzas(
            gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
            gerechtNaam TEXT NOT NULL,
            gerechtPrijs REAL NOT NULL);""")
    print("tbl_pizzas aangemaakt")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam)
    opgehaalde_gegevens = cursor.fetchall()
    print("tabel " + tabel_naam + ":", opgehaalde_gegevens)

def voegPizzaToe(naam_nieuwe_pizza, prijs_nieuwe_pizza):
    cursor.execute("INSERT INTO tbl_pizzas VALUES(NULL, ?, ? )", (naam_nieuwe_pizza, prijs_nieuwe_pizza))
    db.commit()

    #print("pizza toegevoegd:")
    #printTabel("tbl_pizzas")

def verwijderPizza(gerechtNaam):
    cursor.execute("DELETE FROM tbl_pizzas WHERE gerechtNaam = ?", (gerechtNaam,))
    print("Gerecht verwijderd uit 'tbl_pizzas':", gerechtNaam )
    db.commit()
### --------- Hoofdprogramma  ---------------

maakTabellenAan()
verwijderPizza("Hawaii")
printTabel("tbl_pizzas")