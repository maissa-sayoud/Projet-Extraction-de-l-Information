#Step 2
import re, sys

filee = open('infos2.txt','w+',encoding='utf-8')  #sans doublants (infos sur subst_corpus.dic)

fileee= open('infos3.txt','w+',encoding='utf-8')  #sans doublants (infos sur l'ensemble ({subst.dic}-{subs_corpus.dic}) )

fileC = open(sys.argv[1], 'r',encoding='UTF-8')   #corpus-medical.txt
lines_fileC = fileC.readlines()

fileDC = open('subst_corpus.dic', 'w', encoding='utf-16-le') #sans tri sans doublants
fileDC.write('\ufeff')

fileD = open('subst.dic', 'r', encoding='utf-16-le')
lines_fileD = fileD.readlines()
AncienD=[]
for m in lines_fileD:
    AncienD.append(m)
print(len(AncienD))


cpt=0
cptx=0

cptrouv=0
trouver=[0]

for line in (lines_fileC):
    #print("line",i)
    #cpt+=1
    
    x = re.search(r"^[-*Ø]?\s? ?(\w+) :? ?(\d+|,|\d+.\d)+ (g|mg|µg|mg\s|s|ml|-|flacon|sachet|amp|j|1/j|2/j|un|mcg|UI|iu|injection|cp|comprimé|gel|/).*", line, re.IGNORECASE)
    
    if x:
        #print(x)
        cptx+=1
        
        trouv=str(x.group(1).lower())
        #print(trouv)
        
        if trouv!='eau' and trouv!='hémoglobine' and trouv!='puis' and trouv!='a' and trouv!='ph' and trouv!='kcl' and trouv!='crp' and trouv!='b1' and trouv!='le' and trouv!='pendant' and trouv!='intraveineuse':
            true=0
            
            #dictionnaire de corpus-medical:
            fileDC.write(trouv)
            fileDC.write(",.N+subst\n")
            
            for t in trouver:    #eliminer les doublants
                #print("inside loop\n")
                if t==trouv:
                    true=1
                    #print("true")
                
            if true==0 :
                trouver.append(trouv)
                cptrouv+=1
                


# -> Pour l'enrichissement de subst.dic
trouve=[]
for line in lines_fileD:
    trouve.append(line)
print("len(subst.dic): ",len(trouve))

#-> Generer: infos2.txt
lettres=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cptLettres=0
del trouver[0]
trouver.sort()
for l in lettres:
    cptL=0
    for t in trouver:
        if t[0]==l:
            cptL+=1
            cptLettres+=1;
            #print(t)
            med=t+",.N+subst\n"
            filee.write(med)
            
            trouve.append(med)
            
    filee.write("------------------------------------------------------------------\nLe nombre de medicaments issus du corpus pour la lettre ")
    filee.write(l)
    filee.write(" est : ")
    filee.write(str(cptL))
    filee.write("\n------------------------------------------------------------------\n")
filee.write("------------------------------------------------------------------\nTotal= ")
filee.write(str(cptLettres))

#enrichir subst.dic
trouve.sort()
trouve=list(set(trouve))
lettrs=['a','b','c','d','e','é','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
fileD = open('subst.dic', 'w', encoding='utf-16-le')
fileD.write('\ufeff')
for l in lettrs:
    for t in trouve:
        if t[0]==l:
            fileD.write(t)

# -> Generer infos3.txt  
fileD = open('subst.dic', 'r', encoding='utf-16-le')
lines_fileD= fileD.readlines()

D=[]
DC=[]
for l in lines_fileD:
    D.append(l)
print("subst.dic= ",len(D),"\tN_medic_corpus= ",len(trouver) )

for t in trouver:
    DC.append(t+",.N+subst")


#print("DC=",len(DC))
intersection=[]
total=0
cptL=0
i=0
l=lettrs[i]
for t in DC:
    if t[0]!=l:
        fileee.write("------------------------------------------------------------------\nLe nombre de medicaments issus du corpus pour la lettre ")
        fileee.write(l)
        fileee.write(" est : ")
        fileee.write(str(cptL))
        fileee.write("\n------------------------------------------------------------------\n")
        cptL=0
        while t[0]!=l:
            i+=1
            l=lettrs[i]
            
    
    r=0
    #print(t)
    for d in AncienD:
        d=d.rstrip(d[-1])
        
        #print(d)
        if t==d:
            #print(t,d)
            intersection.append(t) 
            r=1
    if r==0:
        cptL+=1
        total+=1
        fileee.write(t)
        fileee.write("\n")
fileee.write("------------------------------------------------------------------\nLe nombre de medicaments issus du corpus pour la lettre ")
fileee.write(l)
fileee.write(" est : ")
fileee.write(str(cptL))
fileee.write("\n------------------------------------------------------------------\nTotal= ")
fileee.write(str(total))
fileee.write("\n------------------------------------------------------------------")

print(len(intersection))
#print (DC)
#la liste "D" contient les medicaments du "subst.dic" apres l'enrichissement
#la liste "DC" contient les medicaments trouvés dans corpus



#print("trouver: \n",len(trouver))
#print("trouve:\n",len(trouve))

#print(trouve)

#print("liste:",trouver)

#print(type(x))  

#print(trouver)

print(">>Resultats\nx= ",cptx)
print("N_trouv= ",cptrouv)
