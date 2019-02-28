oriC_vibriocholerae = '''atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc'''

def PatternCount(nucleotide_sequence, k_mer):
    count = 0 # zmienna do zliczania czestosci pojawiania sie k-merow
    for i in range(len(nucleotide_sequence)-len(k_mer)+1):
        # ostatnia pozycja poczatkowa k-meru to ostatni nukleotyd (dlugosc sekwencji)
        # minus dlugosc k-meru
        if nucleotide_sequence[i:(i+len(k_mer))] == k_mer:
            count += 1 # jeżeli w sekwencji nukleotydow napotka dany k-mer,
            # zwieksza wartosc count o 1
    assert nucleotide_sequence != "", "sekwencja nukleotydow musi skladac sie z przynajmniej 1 nukleotydu"
    assert k_mer != "", "poszukiwany k-mer musi skladac sie z przynajmniej 1 nukleotydu"
    assert len(k_mer) <= len(nucleotide_sequence), "dlugosc poszukiwanego k-mera nie moze byc dluzsza niz sekwencja nukleotydow nici"
    assert count < len(nucleotide_sequence), "funkcja zle zlicza k-mery"
    # wyjasnienie: najmniejszy badany k-mer o dlugosci k = 2 wystepuje w nici o dlugosci n
    # maksymalnie n-1 razy i maksymalna czestosc wystepowania k-meru zmniejsza sie
    # coraz bardziej z jego dlugoscia
    return count

def Frequent_kMers(nucleotide_sequence, k):
    frequent_kmers = {} # tworzy slownik czestosci k-merow, jest to o tyle
    # wygodne, ze ponowne natkniecie sie na ten sam k-mer nadpisuje poprzedni (jako klucz),
    # natomiast wartosc czestosci jego pojawiania sie w sekwencji nukleotydow nie zmienia sie
    for i in range(len(nucleotide_sequence)-k+1):
        k_mer = nucleotide_sequence[i:(i+k)]
        frequent_kmers[k_mer] = PatternCount(nucleotide_sequence, k_mer)
        # danemu k-merowi przypisuje jego wartosc czestosci pojawiania sie
    assert nucleotide_sequence != "", "sekwencja nukleotydow musi skladac sie z przynajmniej 1 nukleotydu"
    assert k > 0, "nie istnieje k-mer o dlugosci 0 lub ujemnej"
    assert k <= len(nucleotide_sequence), "dlugosc k-mera nie moze byc dluzsza niz sekwencja nukleotydowa nici"
    assert frequent_kmers[k_mer] >= 0, "k-mer nie moze wystepowac mniej niz 0 razy, blad dzialania funkcji PatternCount"
    return frequent_kmers

def GetMaxValue(dictionary):
    maxvalue = 0
    keys = []
    maxvalues = []
    for key, value in dictionary.items():
        assert value >= 0, "k-mer nie moze wystepowac mniej niz 0 razy; zle przypisane wartosci w slowniku"
        # funkcja assert znajduje sie w tym miejscu, gdyz odnosi sie do konkretnej wartosci
        # (wywolanej w danej iteracji petli) w tym slowniku
        if value > maxvalue: 
            maxvalue = value # nadpisuje nowa wartosc maxvalue
            keys.clear() # czysci k-mery dla poprzednich wartosci maxvalue
            keys.append(key) # dopisuje k-mer o nowej wartosci maxvalue
        elif value == maxvalue:
            keys.append(key) # jezeli dwa k-mery sa rownorzednej wartosci,
            # tj. wystepuja tak samo czesto, to dopisuje kolejny k-mer, nie kasujac
            # poprzedniego (rownorzednego)
    maxvalues = keys # jezeli petla sprawdzi k-mery, to ostateczny zestaw k-merow
    # przenosi do nowej listy maxvalues
    assert dictionary != {}, "wprowadzony slownik jest nieprawidlowy/pusty"
    assert maxvalues != [], "zestaw najczestszych k-merow nie moze byc pusty (po wykonaniu petli)"
    # jezeli slownik k-merow nie jest pusty, to zestaw najczestszych k-merow sklada sie "najmniej"
    # z wszystkich k-merow o tej samej czestosci wystepowania w sekwencji (wszystkie k-mery
    # sa rownorzedne); zestaw ten nigdy nie moze byc pusty (gdyz zawsze jest jeden k-mer badz kilka
    # k-merow, ktore wystepuja najczesciej albo wszystkie k-mery wystepuja z ta sama czestoscia)
    return maxvalues

textfile = open("najczestszekmery.txt", "a")

for k in range(2, 15): # badam k-mery o dlugosci k w zakresie od 2 do 14
    k_mers = Frequent_kMers(oriC_vibriocholerae, k)
    print("k = ", k, "\t", k_mers, "\n\n")
    mostfrequent = GetMaxValue(k_mers)
    textfile.write("Najczesciej wystepujace k-mery dla k = " + str(k) + "\n" + str(mostfrequent) + "\n\n")

textfile.write("WNIOSEK: K-mery o wartosci k=12 sa najlepsze w tej sekwencji nukleotydow, gdyz dlugosc\ntych k-merow jest na tyle wielka, ze prawdopodobienstwo powtorzenia sie tak dlugich sekwencji\njest prawie niemozliwe. Jednak w najczesciej wystepujacych 12-merach pojawiaja sie az trzy,\nktore powtarzaja sie DWA razy. Przy k=13 jest tylko jeden k-mer, ktorzy powtarza sie dwukrotnie (co jest gorszym\nwynikiem niz dla k=12). Natomiast powyzej wartosci k=14 sekwencje juz nie powtarzaja sie dwukrotnie.\nTakie sekwencje, ktore powtarzaja sie jak przy k=12, moga prawdopodobnie pelnic wazne funkcje w ekspresji danego genu.\n")
textfile.close()