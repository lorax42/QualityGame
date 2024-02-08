import random

import charakter as c
import utils as u
import main as m

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

def checkSzenError(x,sID,wahl):
    if x==0:
        return 0
    elif x==1:
        errorSzenario(sID,wahl)
    else:
        undefError(sID,x)

# zufällige Szenarienwahl
def szenario():
    sID=0 # szenario ID

    szenarien=[szenario1,szenario2] # liste der Szenarien
    szen=random.choice(szenarien) # szen ist ein zufälliges Szenario
    x=szen() # szen wird ausgeführt
    
    # Error checking
    if x==0:
        return 0
    elif x==1:
        errorSzenario(sID,szen)
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
        x=c.addPunkte("disziplin",-5)
    elif wahl==2:
        x=c.addPunkte("gesundheit",-3)
    elif wahl==3:
        x=c.addPunkte("antwortgeschwindigkeit",5)
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




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # #   # #   #         #   # # # #   # # # # #     # # # #   # # #   # #     # #       # #   # # # #       # #   # # # 
# # #   # #   #   # # # #   # # # #   # # # #   # #   # # #   # # #   #   # #   #   # #   #   # # # #   # #   #   # # # 
# # #         #       # #   # # # #   # # # #   # #   # # #   # # #   #   # #   #   # #   #   # # # #   # #   #   # # # 
# # #   # #   #   # # # #   # # # #   # # # #   # #   # # #   #   #   #   # #   #       # #   # # # #   # #   #   # # # 
# # #   # #   #   # # # #   # # # #   # # # #   # #   # # #     #     #   # #   #   # #   #   # # # #   # #   # # # # # 
# # #   # #   #         #         #         # #     # # # #   # # #   # #     # #   # #   #         #       # #   # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Szenario 2 ##########################################################################################################
def szenario2():

    sID=2 # szenario ID
    if c.level<2:
        return 2

    print("""
Du sitzt wie so oft in Deiner viel zu kleinen Büroeinheit und gehst Deiner sinnlosen Arbeit nach: [kreatives Einfügen]
Plötzlich vibriert Dein QualityPad und leuchtet auf, sodass Dein Blick zu ihm gleitet: eine neue Nachricht
1) Weiterarbeiten
2) Öffnen
    """)

    wahl1=int(input("> "))
    u.update(m.runde)

    if wahl1==1:

        x=c.addPunkte("produktivität",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("antwortrate",-30)
        checkSzenError(x,sID,wahl1)

        print("""
Weiterarbeiten (+Produktivität; -Antw-rate i. soz. Med.):
Du lässt Dich nicht beirren und drehst Dein QualityPad herum, sodass Dich das Leuchten nicht mehr ablenken kann.
Mit neuem, entschlossenerem Tatendrang wendest Du Dich wieder Deiner Arbeit zu.
Aber bist Du Dir da so sicher? Vielleicht hat Deine Nachbarin einen neuen Wellensittich und wenn Du jetzt nicht nachschaust
wirst Du es als letztes erfahren!
Vielleicht sind es aber auch nur Deine Eltern, die wissen wollen wie es Dir geht….
1) QualityPad doch öffnen
2) endlich weiterarbeiten!
        """)

        wahl2=int(input("> "))
        u.update(m.runde)

        if wahl2==1:

            x=c.addPunkte("antwortrate",30)
            checkSzenError(x,sID,wahl2)

            x=c.addPunkte("produktivität",-50)
            checkSzenError(x,sID,wahl2)

            print("""
Öffnen (+Antw.rate i. soz. Med.; -Produktivität):
Du nimmst das QualityPad und öffnest die Nachricht - irgendetwas auf Everybody.
Nach einem kurzen Moment öffnet sich die App und Du kannst den Text der Nachricht lesen:
“heute gemüseauflauf! nice!”. Wieder irgend so ein Thermomixer… Du schüttelst genervt den Kopf.
-
Gerade willst Du Dich wieder deiner Arbeit zuwenden, als Dir Werbung für die neuen Low-Fett Zuckerfesazus angezeigt wird.
Mhm… ein wenig Hunger hast Du ja schon. Und nun auch wesentlich gesünder!
1) Die Fesazus bestellen
2) endlich weiterarbeiten!
            """)

            wahl3=int(input("> "))
            u.update(m.runde)

            if wahl3==1:

                x=c.addPunkte("konsumaufgeschlossenheit",50)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("geschmack",-20)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("gesundheit",-20)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("sexappeal",-10)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("bmi",-10)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("lebenserwartung",-10)
                checkSzenError(x,sID,wahl3)

                print("""
Die Fesazus bestellen (+Aufgeschl. gg. neuen Kons.angeb; .-Geschmack; -Gesundheit; -Sexappeal; -BMI; -Lebenserwartung):
Du bestellst die Fesazus und wartest ungeduldig die zehn Sekunden, bis die Lieferdrohne an
Deinem Bürofenster angekommen ist, ehe Du Dich genüsslich über die Snacks hermachst. …
                """)

                input()
                u.update(m.runde)

            elif wahl3==2:

                x=c.addPunkte("produktivität",20)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("konsumaufgeschlossenheit",-40)
                checkSzenError(x,sID,wahl3)

                print("""
endlich weiterarbeiten! (+Produktivität; -Aufgeschl. gg. neuen Kons.angeb.):
Du schüttelst den Kopf: “Wie kann nur so ungesund leben?!”.
So bleibst Du eisern und verfällst nicht der Versuchung, sondern kümmerst Dich weiter um Deinen Job.
-
”Ha, nieder mit dieser Konsumgesellschaft!” Du lachst. Plötzlich aber hälst Du inne - hast Du das gerade laut gedacht?
Und hast Du gerade vor der Kamera Deines Computers (und eigentlich aller elektrischen Geräte
in diesem Zimmer - wozu braucht ein Toaster [passenderes Büroequipment!] eigentlich eine Kamera?) die Faust geregt?
Schnell wendest Du Dich wieder Deiner Arbeit zu.	
                """)

                input()
                u.update(m.runde)
            
            else:
                errorWahlSzenario(sID,wahl3)
                return 1
        
        elif wahl2==2:

            x=c.addPunkte("produktivität",10)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("antwortrate",-20)
            checkSzenError(x,sID,wahl3)

            print("""
endlich weiterarbeiten!(+Produktivität; -Antw-rate i. soz. Med.):
Du schüttelst den Kopf und bleibst eisern.
Auch wenn die Versuchung schon groß ist….
            """)

            input()
            u.update(m.runde)

        else:
            errorWahlSzenario(sID,wahl2)
            return 1


    elif wahl1==2:

        x=c.addPunkte("antwortrate",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("produktivität",-30)
        checkSzenError(x,sID,wahl1)

        print("""
Öffnen (+Antw.rate i. soz. Med.; -Produktivität):
Du nimmst das QualityPad und öffnest die Nachricht - irgendetwas auf Everybody.
Nach einem kurzen Moment öffnet sich die App und Du kannst den Text der Nachricht lesen: “heute gemüseauflauf! nice!”.
Wieder irgend so ein Thermomixer… Du schüttelst genervt den Kopf.
-
Gerade willst Du Dich wieder deiner Arbeit zuwenden, als Dir Werbung für die neuen Low-Fett Zuckerfesazus angezeigt wird.
Mhm… ein wenig Hunger hast Du ja schon. Und nun auch wesentlich gesünder!
1) Die Fesazus bestellen
2) endlich weiterarbeiten!
        """)

        wahl3=int(input("> "))
        u.update(m.runde)

        if wahl3==1:

            x=c.addPunkte("konsumaufgeschlossenheit",50)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("geschmack",-20)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("gesundheit",-20)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("sexappeal",-10)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("bmi",-10)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("lebenserwartung",-10)
            checkSzenError(x,sID,wahl3)

            print("""
Die Fesazus bestellen (+Aufgeschl. gg. neuen Kons.angeb; .-Geschmack; -Gesundheit; -Sexappeal; -BMI; -Lebenserwartung):
Du bestellst die Fesazus und wartest ungeduldig die zehn Sekunden, bis die Lieferdrohne an
Deinem Bürofenster angekommen ist, ehe Du Dich genüsslich über die Snacks hermachst. …
                """)

            input()
            u.update(m.runde)

        elif wahl3==2:

            x=c.addPunkte("produktivität",20)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("konsumaufgeschlossenheit",-40)
            checkSzenError(x,sID,wahl3)

            print("""
endlich weiterarbeiten! (+Produktivität; -Aufgeschl. gg. neuen Kons.angeb.):
Du schüttelst den Kopf: “Wie kann man nur so ungesund leben?!”.
So bleibst Du eisern und verfällst nicht der Versuchung, sondern kümmerst Dich weiter um Deinen Job.
-
”Ha, nieder mit dieser Konsumgesellschaft!” Du lachst. Plötzlich aber hälst Du inne - hast Du das gerade laut gedacht?
Und hast Du gerade vor der Kamera Deines Computers (und eigentlich aller elektrischen Geräte
in diesem Zimmer - wozu braucht ein Toaster [passenderes Büroequipment!] eigentlich eine Kamera?) die Faust geregt?
Schnell wendest Du Dich wieder Deiner Arbeit zu.	
                """)

            input()
            u.update(m.runde)
            
        else:
            errorWahlSzenario(sID,wahl3)
            return 1

    else:
        errorWahlSzenario(sID,wahl1)
        return 1

# Szenario 3 ##########################################################################################################
