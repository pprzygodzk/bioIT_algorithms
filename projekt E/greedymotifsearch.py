import itertools
import score as sc

def makeProfile(Motifs, l):
    """funkcja tworzaca macierz prawdopodobienstw Profile na podstawie zadanej macierzy
    motywow Motifs o dlugosci l
    Motifs - macierz motywow
    l - dlugosc pojedynczego motywu w macierzy"""
    
    assert Motifs != [], "macierz motywow nie moze byc pusta"
    assert l >= 2, "najmniejszy mozliwy motyw sklada sie z 2 zasad azotowych"
    for i in range(len(Motifs)):
        assert Motifs[i] != "", "motywy w macierzy nie moga byc puste"
    if len(Motifs) > 1:
        for i in range(len(Motifs)-1):
            for j in range(len(Motifs)):
                assert len(Motifs[i]) == len(Motifs[j]), """dlugosci wszystkich motywow
                w macierzy musza byc sobie rowne"""
    assert l == len(Motifs[0]), "podana dlugosc motywu musi byc zgodna z rzeczywista"
    
    Profile = {'a': [0]*l, 'c': [0]*l, 'g': [0]*l, 't': [0]*l } # tworzy slownik, tj. pusta
    # macierz Profile rozmiaru 4 x l (4 to ilosc wierszy, czyli reprezentuje poszczegolne
    # zasady azotowe; l to ilosc pozycji w motywie (dlugosc motywu))
    
    for motif in Motifs: # petla po motywach w macierzy motywow
        for i in range(l): # petla po pozycjach w danym motywie
            for key in Profile.keys(): 
                if motif[i] == key: # jesli zasada w danej iteracji petli jest taka
                # sama jak zasada na danej pozycji motywu
                    Profile[key][i] += 1 # dodaj 1 (tj. zlicza wystapienia kazdej z zasad)
                    
    t = len(Motifs) # liczba motywow w macierzy dopasowania, a przez to maksymalna liczba
    # zasad w danej kolumnie, jaka moze wystapic
    for i in range(l):
        assert Profile['a'][i] + Profile['c'][i] + Profile['g'][i] + Profile['t'][i] == t, """
        w motywach wystepowaly inne litery niz A, C, G, T (nie byly to motywy DNA)"""
        
    for i in range(l): 
        for key in Profile.keys():
            Profile[key][i] += 1 # reguła Laplace'a (pseudozliczeń), aby zera nie powodowały problemu
            # przy wyszukiwaniu l-merów
            Profile[key][i] /= (t+4) # aby uzyskac macierz prawdopodobienstw, nalezy podzielic
            # kazda wartosc w macierzy profile przez laczna liczbe zasad w danej kolumnie (t)
            # i liczbe dodanych jedynek w kolumnie (4)
            assert Profile[key][i] >= 0 and Profile[key][i] <= 1, "prawdopodobienstwo musi byc w przedziale od 0 do 1"
    
    assert Profile != {}, "macierz Profile nie moze byc pusta"
    assert Profile != {'a': [0]*l, 'c': [0]*l, 'g': [0]*l, 't': [0]*l }, """po wykonanych operacjach
    macierz Profile musi zawierac jakies prawdopodobienstwa (sekwencje nie byly sekwencjami DNA, tj.
    nie zawieraly zasad azotowych)"""
    return Profile


