import datetime
import os

import charakter as c

# Lognachricht schreiben
def logMssg(message,error,p):
    message=str(message)
    error=str(error)
    p=int(p)
    if p!=0:
        print(message)
    log=open(r"log.txt","a") # log Datei öffnen
    if log:
        log.write(str(datetime.datetime.now())+"\n")
        log.write(message+"\nerror="+error+"\n\n")
    else:
        print("ERROR: Logdatei konnte nicht gefunden werden")
        return 1
    log.close() # log Datei schließen

    return 0

# Terminal reinigen
def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    elif os.name == 'posix':
        _ = os.system('clear')
    
    else:
        logMssg("ERROR: undefinierter Systemtyp: "+os.name,1,1)
        return 1

def update(runde):
    clear() # Terminal reinigen
    c.setPunkte() # berechnet die Punkte neu
    c.setLevel() # berechnet das Level neu
    
    # Situation anzeigen
    print(c.vorname,c.name)
    print("Level:",int(c.level))
    print("Punkte:",c.punkte)
    print("###",runde)
    print()

def logo():
    print(r"""
 ______                                ______
/|     \              ||     ||       /|     \
||     |        ____  || || ||||      ||        ____   ___  __   ___
||  _  | ||  | /|  |\ ||     ||       ||   __  /|  |\ ||  \/  | /|__\
||  \\ | ||  | ||  || || ||  || \\  / ||     | ||  || ||  ||  | ||  
\|___\\/ \|__/ \|__|| \| \|  \|  \\/  \|_____/ \|__|| ||  ||  | \|__/
______\\_________________________//__________________________________
___Lloyd Bush und Robin Ulke____//_______(c) 2024 MIT-License________
""")
    return 0