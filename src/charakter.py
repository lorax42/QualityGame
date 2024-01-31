import time

import utils as u

# Attribute
name=""
vorname=""
punkte=0 # SUMME UB!
level=0

# Unterbereiche
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
    "antwortgeschwindigkeit":0, # und -rate in sozialen Netzwerken
    "konsumaufgeschlossenheit":0,
    "stressresistenz":0,
    "disziplin":0,
    "selbstvertrauen":0,
    "tischmanieren":0
}
# Methoden
def addPunkte(num):
    global punkte
    punkte+=num

    if num >= 0:
        print("### +%d Punkte ###" %(num))
    elif num < 0:
        print("### %d Punkte ###" %(num))
    else:
        u.logMssg("EEROR: undefinierte Zahl="+num,1,1)
        return 1
    
    time.sleep(2)
    # Utils
    return 0

# setzt alle Unterbereiche in ub auf eine Punktzahl num
def setAllUb(num):
    global ub

    for i in ub:
        ub[i]=num
    
    return 0

# gibt Summe der Punkte des Inputs
def sumUb():
    global punkte,ub
    punkte=0

    for i in ub:
        punkte+=ub[i]
    
    return 0

# berechnet Level durch Punktzahl in ub
def calcLevel():
    global level,ub,punkte

    level=len(ub)/100 *punkte+ (1000-len(ub))/100 *punkte # berechnet Level aus Punkten
    # level = 0.42  *  total Pkt.     +      0.58   *   total Pkt.

    level=10

    return 0