def mostprobable_nextlmer(sequence_k, l, Profile):
    """funkcja zwraca l-mer z kolejnej k-tej sekwencji majacy najwieksze prawdopodobienstwo
    sequence_k - k-ta sekwencja w zestawie DNA
    l - dlugosc szukanego l-meru
    Profile - macierz prawdopodobienstw potrzebna do wyznaczenia kolejnego l-meru"""
    
    assert sequence_k != "", "podana sekwencja nie moze byc pusta"
    assert l < len(sequence_k), "dlugosc szukanego l-meru nie moze byc wieksza niz dlugosc sekwencji"
    assert l >= 2, "l-mer nie moze byc krotszy niz 2 zasady azotowe"
    assert Profile != {}, "macierz Profilu nie moze byc pusta"
    
    mostprobability = -1 # prawdopodobienstwo poczatkowe rowne -1, gdyz jest ono
    # niemozliwe do uzyskania (kazde znalezione prawdopodobienstwo musi byc w przedziale od 0 do 1)
    for (i, j) in zip(itertools.count(0, 1), itertools.count(l, 1)): # petla po l-merach
        # powstalych w wyniku przesuniec w k-tej sekwencji DNA
        # UWAGA: wyjasnienie itertools.count w GreedyMotifSearch
        if j > len(sequence_k): # j nie moze byc dluzsze niz dlugosc pojedynczej sekwencji DNA
            break
        lmer = sequence_k[i:j] # badany l-mer musi miec dlugosc l
        probability = 1 # mnozenie przez 1 nie zmienia wyniku, dlatego taka wartosc 
        
        for i_lmer in range(l): # petla po pozycjach (i) w badanym l-merze
            for key in Profile.keys(): # zasady azotowe
                if lmer[i_lmer] == key: # jesli zasada w danej iteracji petli jest taka sama jak
                # zasada na danej pozycji badanego l-meru
                    probability *= Profile[key][i_lmer] # to mnozy 1 przez prawdopodobienstwo
                    # wystapienia tej zasady na i-tej pozycji
                    assert probability >= 0 and probability <= 1, "prawdopodobienstwo jest zawsze w przedziale od 0 do 1"
        
        if probability > mostprobability: # jesli prawdopodobienstwo badanego l-meru jest wieksze
        # niz znalezione do tej pory najwieksze prawdopodobienstwo 
            mostprobability = probability # to wartosc najwiekszego prawdopodobienstwa
            # jest teraz wartoscia nowego prawdopodobienstwo 
            nextlmer = sequence_k[i:j] # zapamietuje l-mer z najwiekszym prawdopodobienstwem
            s_k = i # pozycja startowa l-meru w sekwencji k-tej
    
    assert mostprobability != -1, "warunek if musi wykonac sie przynajmniej 1 raz (wartosci w Profile sa bledne)"
    assert nextlmer != "", "musi istniec najbardziej prawdopodobny l-mer w k-tej sekwencji"
    assert s_k <= len(sequence_k)-l, "maksymalna pozycja startowa motywu o dlugosci l w sekwencji o dlugosci n wynosi n-l"
    return nextlmer, s_k


