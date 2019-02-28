import re

try:
    file = open("wynik_wyszukiwan.txt", 'a')
except IOError:
    print("Blad otwarcia pliku!")

DNA = ['CGGGGCTATGCAACTGGGTCGTCACATTCCCCTTTCGATA',
'TTTGAGGACGTACGTACGATGCAACTCCAAAGCGGACAAA',
'GGATGCAACTGATGCCGTTTGACGACCTAAATCAACGGCC',
'AAGGATGCAACTCGACGTACGTACGAGCTGGTTCTACCTG',
'AATTGGTCTAAAAAGATTATAATGTCGGTCCATGCAACTT',
'CTGCTGTACAACTGAGATCATGCTGCATGCAACTTTCAAC',
'TACATGATCTTTTGATGCAACTTGGATGAGGGAATGATGC',
'ATGACGTACGTACGACTGACGTACCGACGCATGCAACTTC']

file.write("***ZLEPKI GC***\n")
for dna in DNA: # petla po sekwencjach DNA
    m = re.findall(r"GC", dna) # szuka wszystkie wystapienia
    if m:
        file.write("W sekwencji: " + dna + " wystepuje GC w:\n") 
        for match in re.finditer(r"GC", dna): # petla po wszystkich matchach w danej sekwencji
            file.write(str(match.span()) + ' ' + str(match.group()) + '\n')
            # span podaje pozycje startowa i koncowa zlepku, a group wyswietla wystapienie matchujace
    else:
        file.write("W sekwencji: " + dna + " nie wystepuje GC\n")

file.write("\n\n***ZLEPKI G.C LUB C.G, GDZIE W MIEJSCU . JEST DOWOLNY NUKLEOTYD***\n")
for dna in DNA:
    m = re.findall(r"(G.C|C.G)", dna)
    if m:
        file.write("W sekwencji: " + dna + " wystepuja:\n")
        for match in re.finditer(r"(G.C|C.G)", dna):
            file.write(str(match.span()) + ' ' + str(match.group()) + '\n')
    else:
        file.write("W sekwencji: " + dna + " nie wystepuje ani G.C ani C.G\n")
        
file.write("\n\n***ZLEPKI GC I CG, POMIEDZY KTORYMI WYSTEPUJE DOWOLNA SEKWENCJA NIE DLUZSZA NIZ 6***\n")        
for dna in DNA:
    m = re.findall(r"(GC[ACGT]{1,6}CG|CG[ACGT]{1,6}GC)", dna)
    if m:
        file.write("W sekwencji: " + dna + " wystepuja:\n")
        for match in re.finditer(r"(GC[ACGT]{1,6}CG|CG[ACGT]{1,6}GC)", dna):
            file.write(str(match.span()) + ' ' + str(match.group()) + '\n')
    else:
        file.write("W sekwencji: " + dna + " nie wystepuje taki zlepek\n")
        
file.write("\n\n***KONCOWY ZLEPEK C...C, PRZY CZYM W MIEJSCU ... WYSTEPUJE A DOWOLNA ILOSC RAZY***\n")
for dna in DNA:
    m = re.findall(r"(CA*C$)", dna)
    if m:
        file.write("W sekwencji: " + dna + " wystepuja:\n")
        for match in re.finditer(r"(CA*C$)", dna):
            file.write(str(match.span()) + ' ' + str(match.group()) + '\n')
    else:
        file.write("W sekwencji: " + dna + " nie wystepuje C(AAA...)C\n")
        
file.close()