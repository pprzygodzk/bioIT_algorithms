import score as sc
import tree as tr

def BranchAndBoundMotifSearch(DNA, t, n, l):
    """przeszukuje podany zestaw DNA metodą z ograniczeniami, wynajdując w nim motyw
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
    
    s_tree = [1]*t # lista poczatkowych pozycji startowych w t sekwencjach DNA 
    bestScore = 0 # poczatkowy bestScore ustawiamy jako 0
    # takiego score'a w rzeczywistosci nie da sie uzyskac, gdyz najmniejszy score jest wartosci
    # (l*t)/4, czyli wszystkie zasady azotowe pojawiaja sie z takim samym prawdopodobienstwem,
    # dlatego szukajac motywu, zawsze znajdziemy jakis "lepszy" score
    i = 0 # poziom drzewa, z ktorego startujemy, jest rowny 0
    while True:
        assert i <= t, "poziom drzewa nie moze byc wiekszy niz jego wysokosc"
        if i < t: # jesli poziom drzewa jest mniejszy niz jego wysokosc
            s = [s_tree_i-1 for s_tree_i in s_tree]
            optimisticScore = sc.Score(s, DNA, l)+(t-i)*l # optymistyczny score to tzw. poprawiony
            # score dla poz. startowych nie do konca wypelnionych w drzewie, np. 000 oznacza _ _ _
            # albo 100 oznacza 1_ _
            if optimisticScore < bestScore: # jezeli jest mniejszy niz bestScore
                s_tree, i = tr.Bypass(s_tree, i, t, n-l+1) # to pomija dzieci tego wierzcholka, gdyz
                # nie znajdziemy w nich juz lepszego score'a niz ten optymistyczny
            else: # jezeli jest wiekszy
                s_tree, i = tr.NextVertex(s_tree, i, t, n-l+1) # to wchodzi w glab drzewa, gdyz
                # jest mozliwosc, ze znajdziemy wierzcholek, dla ktorego score
                # jest wiekszy niz bestScore
        else: # jesli poziom jest rowny wysokosci drzewa (bo i nie osiagnie wartosci wiekszej niz t)
            s = [s_tree_i-1 for s_tree_i in s_tree]
            if sc.Score(s, DNA, l) > bestScore: # jesli score jest wiekszy niz bestScore
                bestScore = sc.Score(s, DNA, l) # ustaw score jako nowy bestScore
                bestMotif = [s_i for s_i in s] # a jako bestMotif ustaw pozycje startowe,
                # dzieki ktorym da sie uzyskac ten score
            s_tree, i = tr.NextVertex(s_tree, i, t, n-l+1) # jezeli score nie jest wiekszy, to przejdz
            # do wierzcholka obok 
        if s_tree == [0]*t: # po skonczeniu przeszukiwania calego drzewa NextVertex lub ByPass
            # zwraca wierzcholek s = [0, 0, ..., 0]
            break # przerywa petle
            
    assert bestMotif != [], "zawsze istnieje jakis najlepszy motyw"
    return bestMotif

if __name__ == '__main__':
    test_DNA = ['tagccatgc',
                'cctagaacg',
                'gttgcatag']
    
    testbestMotif = BranchAndBoundMotifSearch(test_DNA, 3, len(test_DNA[0]), 3)
    assert testbestMotif == [0, 2, 6], "funkcja zle wyszukuje motywy"
    # na pozycjach startowych 0, 2, 6 znajduje sie motyw 'tag'
    
    testbestMotif2 = BranchAndBoundMotifSearch(test_DNA, 3, len(test_DNA[0]), 4)
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
    testbestMotif3 = BranchAndBoundMotifSearch(test_DNA_2, 10, len(test_DNA_2[0]), 5)
    assert testbestMotif3 == [0, 3, 2, 0, 0, 0, 0, 1, 4, 1], "funkcja zle wyszukuje motywy"
    print("Wynik BranchAndBound: ", testbestMotif3)