# Modul statt Klasse

# PUBLIC
# get
def get_name():
    return __name

def get_vorname():
    return __vorname

# set
def set_name(new_name):
	__name=new_name
     
def set_vorname(new_vorname):
    __vorname=new_vorname

# PRIVATE
__name=""
__vorname=""
