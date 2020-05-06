# CZESC PIERWSZA - TEKST
#
text = '''Jestes sterem bialym zolnierzem
Nosisz spodnie wiec walcz
Jestes zaglem szalonym wiatrem'''

def add_to_file(nazwa_pliku):
    try:
        file = open(nazwa_pliku, 'a') # otwiera plik w trybie dopisywania do pliku
        # jezeli plik nie istnieje, tworzy go
    except IOError:
        print("\nBlad dostepu do pliku") # jezeli blad otwarcia, wyswietla komunikat
    return file

words = text.split() # rozdziela tekst na wyrazy, separatorem jest kazdy bialy znak
print("Wyrazy: ", words)
amount_of_words = text.count(' ') + text.count('\n') + 1
# dodaje 1, poniewaz po ostatnim wyrazie nie wystepuje zaden bialy znak
print("Liczba wyrazow: ", amount_of_words, "(spodziewany wynik: 12)\n")

file1 = add_to_file("prefiksy.txt")
file2 = add_to_file("sufiksy.txt")

test_words = ['abra', 'kadabra'] # testowa lista wyrazow
l = len(test_words[0]) # wyraz w indeksie 0 jest najkrotszy (ale lista nie jest posortowana)
# dlugosci prefiksu czy sufiksu nie moga byc dluzsze niz liczba l

# test czy prefiksy i sufiksy sa budowane prawidlowo
for i in range(l):
    preffix = ""
    suffix = ""
    for j in range(len(test_words)):
        temporary = test_words[j]
        preffix = preffix + temporary[0:(i+1)]
        # i+1 poniewaz iterator i zaczyna sie od 0, a trzeba wziac na poczatku 1 litere (wiec [0:1])
        suffix = suffix + temporary[-(i+1):]
        # -(i+1) poniewaz indeksy od konca zaczynaja sie od -1, a poczatkowa wartosc i wynosi 0
    print("Testowy wyraz zbud. z prefiksow o l = ", str(i+1), "\t", preffix) 
    print("Testowy wyraz zbud. z sufiksow o l = ", str(i+1), "\t", suffix)
print("(spodziewane wyniki dla wyrazow zbud. z prefiksow: ak, abka, abrkad, abrakada)")
print("(spodziewane wyniki dla wyrazow zbud. z sufiksow: aa, rara, brabra, abraabra)\n")

words2 = sorted(words, key = len, reverse = False) # uporzadkowana lista wlasciwych wyrazow
# porzadkuje liste od najkrotszego do najdluszego
k = len(words2[0]) # k nie moze przekraczac dlugosci najkrotszego wyrazu
# najkrotszy wyraz znajduje sie w indeksie 0

# wlasciwa implementacja
for i in range(k):
    preffix = ""
    suffix = ""
    for j in range(len(words)):
        temporary = words[j]
        preffix = preffix + temporary[0:(i+1)]
        # i+1 poniewaz iterator i zaczyna sie od 0, a trzeba wziac na poczatku jedna litere
        suffix = suffix + temporary[-(i+1):]
        # -(i+1) poniewaz indeksy od konca zaczynaja sie od -1, a poczatkowa wartosc i wynosi 0
    file1.write("k = " + str(i+1) + "\t" + preffix + "\n")
    file2.write("k = " + str(i+1) + "\t" + suffix + "\n")

file1.close()
file2.close()

file3 = add_to_file("najkrotszenajdluzsze.txt")
shortest_word = words2[0]
file3.write("Najkrotszy wyraz: " + shortest_word + "\n")
# lista words2 jest posortowana wg dlugosci wyrazu, w indeksie 0 (liczymy
# od poczatku) znajduje sie najkrotsze slowo
longest_word = words2[-1]
file3.write("Najdluzszy wyraz: " + longest_word + "\n")
file3.close()
# lista words2 jest posortowana wg dlugosci wyrazu, w indeksie -1 (liczymy
# od konca) znajduje sie najdluzsze slowo

file4 = add_to_file("wyrazyuporzadkowane.txt")

