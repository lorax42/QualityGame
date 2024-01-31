# import random
# 
# import charakter as c
# import utils as u
# 
# # ERROR: undefinierte Wahl eines Szenarios
# def errorWahlSzenario(szenario,wahl):
#     u.logMssg("ERROR: undefinierte Wahl eines Szenarios\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
#     return 0
# 
# def errorSzenario(szenario,wahl):
#     u.logMssg("ERROR: in einem Szenario\nSzenario="+str(szenario)+"\nwahl="+str(wahl),1,1)
#     return 0
# 
# def undefError(szenario,error):
#     u.logMssg("ERROR: undefinierter error in Szenario="+str(szenario),error,1)
#     return 0
# 
# def unqualError(szenario,wahl):
#     u.logMssg("ERROR: in Szenario="+str(szenario)+"\nunqualifiziert für Szenario="+str(wahl),2,0)
#     return 0
# 
# 
# # zufällige Szenarienwahl
# def szenario():
#     szenName=0 # szenario Codenummer
#     numSzenario=2 # Anzahl der Szenarien
#     wahl=random.randint(0,100000)%numSzenario
#     wahl+=1 # 0 ist szenario(), 1 ist szenario1() ...
# 
#     if wahl==1:
#         x=szenario1()
#     elif wahl==2:
#         x=szenario2()
#     # elif wahl==3:
#         # x=szenario3()
#     else:
#         errorWahlSzenario(szenName,wahl)
#         return 1
#     
#     # Error checking
#     if x==0:
#         return 0
#     elif x==1:
#         errorSzenario(szenName,wahl)
#         return 1
#     elif x==2: # für dieses Szenario unqualifiziert
#         unqualError(szenName,wahl)
#         szenario()
#         return 0
#     else:
#         undefError(szenName,x)
#         return 1
#     
#     return 0
# 
# ###SZENARIEN###
# 
# # Szenario 1
# def szenario1():
#     if c.level<2:
#         return 2
#     
#     print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
#     wahl=int(input("> "))
# 
#     if wahl==1:
#         x=c.addPunkte(-5)
#     elif wahl==2:
#         x=c.addPunkte(-3)
#     elif wahl==3:
#         x=c.addPunkte(5)
#     else:
#         errorWahlSzenario("szenario1",wahl)
#         return 1
#     
#     if x==0:
#         return 0
#     elif x==1:
#         errorSzenario("szenario1",wahl)
#     else:
#         undefError("szenario1",x)
#     
#     return 0
# 
# ### FÜR DEBUGGING ###
# 
# # Szenario 2
# def szenario2():
#     if c.level<2:
#         return 2
#     
#     print("Du kommst nach Hause. Was machst du?\n1) Dich entspannen und Chips essen\n2) An Deinem Buch weiterschreiben\n3) Dein Everyone Profil updaten")
#     wahl=int(input("> "))
# 
#     if wahl==1:
#         x=c.addPunkte(-5)
#     elif wahl==2:
#         x=c.addPunkte(-3)
#     elif wahl==3:
#         x=c.addPunkte(5)
#     else:
#         errorWahlSzenario("szenario1",wahl)
#         return 1
#     
#     if x==0:
#         return 0
#     elif x==1:
#         errorSzenario("szenario1",wahl)
#     else:
#         undefError("szenario1",x)
#     
#     return 0

### Sinnvoll

#
# level : int
# name : str
# vorname : str
# punkte : int
# scenario : [scene]
#

import utils as u
import charakter as c

class scenario:
    scenes = []

    def __init__(self, file, title):
        # loading
        self.title = title
    
    def call(self):
        for x in self.scenes:
            u.clear()
            print(self.title)
            x.call()
            c.level = c.calcLevel()
        