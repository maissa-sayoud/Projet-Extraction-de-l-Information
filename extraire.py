#Step1 : 

import sys
import requests
from bs4 import BeautifulSoup


# - gerer l'intervalle (1er argument):
def range_char(debut, fin):
    return (chr(n) for n in range(ord(debut), ord(fin) + 1))

lettre=sys.argv[1]

#lettre est de la sorte : 'A-Z'
a=lettre[0]
b=lettre[2]


# fonction d'extraction & du traitement du code html :
def ExtraireHtml(link):

    content= requests.get(link)

    bloc= BeautifulSoup(content.text, "html.parser")
    #print(bloc)
    
    indice=character.lower()
    #print(indice)
    sousBloc=bloc.find('ul',{"id":f"letter{indice}"})
    
    medBloc=sousBloc.find_all('a')
    #print (len(medBloc))
    
    medic=[]
    #print (type(medic))
    for i in range (len(medBloc)):
        medic=medic+[medBloc[i].text]
    #print (medic)
    
    t=0
    for m in medic:
        t=t+1;
        #d=m+",.N+subst"
        #print(d)
        file.write(m+",.N+subst")
        file.write("\n")
    #print("\n")
    #print(">>> fin de la page: ",character)
    
    filee.write("Total de ")
    filee.write(character)
    filee.write(" est : ")
    filee.write(str(t))
    filee.write("\n")
    print(character, " >> success ! \n")
    return t


#creer le fichier subst.dic (UTF-16 LE avec BOM (UCS-2 LE BOM)) & infos1.txt ():   
file= open("subst.dic",'w',encoding='utf-16-le')
file.write('\ufeff')    #BOM

filee= open('infos1.txt','w+',encoding='utf-8')

    
# - gerer le port (2eme argument) :  
port=sys.argv[2]
#print (port)

# - generer le lien d'une page:
#lien=f"http://127.0.0.1:{port}/vidal/vidal-Sommaires-Substances-{lettre}.html"
#                          *                                         *
#http://127.0.0.1:80/vidal/vidal-Sommaires-Substances-A.html"

Total=0

#Generer tous les liens de l'intervalle specifié dans argv[1]
for character in range_char(a, b):
    #print(character)
    lien=f"http://127.0.0.1:{port}/vidal/vidal-Sommaires-Substances-{character}.html"
    #print(lien)
    cpt=(ExtraireHtml(lien))
    Total=Total+cpt

#print (Total)

file.close()

filee.write("Nombre total des substances actives : ")
filee.write(str(Total))

filee.close()