test_unsorted_words = ['abrakadabra', 'expecto', 'patronum', 'alakkazam']
test_words_alphabet = sorted(test_unsorted_words, key = str.lower, reverse = False)
# sprawdzam czy funkcja sorted sortuje poprawnie wyrazy alfabetycznie
print("Testowe wyrazy uporzadk. alfabetycznie: ", test_words_alphabet)
print("(spodziewany wynik: [abrakadabra, alakkazam, expecto, patronum])\n")
test_words_length = sorted(test_unsorted_words, key = len, reverse = False)
# sprawdzam czy funkcja sorted sortuje poprawnie wyrazy wg dlugosci
print("Testowe wyrazy uporzadk. wg dlugosci: ", test_words_length)
print("(spodziewany wynik: [expecto, patronum, alakkazam, abrakadabra])\n")

# wlasciwe listy posortowanych wyrazow
words_alphabet = sorted(words, key = str.lower, reverse = False)
words_length = words2

file4.write("Wyrazy uporzadkowane alfabetycznie: " + str(words_alphabet) + "\n") 
file4.write("Wyrazy uporzadkowane wg dlugosci: " + str(words_length) + "\n")
file4.close()



# CZESC DRUGA - DNA
#
import random as rm

# generowanie losowo nici DNA
file5 = add_to_file("losowanicDNA.txt")
n = 101
# 99 jest podzielne przez 3, wiec powstanie 33 aminokwasy
# dodaje 99+2, poniewaz bedziemy przesuwac ramke odczytu (zaczynac od 1, 2 lub 3 nukleotydu)
nitrogen_base = {1: 'A', 2: 'C', 3: 'G', 4: 'T'} # slownik zasad azotowych DNA
DNA_strand = ""
test_DNA_strand = "ACCGTATGA" # krotka sekwencja nukleotydow do przeprowadzenia testow obliczen

for i in range(1, n+1):
    DNA_strand += nitrogen_base[rm.randint(1,4)] 
    # funkcja randint generuje losowo liczby z zakresu od 1 do 4,
    # jest indeksem dla slownika zasad azotowych

file5.write('5\' ' + DNA_strand + ' 3\'' + '\n')
file5.close()

# tworzenie nici komplementarnej za pomoca instrukcji warunkowych
file6 = add_to_file("komplementarnanicDNA.txt")
complementary_DNA_strand = ""
test_complementary_DNA_strand = ""

# sprawdzam czy podana implementacja dobrze przeprowadza replikacje
for i in range(0, 9): # indeksy w testowym DNA sa od 0 do 8, jest 9 nukleotydow
    if test_DNA_strand[i] == 'A':
        test_complementary_DNA_strand += 'T' # komplementarna para A=T
    elif test_DNA_strand[i] == 'T':
        test_complementary_DNA_strand += 'A'
    elif test_DNA_strand[i] == 'C':
        test_complementary_DNA_strand += 'G' # komplementarna para C=G
    elif test_DNA_strand[i] == 'G':
        test_complementary_DNA_strand += 'C'

print("Testowa nic komplementarna: ", test_complementary_DNA_strand, "(spodziewany wynik: TGGCATACT)")

for i in range(0, n):
    if DNA_strand[i] == 'A':
        complementary_DNA_strand += 'T' # komplementarna para A=T
    elif DNA_strand[i] == 'T':
        complementary_DNA_strand += 'A'
    elif DNA_strand[i] == 'C':
        complementary_DNA_strand += 'G' # komplementarna para C=G
    elif DNA_strand[i] == 'G':
        complementary_DNA_strand += 'C'

file6.write('3\' ' + complementary_DNA_strand + ' 5\'' + '\n')
file6.close()

# transkrypcja nici DNA do mRNA
file7 = add_to_file("mRNA.txt")
test_mRNA_strand = test_DNA_strand.replace('T', 'U')
# sprawdzam czy podana implementacja dobrze przeprowadza transkrypcje do mRNA
print("Testowe mRNA: ", test_mRNA_strand, "(spodziewany wynik: ACCGUAUGA)")
mRNA_strand = DNA_strand.replace('T', 'U') # w mRNA zamiast tyminy wystepuje uracyl
file7.write('5\' ' + mRNA_strand + ' 3\'' + '\n')
file7.close()

