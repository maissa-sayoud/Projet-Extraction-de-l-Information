import re
import sqlite3
import string

file = open("corpus-medical_snt/concord.html","r",encoding="UTF-8")
contenuH = file.read()
print(contenuH)

posologies =[]
posologies = re.findall(r"<a href=\"[0-9 ]+\">.+</a>",contenuH)
#print(posologies)

#print (len(posologies))
for i in range(len(posologies)):
    #print (posologies[i])
    posologies[i] = re.findall(r">.+<",posologies[i])[0][1:-1]
    #print (posologies[i])
    
inst = sqlite3.connect("extraction.db")

inst.execute("CREATE TABLE POSOLOGIES (ID INTEGER PRIMARY KEY , Posologie TEXT)")

i=1
for p in posologies:
    print(i,p)
    inst.execute("INSERT INTO POSOLOGIES VALUES (?,?)",(str(i),p))
    i+=1

inst.commit()

inst.close()
