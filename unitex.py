#step3

# Le fichier d’alphabet Alphabet.txt est un fichier texte qui décrit tous les caractères d’une langue!
# Il est important de le rajouter pour que Unitex puisse faire la difference entre les differents caracteres d'une langue
# Par exemple les caracteres de la langue arabe sont differents de ceux de la langue française,
# Et donc, pour pouvoir demarrer un traitement sur unitex il faudra bien le rajouter pour la reconnaissance des lettres,
#  d'où les mots.


import os
from os import path

if path.exists("corpus-medical_snt"):
    os.system("rd /s corpus-medical_snt")


os.mkdir("corpus-medical_snt")


os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt Dela_fr.bin subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posolgie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posolgie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55") 