# translacja mRNA do lancucha polipeptydowego
file8 = add_to_file("sekw_aminokw_od_1_nukleotydu.txt")
file9 = add_to_file("sekw_aminokw_od_2_nukleotydu.txt")
file10 = add_to_file("sekw_aminokw_od_3_nukleotydu.txt")

aminoacids = {'UUU':"Phe",'UUC':"Phe",'UUA':"Leu",'UUG':"Leu",
              'UCU':"Ser",'UCC':"Ser",'UCA':"Ser",'UCG':"Ser",
              'UAU':"Tyr",'UAC':"Tyr",'UAA':"Stop",'UAG':"Stop",
              'UGU':"Cys",'UGC':"Cys",'UGA':"Stop",'UGG':"Trp",
              'CUU':"Leu",'CUC':"Leu",'CUA':"Leu",'CUG':"Leu",
              'CCU':"Pro",'CCC':"Pro",'CCA':"Pro",'CCG':"Pro",
              'CAU':"His",'CAC':"His",'CAA':"Gln",'CAG':"Gln",
              'CGU':"Arg",'CGC':"Arg",'CGA':"Arg",'CGG':"Arg",
              'AUU':"Ile",'AUC':"Ile",'AUA':"Ile",'AUG':"Met",
              'ACU':"Thr",'ACC':"Thr",'ACA':"Thr",'ACG':"Thr",
              'AAU':"Asn",'AAC':"Asn",'AAA':"Lys",'AAG':"Lys",
              'AGU':"Ser",'AGC':"Ser",'AGA':"Arg",'AGG':"Arg",
              'GUU':"Val",'GUC':"Val",'GUA':"Val",'GUG':"Val",
              'GCU':"Ala",'GCC':"Ala",'GCA':"Ala",'GCG':"Ala",
              'GAU':"Asp",'GAC':"Asp",'GAA':"Glu",'GAG':"Glu",
              'GGU':"Gly",'GGC':"Gly",'GGA':"Gly",'GGG':"Gly",} # tabela kodonow

def translation(mRNA, first, last): # funkcja przepisuje kodony na aminokwasy
    codon = ""
    polipeptide_chain = ""
    for i in range(first, last):
        codon += mRNA[i] # tworzy kodon (klucz slownika)
        if len(codon) == 3:
            assert aminoacids.__contains__(codon) == 1, "bledna nic mRNA" 
            # sprawdza, czy kodon znajduje sie w tabeli aminokwasow, funkcja assert
            # znajduje sie w tym miejscu, gdyz kodon sprawdzamy, gdy sklada sie
            # tylko z 3 nukleotydow
            polipeptide_chain += aminoacids[codon]
            # jezeli warunek jest spelniony, dodaje odpowiedni aminokwas do lancucha polipeptydowego
            codon = ""
    assert first < last, "blad w numeracji indeksow"
    assert last-first >= 3, "nic jest za krotka, aby zaszla translacja"
    assert len(codon) <= 3, "kodon nie moze skladac sie z wiecej niz 3 nukleotydow"
    return polipeptide_chain

# sprawdzam czy powyzsza funkcja poprawnie przeprowadza translacje
test_polipeptide_chain = translation(test_mRNA_strand, 0, 9)
print("Testowy lancuch polipeptydowy: ", test_polipeptide_chain, "(spodziewany wynik: Thr-Val-Stop)")

# bierzemy od 1 do 99 nukleotydu (indeksy sa od 0 do 98)
polipeptide_chain1 = translation(mRNA_strand, 0, 99)
file8.write(polipeptide_chain1 + '\n')
file8.close()

# nastepuje przesuniecie ramki odczytu
# bierzemy od 2 do 100 nukleotydu (indeksy sa od 1 do 99)
polipeptide_chain2 = translation(mRNA_strand, 1, 100)
file9.write(polipeptide_chain2 + '\n')
file9.close()

# nastepuje przesuniecie ramki odczytu
# bierzemy od 3 do 101 nukleotydu (indeksy sa od 2 do 100)
polipeptide_chain3 = translation(mRNA_strand, 2, 101)
file10.write(polipeptide_chain3 + '\n')
file10.close()
