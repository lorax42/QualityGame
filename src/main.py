# QualityGame ist ein Spiel von Robin Ulke und Lloyd Bush, basierend auf den Büchern des Marc-Uwe Kling.
# Dieses Projekt steht unter der MIT-Lizenz. Mit dem source code dieses Spiels müsstest du eine Kopie erhalten haben, falls nicht ist sie unter https://mit-license.org zu finden.

import time
import os

import charakter as c
import szenarien as s
import utils as u

# SETUP

if os.path.exists("log.txt"):
  os.remove("log.txt")

u.logMssg("START",0,0)

u.clear() # Terminal reinigen

# Charakter und Umfeld aufstellen
u.logo()

c.name=str(input("Dein Nachname: "))
c.vorname=str(input("Dein Vorname: "))
c.level=10
c.punkte=c.level*100

# Einführende Geschichte

# HAUPTSCHLEIFE
runde=0 # Zähler
while True:
    runde+=1 # Rundenanzähler inkrementieren

    u.clear() # Terminal reinigen
    
    # Situation anzeigen
    print(c.vorname,c.name)
    print("Level:",c.level)
    print("Punkte:",c.punkte)
    print("###",runde)
    print()

    time.sleep(1)

    x=s.szenario() # Szenario stellen
    if x!=0:
        u.logMssg("ERROR: in Funktion szenario() (von main aus gesendet)",x,1)
        # runde-=1

    # (Antwort verarbeiten)
    # Konsequenzen ziehen
    # Charakter und Umfeld anpassen

    # Endbedingungen
    if c.level<=2: # zu niedriges Level
        break
    elif runde>=10: # maximale Rundenzahl erreicht
        break

# CLEANUP

u.clear() # Terminal reinigen
u.logo()

# Stats anzeigen
print("Du hast")
print("Level",c.level,"erreicht")
print(c.punkte,"Punkte gesammelt")
print(runde,"Runden überlebt")
print()

# offene Enden aufheben
# Geschichte beenden

# Abspann
time.sleep(5)
print("QualityGame ist ein Spiel von Robin Ulke und Lloyd Bush, basierend auf den Büchern des Marc-Uwe Kling.")
print("Dieses Projekt steht unter der MIT-Lizenz. Mit dem source code dieses Spiels müsstest du eine Kopie erhalten haben, falls nicht ist sie unter https://mit-license.org zu finden.")

time.sleep(5)
print("\nENDE")
u.logMssg("ENDE",0,0)

# ENDE
