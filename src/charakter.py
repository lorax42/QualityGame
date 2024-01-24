import time

import utils as u

# Attribute
name=""
vorname=""
punkte=0
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
    
    return 0
