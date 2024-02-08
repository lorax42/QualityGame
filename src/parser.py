# import os

# Tokens
LPAREN      ="("
RPAREN      =")"
QUALIF      ="???"
ADDPKT      ="+++"
DIGITS      ="0123456789"

# Parts
TEXT    =""
REQLEV  =0

# read file
def fread(file):
    global REQLEV
    file=open(file,"r")
    buf=file.read()

    for i,c in enumerate(buf):
        if c in QUALIF:
            if buf[i+1] in QUALIF and buf[i+2] in QUALIF:
                s_num=""
                for j,d in enumerate(buf,i):
                    if d in DIGITS:
                        s_num+=d
                REQLEV=int(s_num)
                
    file.close()

# Pfad zu Szenarien
# dir_path=os.path.dirname(os.path.abspath(__file__))+"/szenarien"
# 
# for root,dirs,files in os.walk(dir_path):
#     for file in files:
#         if file.endswith(".txt"):
#             print(root+"/"+str(file))
#             fread("szenarien/"+file)

fread("szenarien/szenarien.txt")