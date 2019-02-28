import score as sc
import tree as tr

def BruteForceMotifSearchAgain(DNA, t, n, l):
    """przeszukuje podany zestaw DNA metodą brutalnej sily (tj. sprawdza wszystkie
    liscie drzewa), wynajdując w nim motyw
    DNA - zestaw sekwencji DNA
    t - liczba sekwencji DNA
    n - dlugosc pojedynczej sekwencji DNA
    l - dlugosc motywu (mera)
    s - lista pozycji startowych"""
    
    assert DNA != [], "aby znalezc motyw, zestaw musi zawierac jakies sekwencje DNA"
    assert DNA[0] != "" and DNA[1] != "", "musza byc minimum 2 sekwencje, aby zaczac szukac motywu"
    for i in range(len(DNA)-1):
        for j in range(1, len(DNA)):
            assert len(DNA[i]) == len(DNA[j]), "dlugosc kazdej sekwencji musi byc taka sama"
    assert n > 2, "dlugosc sekwencji nie moze byc mniejsza niz dlugosc najmniejszego motywu"
    assert n == len(DNA[0]), "podana dlugosc sekwencji musi byc zgodna z rzeczywista"
    assert t >= 2, "do szukania motywu potrzebne sa minimum 2 sekwencje"
    assert t == len(DNA), "podana liczba sekwencji musi byc zgodna z rzeczywista"
    assert l >= 2, "motyw sklada sie przynajmniej z 2 zasad azotowych (pojedyncza zasada azotowa nie jest motywem)"
    assert l < n, "motyw nie moze byc dluzszy niz sekwencja DNA"
    
    s_tree = [1]*t # lista pozycji startowych pierwszego liscia
    s = [s_tree_i-1 for s_tree_i in s_tree]
    bestScore = sc.Score(s, DNA, l) # poczatkowy bestScore jest scorem dla pierwszego liscia
    while True:
        s_tree = tr.NextLeaf(s_tree, t, n-l+1) # przejdz do nastepnego liscia
        assert len(s_tree) == t, "liczba pozycji startowych musi byc rowna liczbie sekwencji DNA (blad dzialania funkcji NextLeaf)"
        s = [s_tree_i-1 for s_tree_i in s_tree]
        if sc.Score(s, DNA, l) > bestScore: # jezeli score dla kolejnego liscia jest wiekszy
            # niz bestScore
            bestScore = sc.Score(s, DNA, l) # ustaw jako bestScore nowy score
            bestMotif = [s_i for s_i in s] # a jako bestMotif pozycje startowego nowego liscia
        if s_tree == [1]*t: # po skonczeniu przeszukiwaniu wszystkich lisci funkcja NextLeaf
            # zwraca pozycje s = [1, 1, ..., 1], co konczy petle
            assert bestMotif != [], "zawsze istnieje jakis najlepszy motyw"
            return bestMotif

if __name__ == '__main__':
    test_DNA = ['tagccatgc',
                'cctagaacg',
                'gttgcatag']
    
    testbestMotif = BruteForceMotifSearchAgain(test_DNA, 3, len(test_DNA[0]), 3)
    assert testbestMotif == [0, 2, 6], "funkcja zle wyszukuje motywy"
    # na pozycjach startowych 0, 2, 6 znajduje sie motyw 'tag'
    
    testbestMotif2 = BruteForceMotifSearchAgain(test_DNA, 3, len(test_DNA[0]), 4)
    assert testbestMotif2 == [0, 2, 1], "funkcja zle wyszukuje motywy"
    # alignment = ['tagc', 'taga', 'ttgc']
    
    test_DNA_2 = ['tagtggtct',
                  'cgcgactcg',
                  'gttacttgt',
                  'aacatcagg',
                  'accaccgga',
                  'tagattcga',
                  'gaaatggtt',
                  'atgtatact',
                  'ttcttacac',
                  'ctacctatg']
    testbestMotif3 = BruteForceMotifSearchAgain(test_DNA_2, 10, len(test_DNA_2[0]), 5)
    assert testbestMotif3 == [0, 3, 2, 0, 0, 0, 0, 1, 4, 1], "funkcja zle wyszukuje motywy"
    print("Wynik BruteForce: ", testbestMotif3)