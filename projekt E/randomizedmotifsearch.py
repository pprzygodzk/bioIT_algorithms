import score as sc
import random as rd
from greedymotifsearch import makeProfile
from greedymotifsearch import mostprobable_nextlmer

def makenewMotifs(Profile, set_of_DNA, l):
    """zwraca nową macierz motywów na podstawie macierzy Profile i sekwencji DNA
    Profile - macierz prawdopodobienstw (w postaci slownika)
    set_of_DNA - zestaw sekwencji DNA, w ktorych szukamy nowej macierzy motywow
    l - dlugosc szukanego motywu"""
    
    assert Profile != {}, "macierz Profile nie moze byc pusta"
    assert set_of_DNA != [], "zestaw sekwencji DNA nie moze byc pusty"
    for DNA in set_of_DNA:
        assert DNA != "", "sekwencje musza byc ciagiem znakow"
    for i in range(len(set_of_DNA)-1):
        for j in range(1, len(set_of_DNA)):
            assert len(set_of_DNA[i]) == len(set_of_DNA[j]), """dlugosc kazdej sekwencji
            w zestawie musi byc taka sama"""
    assert l >= 2, """najmniejszy mozliwy motyw nie moze byc krotszy niz 2 zasady azotowe
    (1 zas. azotowa to nie motyw)"""
    assert l < len(set_of_DNA[0]), "dlugosc motywu nie moze byc wieksza niz dlugosc sekwencji DNA"
    
    newMotifs = []
    s_list = []
    for DNA in set_of_DNA: # pętla po sekwencjach DNA
        newmotif, s_k = mostprobable_nextlmer(DNA, l, Profile) # zwraca najbardziej prawdopodobny
        # motyw w danej sekwencji
        assert newmotif != "", "zawsze jest jakis najbardziej prawdopodobny motyw (blad dzialania funkcji mostprobable_nextlmer)"
        assert s_k <= len(DNA)-l, "maksymalna pozycja startowa motywu o dlugosci l w sekwencji o dlugosci n wynosi n-l (blad dzialania funkcji mostprobable_nextlmer)"
        newMotifs.append(newmotif)
        s_list.append(s_k)
    
    s = tuple(s_list)
    assert newMotifs != [], "macierz nowych motywow nie moze byc pusta po wykonanych operacjach"
    assert s != (), "krotka musi zawierac jakies startowe indeksy po wykonanych operacjach"
    return newMotifs, s


def RandomizedMotifSearch(set_of_DNA, l, t):
    """szuka metodą losową i zwraca macierz motywów (alignment), z ktorej
    mozna utworzyc najlepszy motyw
    set_of_DNA - zestaw sekwencji DNA, w ktorych szukamy motywu
    l - dlugosc szukanego motywu
    t - liczba sekwencji DNA"""
    
    assert set_of_DNA != [], "zestaw sekwencji DNA nie moze byc pusty"
    assert set_of_DNA[0] != [] and set_of_DNA[1] != [], """musza byc minimum
    2 sekwencje DNA, aby mozna zaczac szukac motyw"""
    for i in range(t-1):
        for j in range(1, t):
            assert len(set_of_DNA[i]) == len(set_of_DNA[j]), """dlugosc kazdej sekwencji
            w zestawie musi byc taka sama"""
    assert t > 1, "nie mozna szukac motywu w mniej niz 2 sekwencjach DNA"
    assert t == len(set_of_DNA), """podana liczba sekwencji DNA musi byc zgodna
    z rzeczywista w zestawie sekwencji DNA"""
    assert l >= 2, """najmniejszy mozliwy motyw nie moze byc krotszy niz 2 zasady azotowe
    (1 zas. azotowa to nie motyw)"""
    assert l < len(set_of_DNA[0]), "dlugosc motywu nie moze byc wieksza niz dlugosc sekwencji DNA"
    
    if __name__ == '__main__':
        print("***RANDOMIZED MOTIF SEARCH***")
        print("Dlugosc szukanego motywu:", l)
    
    n = len(set_of_DNA[0]) # dlugosc pojedynczej sekwencji DNA
    Motifs = [] # pusta lista dla losowo wybranych motywow
    s = []
    for DNA in set_of_DNA: # odpowiednik petli od 0 do t-1 (petla po sekwencjach)
        i = rd.randint(0, n-l) # losuje liczbe int z zakresu od 0 do n-l
        # n-l to maksymalna startowa pozycja motywu 
        j = i+l
        Motif_1 = DNA[i:j] # wycina motyw o dlugosci l z sekwencji DNA
        s.append(i)
        Motifs.append(Motif_1) # tworzy macierz losowych motywow od 0 do t-1
    
    BestMotifs = Motifs # poczatkowe BestMotifs to macierz losowych motywow
    s_bestmotifs = tuple(s)
    if __name__ == '__main__':
        print("\nPoczątkowe BestMotifs:")
        print(BestMotifs)
        print("(początkowy score wynosi:", sc.myScore(s_bestmotifs, set_of_DNA, l), end=')\n')
        # end umozliwia wstawienie nawiasu zaraz po wartosci myScore bez zbednej spacji
        # w tym przypadku ma funkcje jedynie estetyczna
    
    while True:
        Profile = makeProfile(Motifs, l) # tworzy macierz Profile z macierzy Motifs
        Motifs, s = makenewMotifs(Profile, set_of_DNA, l) # tworzy macierz nowych motywow
        # na podstawie utworzonej macierzy Profile i sekwencji DNA
        
        if sc.myScore(s, set_of_DNA, l) > sc.myScore(s_bestmotifs, set_of_DNA, l): # score musi byc wiekszy, gdyz swiadczy
        # o lepszym dopasowaniu motywow w macierzy
            BestMotifs.clear()
            for motif in Motifs: # pętla po motywach
                BestMotifs.append(motif) # jesli warunek jest spelniony, to macierz Motifs zostaje
                # nowa macierza BestMotifs
            if __name__ == '__main__':
                print("BestMotifs po kolejnej iteracji:")
                print(BestMotifs)
            s_bestmotifs = s
        else:
            BestScore = sc.myScore(s_bestmotifs, set_of_DNA, l)
            if __name__ == '__main__':
                print("Ostateczne BestMotifs:")
                print(BestMotifs)
            return BestMotifs, BestScore
        

if __name__ == '__main__':
    test_set_of_DNA = ['cgcccctctcgggggtgttcagtaaacggcca',
                       'gggcgaggtatgtgtaagtgccaaggtgccag',
                       'tagtaccgagaccgaaagaagtatacaggcgt',
                       'tagatcaagtttcaggtgcacgtcggtgaacc',
                       'aatccaccagctccacgtgcaatgttggccta']
    
    motifs3, score3 = RandomizedMotifSearch(test_set_of_DNA, 3, 5)
    print("***Score wynosi: ", score3, '\n\n')
    
    motifs4, score4 = RandomizedMotifSearch(test_set_of_DNA, 4, 5)
    print("***Score wynosi: ", score4, '\n\n')
    
    motifs5, score5 = RandomizedMotifSearch(test_set_of_DNA, 5, 5)
    print("***Score wynosi: ", score5, '\n\n')
    
    motifs6, score6 = RandomizedMotifSearch(test_set_of_DNA, 6, 5)
    print("***Score wynosi: ", score6, '\n\n')