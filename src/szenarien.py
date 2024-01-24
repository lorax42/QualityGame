import random

import charakter as c
import utils as u

# ERROR: undefinierte Wahl eines Szenarios
def errorWahlSzenario(szenario,wahl):
    #print("ERROR: undefinierte Wahl eines Szenarios\nSzenario=%s\nwahl=%d" %(szenario,wahl))
    u.logMssg("ERROR: undefinierte Wahl eines Szenarios\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
    return 0

def errorSzenario(szenario,wahl):
    #print("ERROR: in einem Szenario\nSzenario=%s\nwahl=%d" %(szenario,wahl))
    u.logMssg("ERROR: in einem Szenario\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
    return 0

def undefError(szenario,error):
    #print("ERROR: undefinierter error in szenario=%s\nerror=%d" %(szenario,error))
    u.logMssg("ERROR: undefinierter error in szenario="+str(szenario),error,1)
    return 0

# zufällige Szenarienwahl
def szenario():
    numSzenario=1 # Anzahl der Szenarien
    wahl=random.randint(0,100000)%numSzenario#(numSzenario-1)
    
    if wahl==0:
        x=szenario1()
    #elif wahl==1:
        #x=szenario2()
    #elif wahl==2:
        #x=szenario3()
    else:
        errorWahlSzenario("szenario",wahl)
        return 1
    
    # Error checking
    if x==0:
        return 0
    elif x==1:
        errorSzenario("szenario",wahl)
        return 1
    elif x==2: # für dieses Szenario unqualifiziert
        szenario()
        return 0
    else:
        undefError("szenario",x)
        return 1
    
    return 0

###SZENARIEN###

# Szenario 1
def szenario1():
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
        errorWahlSzenario("szenario1",wahl)
        return 1
    
    if x==0:
        return 0
    elif x==1:
        errorSzenario("szenario1",wahl)
    else:
        undefError("szenario1",x)
    
    return 0
