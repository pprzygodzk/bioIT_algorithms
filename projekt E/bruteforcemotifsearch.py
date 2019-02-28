import score as sc
import itertools

def BruteForceMotifSearch(set_of_DNA, t, n, l):
    """szuka metoda brutalnej sily, tj. krotka po krotce i zwraca krotke skladajaca sie
    ze startowych pozycji w podanym zestawie sekwencji DNA, z ktorych mozna utworzyc
    macierz motywow i znalezc w niej najlepszy motyw o dlugosci l, oraz score'a
    dla tej macierzy motywow
    set_of_DNA - zestaw sekwencji DNA, w ktorych szukamy motywu
    t - liczba sekwencji DNA
    n - dlugosci pojedynczej sekwencji DNA
    l - dlugosc szukanego motywu"""
    
    assert t > 1, "nie mozna szukac motywu w mniej niz 2 sekwencjach DNA"
    assert t == len(set_of_DNA), "podana liczba sekwencji DNA musi byc zgodna z rzeczywista"
    assert l < n, "dlugosc motywu nie moze byc wieksza niz dlugosc sekwencji DNA"
    assert l >= 2, "najmniejszy mozliwy motyw nie powinien byc krotszy niz 2 zasady azotowe, gdyz pojedyncze zasady azotowe nie sa motywami" 
    assert n > 2, "sekwencja powinna byc dluzsza niz najmniejszy mozliwy motyw"
    assert set_of_DNA != [], "zestaw sekwencji DNA nie moze byc pusty"
    assert set_of_DNA[0] != "" and set_of_DNA[1] != "", "musza byc minimum 2 sekwencje DNA, aby moc zaczac szukac motywu"

    bestscore = 0 # poczatkowy score przypisuje wartosc 0
    # takiego score'a w rzeczywistosci nie da sie uzyskac, gdyz najmniejszy score jest wartosci
    # (l*t)/4, czyli wszystkie zasady azotowe pojawiaja sie z takim samym prawdopodobienstwem,
    # dlatego przeszukujac motywy po kolejnych krotkach zawsze znajdziemy jakis z "lepszym" scorem
    for s in itertools.product(range(n-l+1), repeat = t): # petla for iteruje krotka po krotce
        # funkcja product zaimplementowana z modulu itertools tworzy krotki o dlugosci podanej
        # w repeat (oznacza to, ze krotka bedzie posiadac t indeksow), czyli s = (s1, s2, ..., st),
        # natomiast range(n-l+1) oznacza, ze kazdy indeks bedzie iterowal n-l+1 razy
        # [czyli od 0 do n-l, tj. (0, 0, ..., 0), (0, 0, ..., 1), ..., (n-l, n-l, ..., n-l)]
        if sc.Score(s, set_of_DNA, l) > bestscore: # sprawdza czy score dla motywow o danych pozycjach
            # startowych (wyznaczonych przez krotke s) w zestawie nici jest wiekszy od bestscore
            bestscore = sc.Score(s, set_of_DNA, l) # jesli tak, to przypisuje nowego score'a
            # jako najlepszy score
            bestmotif = s # najlepszy alignment jest dla motywow o pozycjach startowych s

    assert bestscore != 0, "po przeszukaniu motywow wsrod sekwencji DNA score nie moze sie rownac 0"
    # oznaczaloby to, ze sekwencja nie zawiera zadnej z zasad A, C, G, T, a wiec nie jest sekwencja DNA
    assert bestscore >= (l*t)/4, "najgorsze dopasowanie (najmniejszy score) jest rowny (l*t)/4"
    # t oznacza ze jakas zasada moze pojawic sie t razy na danej pozycji (bo mamy t roznych
    # sekwencji); l oznacza liczbe pozycji w motywie (np. motyw o dlugosci 3 sklada sie
    # z 3 pozycji _ _ _, w ktorych pojawiaja sie zasady azotowe); dzielimy przez 4, gdyz kazda zasada
    # pojawia sie z rownym prawdopodobienstwem
    assert bestscore <= l*t, "najlepsze dopasowanie (najwiekszy score) jest rowny l*t"
    # t*l oznacza ze jakas zasada pojawia sie zawsze t razy na danej pozycji, czyli macierz
    # (alignment) sklada sie z t identycznych motywow
    assert bestmotif != (), "zawsze istnieje jakis najlepszy motyw, krotka (indeksy startowe) nie moze byc pusta"
    return bestmotif, bestscore

if __name__ == '__main__':
    test_set_of_DNA = ['tagccatgc',
    'cctagaacg',
    'ggtgcatag']
    
    testbestmotif_3, testbestscore_3 = BruteForceMotifSearch(test_set_of_DNA, 3, len(test_set_of_DNA[0]), 3)
    assert testbestmotif_3 == (0, 2, 6) and testbestscore_3 == 3 * 3, "funkcja zle wyszukuje motywy"
    # score wynosi 3*3 (l*t), gdyz tworzymy macierz skladajaca sie z t identycznych motywow (tag)
    
    testbestmotif_4, testbestscore_4 = BruteForceMotifSearch(test_set_of_DNA, 3, len(test_set_of_DNA[0]), 4)
    assert testbestmotif_4 == (4, 0, 4) and testbestscore_4 == 10, "funkcja zle wyszukuje motywy"
    # score nie jest juz rowny 12 (l*t), gdyz tworzymy macierz [catg, ccta, cata] i niektore zasady pojawiaja sie
    # na okreslonych pozycjach z roznym prawdopodobienstwem