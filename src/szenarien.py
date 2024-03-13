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

    szenarien=[szenario1,szenario2,szenario3] # liste der Szenarien
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
        x=c.addPunkte("disziplin",-10)
        checkSzenError(x,sID,wahl)
    elif wahl==2:
        x=c.addPunkte("gesundheit",-30)
        checkSzenError(x,sID,wahl)
    elif wahl==3:
        x=c.addPunkte("antwortrate",50)
        checkSzenError(x,sID,wahl)
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
    c.update()

    if wahl1==1:

        x=c.addPunkte("produktivität",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("antwortrate",-30)
        checkSzenError(x,sID,wahl1)

        print("""
Weiterarbeiten:
Du lässt Dich nicht beirren und drehst Dein QualityPad herum, sodass Dich das Leuchten nicht mehr ablenken kann.
Mit neuem, entschlossenerem Tatendrang wendest Du Dich wieder Deiner Arbeit zu.
Aber bist Du Dir da so sicher? Vielleicht hat Deine Nachbarin einen neuen Wellensittich und wenn Du jetzt nicht nachschaust
wirst Du es als letztes erfahren!
Vielleicht sind es aber auch nur Deine Eltern, die wissen wollen wie es Dir geht….
1) QualityPad doch öffnen
2) endlich weiterarbeiten!
        """)

        wahl2=int(input("> "))
        c.update()

        if wahl2==1:

            x=c.addPunkte("antwortrate",30)
            checkSzenError(x,sID,wahl2)

            x=c.addPunkte("produktivität",-50)
            checkSzenError(x,sID,wahl2)

            print("""
Öffnen:
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
            c.update()

            if wahl3==1:

                x=c.addPunkte("konsumaufgeschlossenheit",30)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("geschmack",-25)
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
Die Fesazus bestellen:
Du bestellst die Fesazus und wartest ungeduldig die zehn Sekunden, bis die Lieferdrohne an
Deinem Bürofenster angekommen ist, ehe Du Dich genüsslich über die Snacks hermachst. …
                """)

                input()
                c.update()

            elif wahl3==2:

                x=c.addPunkte("produktivität",20)
                checkSzenError(x,sID,wahl3)

                x=c.addPunkte("konsumaufgeschlossenheit",-40)
                checkSzenError(x,sID,wahl3)

                print("""
Endlich weiterarbeiten!:
Du schüttelst den Kopf: “Wie kann nur so ungesund leben?!”.
So bleibst Du eisern und verfällst nicht der Versuchung, sondern kümmerst Dich weiter um Deinen Job.
-
”Ha, nieder mit dieser Konsumgesellschaft!” Du lachst. Plötzlich aber hälst Du inne - hast Du das gerade laut gedacht?
Und hast Du gerade vor der Kamera Deines Computers (und eigentlich aller elektrischen Geräte
in diesem Zimmer - wozu braucht ein Toaster [passenderes Büroequipment!] eigentlich eine Kamera?) die Faust geregt?
Schnell wendest Du Dich wieder Deiner Arbeit zu.	
                """)

                input()
                c.update()
            
            else:
                errorWahlSzenario(sID,wahl3)
                return 1
        
        elif wahl2==2:

            x=c.addPunkte("produktivität",10)
            checkSzenError(x,sID,wahl2)

            x=c.addPunkte("antwortrate",-20)
            checkSzenError(x,sID,wahl2)

            print("""
endlich weiterarbeiten!:
Du schüttelst den Kopf und bleibst eisern.
Auch wenn die Versuchung schon groß ist….
            """)

            input()
            c.update()

        else:
            errorWahlSzenario(sID,wahl2)
            return 1


    elif wahl1==2:

        x=c.addPunkte("antwortrate",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("produktivität",-30)
        checkSzenError(x,sID,wahl1)

        print("""
Öffnen:
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
        c.update()

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
Die Fesazus bestellen:
Du bestellst die Fesazus und wartest ungeduldig die zehn Sekunden, bis die Lieferdrohne an
Deinem Bürofenster angekommen ist, ehe Du Dich genüsslich über die Snacks hermachst. …
                """)

            input()
            c.update()

        elif wahl3==2:

            x=c.addPunkte("produktivität",20)
            checkSzenError(x,sID,wahl3)

            x=c.addPunkte("konsumaufgeschlossenheit",-40)
            checkSzenError(x,sID,wahl3)

            print("""
endlich weiterarbeiten!:
Du schüttelst den Kopf: “Wie kann man nur so ungesund leben?!”.
So bleibst Du eisern und verfällst nicht der Versuchung, sondern kümmerst Dich weiter um Deinen Job.
-
”Ha, nieder mit dieser Konsumgesellschaft!” Du lachst. Plötzlich aber hälst Du inne - hast Du das gerade laut gedacht?
Und hast Du gerade vor der Kamera Deines Computers (und eigentlich aller elektrischen Geräte
in diesem Zimmer - wozu braucht ein Toaster [passenderes Büroequipment!] eigentlich eine Kamera?) die Faust geregt?
Schnell wendest Du Dich wieder Deiner Arbeit zu.	
                """)

            input()
            c.update()
            
        else:
            errorWahlSzenario(sID,wahl3)
            return 1

    else:
        errorWahlSzenario(sID,wahl1)
        return 1

# Szenario 3 ##########################################################################################################

def szenario3():
    sID=3 # szenario ID
    if c.level<2:
        return 2
    
    
        
    
    

    print("""
Du hockst wie so oft daheim auf der Couch, als die Sendung, die Du gerade siehst, von Werbung unterbrochen wird.
Unter anderem der des neuen Fitnessstudios. Hm… gut, ein bisschen Sport täte Dir sicher nicht schlecht!
Andererseits ist die Couch auch so bequem…
1) liegen bleiben
2) Ab ins Gym!
    """)

    wahl1=int(input("> "))
    c.update()

    if wahl1==1:
        x=c.addPunkte("gesundheit",-100)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("sportlichkeit",-50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("disziplin",-50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("produktivität",-20)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("bmi",-20)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("sexappeal",-10)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("lebenserwartung",-10)
        checkSzenError(x,sID,wahl1)


        print("""
So bleibst Du also lieber entspannt in der Couch hängen, statt etwas Sport zu treiben - fauler Sack!
        """)

    elif wahl1==2:

        x=c.addPunkte("lebenserwartung",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("produktivität",50)
        checkSzenError(x,sID,wahl1)
        
        print("""
Mit ein bisschen Selbstdisziplin stemmst Du Dich aus der Couch und begibst Dich auf den Weg zum Fitnessstudio.
Vor der Haustüre erwartet Dich bereits eine Passagierdrohne, schnellst huschst Du aus der Eingangstüre des Hauses in diese,
um der prallen, glühend heißen Sonne zu entgehen.
Der Klimawandel. Wer hätte denn auch ahnen können, dass das noch so schlimm wird?!
-
Im Fitnessstudio angekommen, machst Du das, was man in einem Fitnessstudio eben so macht… Sport. Und das klappt auch ganz gut!
… wenn man eine Horde visueller Zombies im Rücken hat.
        """)

        input()
        c.update()


        x=c.addPunkte("sportlichkeit",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("sexappeal",50)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("gesundheit",20)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("lebenserwartung",20)
        checkSzenError(x,sID,wahl1)

        x=c.addPunkte("bmi",10)
        checkSzenError(x,sID,wahl1)

        c.update()

    else:
        errorWahlSzenario(sID,wahl1)
        return 1
    
    return 0

# Szenario 4 ##########################################################################################################

def szenario4():
    sID=3 # szenario ID
    if c.level<2:
        return 2


    print("""
Auf der Suche nach einem Abendessen schlenderst Du durch die Straßen von Quality City.
- Das ist natürlich quatsch. Wer schlendert denn bitteschön noch durch Straßen, um ein Restaurant zu suchen?
Dein Ohrwurm hat Dir eine Adresse mit einem Deinem Geschmack und Deinem Kontostand entsprechenden Etablissement ausgegeben, zu der Dich nun eines der selbstfahrenden Autos fährt.
-
Als Du aus dem Fenster blickst, siehst Du ein schickes und teuer aussehendes Level-40 Restaurant. Beneidenswert - aber so teuer wie es aussieht, ist es auch und mit Deinem Level kommst Du da eh nicht rein.
-
Du kommst an und steigst aus dem Auto aus - welches Dich gar nicht um eine Bewertung bittet?
Das muss der letzte Levelaufstieg mitgebracht haben, Nice!
Du willst gerade das Restaurant betreten, als Dein Blick ein paar Häuserfassaden weiter auf ein anderes, neues fällt. Ein im Vergleich zu diesem hier doch deutlich schickeres! … aber auch nur für Level %d. Und entsprechend Teuer - also eigentlich nichts für Deinen begrenztes Konto. Eigentlich…
1) In das für Dich empfohlene Restaurant gehen
2) Dir heute mal etwas gönnen!
    """ %(int(c.level)))

    wahl=int(input("> "))
    c.update()

    if wahl==1:

        x=c.addPunkte("disziplin",50)
        checkSzenError(x,sID,wahl)

        x=c.addPunkte("zuverlässigkeit",50)
        checkSzenError(x,sID,wahl)

        print("""
In das für Dich empfohlene Restaurant gehen:
Du betrittst also das Restraurant und setzt Dich an einen freien Tisch. Der Roboter-Kellner bringt Dir auch sogleich das zu Dir passendste Gericht - Surstömming. Wie kommt das System nur darauf?! 
Naja, inzwischen konntest Du Dich immerhin daran gewöhnen… und irgendwo schmeckt es ja sogar! Vielleicht. Aber das System wird schon recht haben.
        """)

    elif wahl==2:

        x=c.addPunkte("begeisterungsfähigkeit",50)
        checkSzenError(x,sID,wahl)

        x=c.addPunkte("konsumaufgeschlossenheit",50)
        checkSzenError(x,sID,wahl)

        x=c.addPunkte("geschmack",50)
        checkSzenError(x,sID,wahl)

        x=c.addPunkte("vermögen",50)
        checkSzenError(x,sID,wahl)

        print("""
Dir heute mal etwas gönnen!:
Du betrittst also das Restraurant und setzt Dich an einen freien Tisch. Der Roboter-Kellner bringt Dir auch sogleich das zu Dir passendste Gericht - Surstömming. Wie kommt das System nur darauf?! 
Naja, inzwischen konntest Du Dich immerhin daran gewöhnen… und irgendwo schmeckt es ja sogar! Vielleicht. Aber das System wird schon recht haben.
        """)

    else:
        errorWahlSzenario(sID,wahl)
        return 1
    
    return 0
