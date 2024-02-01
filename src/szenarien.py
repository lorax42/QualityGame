import random

import charakter as c
import utils as u

# ERROR: undefinierte Wahl eines Szenarios
def errorWahlSzenario(szenario,wahl):
    u.logMssg("ERROR: undefinierte Wahl eines Szenarios\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
    return 0

def errorSzenario(szenario,wahl):
    u.logMssg("ERROR: in einem Szenario\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
    return 0

def undefError(szenario,error):
    u.logMssg("ERROR: undefinierter error in szenario="+str(szenario),error,1)
    return 0

# zufällige Szenarienwahl
def szenario():
    sID=0 # szenario ID

    szenarien={szenario1} # liste der Szenarien
    szen=random.choice(szenarien) # szen ist ein zufälliges Szenario
    x=szen() # szen wird ausgeführt
    
    # Error checking
    if x==0:
        return 0
    elif x==1:
        errorSzenario(sID,wahl)
        return 1
    elif x==2: # für dieses Szenario unqualifiziert
        szenario()
        return 0
    else:
        undefError(sID,x)
        return 1
    
    return 0

###SZENARIEN###

# Szenario 1
def szenario1():
    sID=1 # szenario ID
    if c.level<2:
        return 2
    
    print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
    wahl=int(input("> "))

    if wahl==1:
        x=c.addPunkte(-5)
    elif wahl==2:
        x=c.addPunkte(-3)
    elif wahl==3:
        x=c.addPunkte(5)
    else:
        errorWahlSzenario(sID,wahl)
        return 1
    
    if x==0:
        return 0
    elif x==1:
        errorSzenario(sID,wahl)
    else:
        undefError(sID,x)
    
    return 0
