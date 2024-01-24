import datetime
import os

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
        #print("ERROR: undefinierter Systemtyp: ",os.name)
        logMssg("ERROR: undefinierter Systemtyp: "+os.name,1,1)
        return 1