def GreedyMotifSearch(set_of_DNA, l, t):
    """szuka metoda zachlanna, a nastepnie zwraca macierz dopasowania (alignment), z ktorej zostanie
    utworzony najlepszy motyw, 
    set_of_DNA - zestaw sekwencji DNA, w ktorych szukamy motywu
    t - liczba sekwencji DNA
    l - dlugosc szukanego motywu"""
    
    assert set_of_DNA != [], "zestaw sekwencji DNA nie moze byc pusty"
    assert set_of_DNA[0] != "" and set_of_DNA[1] != "", "musza byc minimum 2 sekwencje DNA, aby mozna zaczac szukac motyw"
    assert t > 1, "nie mozna szukac motywu w mniej niz 2 sekwencjach DNA"
    assert t == len(set_of_DNA), "podana liczba sekwencji DNA musi byc zgodna z rzeczywista w zestawie sekwencji DNA"
    assert l >= 2, "najmniejszy mozliwy motyw nie moze byc krotszy niz 2 zasady azotowe (1 zas. azotowa to nie motyw)"
    for i in range(t-1):
        for j in range(1, t):
            assert len(set_of_DNA[i]) == len(set_of_DNA[j]), "dlugosc kazdej sekwencji w zestawie musi byc taka sama"
    assert l < len(set_of_DNA[0]), "dlugosc motywu nie moze byc wieksza niz dlugosc sekwencji DNA"
    
    BestMotifs = [set_of_DNA[i][0:l] for i in range(t)] # tworzy macierz poczatkowych 
    # najlepszych motywow z pierwszych l-merow kazdej sekwencji DNA
    s_bestmotifs = tuple([0]*t) # krotka startowych indeksow dla BestMotifs

    for (i, j) in zip(itertools.count(0, 1), itertools.count(l, 1)): # petla po l-merach powstalych w wyniku przesuniec w pierwszej nici DNA
    # itertools.count(start, step) tworzy nieskonczony iterator, ktory zaczyna od wartosci podanej
    # w start i kazda kolejna zwieksza sie o wartosc step
        if j > len(set_of_DNA[0]): # j nie moze byc dluzsze niz dlugosc pojedynczej sekwencji DNA
            break
        Motif_1 = set_of_DNA[0][i:j] # motyw z pierwszej sekwencji DNA, do ktorego porownujemy pozostale sekwencje
        s_list = [i] # lista startowych indeksow dla motywow w sekwencjach DNA
        Motifs = [Motif_1]
        
        for k in range(1, t): # petla po kolejnych 2, 3, ..., t sekwencjach
            Profile = makeProfile(Motifs, l) # tworzenie macierzy profilu
            # dla dotychczasowej macierzy motywow o dlugosci l
            assert Profile != {}, "macierz Profile nie moze byc pusta (blad dzialania funkcji makeProfile)"
            Motif_k, s_k = mostprobable_nextlmer(set_of_DNA[k], l, Profile) # wyszukuje
            # najbardziej prawdopodobny motyw w kolejnej sekwencji
            assert Motif_k != "", "musi istniec najbardziej prawdopodobny motyw w k-tej sekw. (blad dzialania funkcji mostprobable_nextlmer)"
            assert s_k <= len(set_of_DNA[k])-l, "maksymalna pozycja startowa motywu o dlugosci l w sekwencji o dlugosci n wynosi n-l (blad dzialania funkcji mostprobable_nextlmer)"
            Motifs.append(Motif_k) # po czym dolacza go, tworzac nowa macierz motywu
            s_list.append(s_k) # dolacza pozycje startowa Motif_k w sekwencji k-tej DNA do listy startowych indeksow
        
        s = tuple(s_list) # tworzenie krotki z listy
        
        if sc.myScore(s, set_of_DNA, l) > sc.myScore(s_bestmotifs, set_of_DNA, l): # score Motifs musi byc wiekszy
            # niz score BestMotifs, gdyz swiadczy o lepszym dopasowaniu w macierzy
            BestMotifs.clear()
            for motif in Motifs:
                BestMotifs.append(motif) # jesli warunek jest spelniony to macierz Motifs
                # staje sie nowa macierza najlepszych motywow BestMotifs
            s_bestmotifs = s # startowe indeksy motywow w sekwencjach DNA staja sie startowymi
            # indeksami najlepszych motywow w sekwencjach DNA
                
    BestScore = sc.myScore(s_bestmotifs, set_of_DNA, l)
    assert BestMotifs != [], "macierz najlepszych motywow nie moze byc pusta!"
    return BestMotifs, BestScore

if __name__ == '__main__':
    test_set_of_DNA = ['tagccatgc',
    'cctagaacg',
    'ggtgcatag']
    
    testBestMotifs, testBestScore = GreedyMotifSearch(test_set_of_DNA, 3, 3)
    assert testBestMotifs == ['tag', 'tag', 'tag'], "funkcja zle wyszukuje motywy (blad dzialania funkcji GreedyMotifSearch)"
    assert testBestScore == 3*3, "funkcja zwraca zly score (blad dzialania funkcji myScore)"
    
    testBestMotifs2, testBestScore2 = GreedyMotifSearch(test_set_of_DNA, 4, 3)
    assert testBestMotifs2 == ['catg', 'ccta', 'cata'], "funkcja zle wyszukuje motywy (blad dzialania funkcji GreedyMotifSearch)"
    assert testBestScore2 == 10, "funkcja zwraca zly score (blad dzialania funkcji myScore)"