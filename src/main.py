# QualityGame ist ein Spiel von Robin Ulke und Lloyd Bush, basierend auf den Büchern des Marc-Uwe Kling.
# Es ist frei unter https://www.github.com/lloydbush/QualityGame zu finden.
# Wir freuen uns auch zukünftig über Beteiligung am Projekt.
# Dieses Projekt steht unter der MIT-Lizenz.
# Mit dem source code dieses Spiels müsstest du eine Kopie erhalten haben, falls nicht ist sie unter https://mit-license.org zu finden.

import time
import os
from playsound import playsound

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
if c.DEBUG==1:
    print("\t\t\t!!! DEBUG MODE !!!\n")

# Variablen setzen
c.name=str(input("Dein Nachname:\t"))
c.vorname=str(input("Dein Vorname:\t"))
c.setUb(10) # setzt alle Werte von ub auf 10, also auch das durchschnittliche Level
c.setPunkte() # berechnet die Punkte
c.setLevel() # berechnet das Level

# Einführende Geschichte

# HAUPTSCHLEIFE
runde=0 # Zähler
while True:
    runde+=1 # Rundenanzähler inkrementieren
    playsound("media/message.mp3")

    c.update()
    print("###",runde)

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
    elif runde>=5: # maximale Rundenzahl erreicht
        break

# CLEANUP
playsound("media/game-over.mp3")

u.clear() # Terminal reinigen
u.logo()

# Stats anzeigen
print("Du hast")
print("Level",int(c.level),"erreicht")
print(int(c.punkte),"Punkte gesammelt")
print(runde,"Runden überlebt")
print()

# offene Enden aufheben
# Geschichte beenden
print("Du wirst von einer Bande nutzloser ermordet.")

if int(c.level >= 15):
    print("Sie werden in kurzer Zeit gefasst und verurteilt.")
else:
    print("Da dein Level zu niedrig war, hat die Polizei nach kurzer Zeit die Nachforschungen eingestellt.")

print()

# Abspann
#time.sleep(5)
input()

print("""
QualityGame ist ein Spiel von Robin Ulke und Lloyd Bush, basierend auf den Büchern des Marc-Uwe Kling.
Es ist frei unter https://www.github.com/lloydbush/QualityGame zu finden.
Wir freuen uns auch zukünftig über Beteiligung am Projekt.
Dieses Projekt steht unter der MIT-Lizenz.
Mit dem source code dieses Spiels müsstest du eine Kopie erhalten haben, falls nicht ist sie unter https://mit-license.org zu finden.
""")

input()

print("\nENDE")
u.logMssg("ENDE",0,0)

# ENDE
