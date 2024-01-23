import random

import charakter as c

# ERROR: undefinierte Wahl eines Szenarios
def errorWahlSzenario(szenario,wahl):
    print("ERROR: undefinierte Wahl eines Szenarios\nSzenario=%s\nwahl=%d" %(szenario,wahl))

# zufällige Szenarienwahl
def szenario():
    wahl=random.randint(0,100000)%2 # Endwert gleich der Anzahl an Szenarien
    
    if wahl==0:
        szenario1()
    elif wahl==1:
        szenario2()
    elif wahl==2:
        szenario3()
    else:
        errorWahlSzenario("szenario",wahl)

###SZENARIEN###

# Szenario 1
def szenario1():
    if c.level<2:
        return
    
    print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
    wahl=int(input("> "))

    if wahl==1:
        c.addPunkte(-5)
    elif wahl==2:
        c.addPunkte(-3)
    elif wahl==3:
        c.addPunkte(5)
    else:
        errorWahlSzenario("szenario1",wahl)
        
# Szenario 2
def szenario2():
    if c.level<5:
        return
    
    print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
    wahl=int(input("> "))

    if wahl==1:
        c.addPunkte(-5)
    elif wahl==2:
        c.addPunkte(-3)
    elif wahl==3:
        c.addPunkte(5)
    else:
        errorWahlSzenario("szenario2",wahl)
        
# Szenario 3
def szenario3():
    if c.level<10:
        return
    
    print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
    wahl=int(input("> "))

    if wahl==1:
        c.addPunkte(-5)
    elif wahl==2:
        c.addPunkte(-3)
    elif wahl==3:
        c.addPunkte(5)
    else:
        errorWahlSzenario("szenario3",wahl)
        