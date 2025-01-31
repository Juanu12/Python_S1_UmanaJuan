import secrets
import string
letras = string.ascii_letters
num =string.digits
spch=string.punctuation

ch = letras,num,spch
pss_length=1
pss = ""

for i in range (pss_length):
    pss = "".join(secrets.choice(ch *10))
    print (pss) 
    
 