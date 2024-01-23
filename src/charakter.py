# Charakter als Modul (statt Klasse)

import time

# Attribute
name=""
vorname=""
punkte=0
level=0

# Methoden
def addPunkte(num):
    global punkte
    punkte+=num

    if num >= 0:
        print("### +%d Punkte ###" %(num))
    else:
        print("### %d Punkte ###" %(num))
    time.sleep(2)

