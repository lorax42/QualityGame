import time
import random

import utils as u

# Attribute
name=""
vorname=""
punkte=0
level=0

# UNTERBERREICHE
# die Punkte sind die Summe aller Punkte in ub und gUb punkte=(sumUb()+sunGUb())
# 42 bekannte Unterberreiche
ub={
    "flexibilität":0,
    "belastbarkeit":0,
    "innovativität":0,
    "kreativität":0,
    "teamfähigkeit":0,
    "begeisterungsfähigkeit":0,
    "geschmack":0,
    "vernetzung":0,
    "alter":0,
    "wohnort":0,
    "job":0,
    "einkommen":0,
    "gesundheit":0,
    "vermögen":0,
    "beziehungen":0,
    "sozialkompetenz":0,
    "arbeitsfreude":0,
    "bildung":0,
    "iq":0,
    "eq":0,
    "zuverlässigkeit":0,
    "sportlichkeit":0,
    "produktivität":0,
    "humor":0,
    "sexappeal":0,
    "bmi":0,
    "ausstattung":0,
    "pünktlichkeit":0,
    "freunde":0,
    "gene":0,
    "familiäre_krankheitsgeschichte":0,
    "lebenserwartung":0,
    "anpassungsfähigkeit":0,
    "mobilität":0,
    "kritikfähigkeit":0,
    "auslandserfahrung":0,
    "antwortrate":0, # und -rate in sozialen Netzwerken
    "konsumaufgeschlossenheit":0,
    "stressresistenz":0,
    "disziplin":0,
    "selbstvertrauen":0,
    "tischmanieren":0
}

# 58 geheime Unterbereiche
gUb={
    "x43":0,
    "x44":0,
    "x45":0,
    "x46":0,
    "x47":0,
    "x48":0,
    "x49":0,
    "x50":0,
    "x51":0,
    "x52":0,
    "x53":0,
    "x54":0,
    "x55":0,
    "x56":0,
    "x57":0,
    "x58":0,
    "x59":0,
    "x60":0,
    "x61":0,
    "x62":0,
    "x63":0,
    "x64":0,
    "x65":0,
    "x66":0,
    "x67":0,
    "x68":0,
    "x69":0,
    "x70":0,
    "x71":0,
    "x72":0,
    "x73":0,
    "x74":0,
    "x75":0,
    "x76":0,
    "x77":0,
    "x78":0,
    "x79":0,
    "x80":0,
    "x81":0,
    "x82":0,
    "x83":0,
    "x84":0,
    "x85":0,
    "x86":0,
    "x87":0,
    "x88":0,
    "x89":0,
    "x90":0,
    "x91":0,
    "x92":0,
    "x93":0,
    "x94":0,
    "x95":0,
    "x96":0,
    "x97":0,
    "x98":0,
    "x99":0,
    "x100":0
}

# Methoden
def addPunkte(i,num):
    global ub
    try:
        ub[i]+=num
    except:
        u.logMssg("ERROR: undefinierter index="+str(i),1,1)
        return 1

    if num >= 0:
        print("### +%d Punkte in %s ###" %(num,i))
    elif num < 0:
        print("### %d Punkte in %s ###" %(num,i))
    else:
        u.logMssg("ERROR: undefinierte Zahl="+num,1,1)
        return 1
    
    time.sleep(2)
    
    return 0

# setzt Punkte auf die Summe der Werte in ub und gUb
def setPunkte():
    global punkte

    punkte=sumUb()+sumGUb()
    
    return 0

# setzt alle Werte in ub auf num
def setUb(num):
    global ub
    num=int(num)
    
    for i in ub:
        ub[i]=num
    
    return 0

# gibt den Durchschnitt von ub wieder
def avgUb():
    global ub

    return sumUb()/len(ub)

# setzt alle Werte in gUb auf den Durchschnitt von ub
def setGUb():
    global ub,gUb
    avg=avgUb()

    for i in gUb:
        gUb[i]=avg
    
    return 0

# gibt die Summe aller Werte in ub wieder
def sumUb():
    global ub
    total=0
    
    for i in ub:
        total+=ub[i]
    
    return total

# gibt die Summe aller Werte in gUb wieder
def sumGUb():
    global gUb
    total=0
    
    for i in gUb:
        total+=gUb[i]
    
    return total

# berechnet das Level
def setLevel():
    global level,ub
    
    setGUb()
    level=(sumUb()+(random.randint(95,105)/100)*sumGUb())/100
    # level = UB + rand*GeheimUB / 100

    return 0

def levelUp(level):
    print("+++ Du bist Aufgestiegen!!! +++\nDir stehen neue Türen offen...")

def levelDown(level):
    print("--- Du bist Abgestiegen!!! ---\nDas wirst du auf ewig bereuen...")

def levelStay(level):
    print("=== Du bist gleich geblieben!!! ===\nDas ist fast so schlimm, wie Abstieg... du willst mehr!")

def update():
    clevel=level

    u.clear() # Terminal reinigen
    setPunkte() # berechnet die Punkte neu
    setLevel() # berechnet das Level neu

    # Situation anzeigen
    print(vorname,name)
    print("Level:",int(level))
    print("Punkte:",punkte)
    # print("###",runde)
    print()

    if int(clevel) < int(level):
        levelUp(level)
    
    elif int(clevel) > int(level):
        levelDown(level)
    
    else:
        levelStay(level)
    

    print()