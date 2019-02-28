# authors(?) of Tree module: http://www.cs.unc.edu/~prins/Classes/555/Media/Lec05.pdf

def NextLeaf(a, L, k):
    """odwiedza kolejny lisc
    a - wezel drzewa = lista pozycji startowych w sekwencjach DNA
    L - wysokosc drzewa = liczba sekwencji DNA (L = len(a))
    k - dlugosc pojedynczej sekwencji DNA"""
    
    assert a != [], "musi byc przynajmniej jedna pozycja startowa"
    assert L > 0, "musi istniec przynajmniej jedna sekwencja DNA"
    assert L == len(a), "liczba pozycji startowych musi byc rowna liczbie sekwencji DNA"
    assert k > 0, "dlugosc sekwencji DNA nie moze byc mniejsza lub rowna 0"
    
    for i in reversed(range(L)): # petla po pozycjach startowych a od konca listy (reversed)
        if a[i] < k: # jezeli a[i] jest mniejsze niz dlugosc sekwencji DNA
            a[i] += 1 # dodanie jedynki do ostatniej pozycji startowej przenosi nas
            # do nastepnego liscia
            break
        else: # jezeli a[i] przekracza dlugosc sekwencji DNA
            a[i] = 1 # to ustawia a[i] jako 1 (dzieki temu po ostatnim lisciu w drzewie a = [1, 1, ..., 1])
    return a
    
def NextVertex(a, i, L, k):
    """odwiedza drzewo, idac w jego glab, a gdy odwiedzi kazdy lisc odchodzacy
    od danego wierzcholka, to wraca do poziomu tego wierzcholka i przechodzi do wierzcholka obok 
    a - wezel drzewa = lista pozycji startowych w sekwencjach DNA
    i - poziom drzewa
    L - wysokosc drzewa = liczba sekwencji DNA (L = len(a))
    k - dlugosc pojedynczej sekwencji DNA"""
    
    assert a != [], "musi byc przynajmniej jedna pozycja startowa"
    assert L > 0, "musi istniec przynajmniej jedna sekwencja DNA"
    assert L == len(a), "liczba pozycji startowych musi byc rowna liczbie sekwencji DNA"
    assert k > 0, "dlugosc sekwencji DNA nie moze byc mniejsza lub rowna 0"
    assert i >= 0, "poziom drzewa nie moze byc ujemny"
    assert i <= L, "poziom drzewa nie moze byc wiekszy niz wysokosc drzewa (gdyz poziomy indeksujemy od 0)"
    
    if i < L: # jezeli i jest mniejsze niz wysokosc drzewa (nie w lisciu drzewa)
        a[i] = 1 # to i-ta pozycje startowa ustaw jako 1 (umozliwia przejscie w glab drzewa)
        return a, i+1
    else: # jezeli i jest juz rowne wysokosci drzewa (w lisciu drzewa)
        for j in reversed(range(L)): # petla po pozycjach startowych a od konca listy (reversed)
            if a[j] < k: # jezeli a[i] jest mniejsza niz dlugosc sekwencji DNA (ostatnia mozliwa pozycja startowa)
                a[j] += 1 # to dodaj 1 (przechodzi do nastepnego liscia)
                return a, j+1 
            a[j] = 0 # jezeli nie jest, to ustaw a[j] jako 0 i przejdz do kolejnej iteracji petli
            # poprzedniej j-1-szej pozycji startowej (odwiedza kolejny wierzcholek po odwiedzeniu
            # wszystkich lisci w poprzednim wierzcholku)
    return a, 0

def Bypass(a, i, L, k):
    """pomija dzieci wewnetrznego wierzcholka i przechodzi do wierzcholka obok na poziomie i-tym
    a - wezel drzewa = lista pozycji startowych w sekwencjach DNA
    i - poziom drzewa
    L - wysokosc drzewa = liczba sekwencji DNA (L = len(a))
    k - dlugosc pojedynczej sekwencji DNA"""
    
    assert a != [], "musi byc przynajmniej jedna pozycja startowa"
    assert L > 0, "musi istniec przynajmniej jedna sekwencja DNA"
    assert L == len(a), "liczba pozycji startowych musi byc rowna liczbie sekwencji DNA"
    assert k > 0, "dlugosc sekwencji DNA nie moze byc mniejsza lub rowna 0"
    assert i >= 0, "poziom drzewa nie moze byc ujemny"
    assert i <= L, "poziom drzewa nie moze byc wiekszy niz wysokosc drzewa (gdyz poziomy indeksujemy od 0)"
    
    for j in reversed(range(i)): # petla po pozycjach startowych a od i do 0 (reversed)
        if a[j] < k: # jezeli a[j] jest mniejsza niz dlugosc sekwencji DNA
            a[j] += 1 # to dodaj 1 (przechodzi do nastepnego wierzcholka, pomijajac jego dzieci)
            return (a, j+1)
        a[j] = 0 # jezeli nie jest, to ustaw a[j] jako 0 i przejdz do kolejnej iteracji petli
        # tj. poprzedniej j-1 pozycji startowej (aby moc odwiedzic kolejny wierzcholek,
        # pomijajac dzieci)
    return a, 0

if __name__ == "__main__":
    k = 2
    l = 3
    s = [4, 4, 3]
    print ("Wszystkie liscie po", s, end = ':\n')
    
    while True:
        s = NextLeaf(s, 3, k) # sprawdza dzialanie funkcji NextLeaf
        print(s)
        if s == [1, 1, 1]: # wynik powinien byc [1, 1, 1], gdyz przy k = 2
        # maksymalne s = [2, 2, 2], wiec dla s = [4, 4, 3] funkcja NextLeaf
        # dla kazdego a[i] ustawia 1 (wynika to z warunku w else)
            break
    
    print("\nWszystkie wezly w drzewie i ich poziomy:")
    s = [0, 0, 0]
    level = 0
    while True:
        print (s, level)
        s, level = NextVertex(s, level, l, k) # sprawdza dzialanie funkcji NextVertex
        # idzie przez wszystkie wezly w drzewie
        if level == 0: # gdy skonczy przeszukiwac cale drzewo, to NextVertex zwraca znowu
            # wierzcholek [0, 0, 0] czyli wraca do poziomu 0
            break # co konczy petle
    
    print("\nPomijanie dzieci wezlow wewnetrznych na poz. 2 (tj. 11_, 12_->, 21_->, 22_):")
    s = [0, 0, 0]
    level = 0
    while True:
        print (s, level) 
        if (level == 2 and s[0] != s[1]): # pozycja pierwsza i druga musza sie od siebie roznic
            # tak jak 12_ i 21_ (sa to wewnetrzne wezly na poziomie 2)
            s, level = Bypass(s, level, l, k) # aby pomijac dzieci wierzcholka
            print("pomija dzieci wierzcholka wyzej")
        else:
            s, level = NextVertex(s, level, l, k) 
        if level == 0: # po przeszukiwaniu calego drzewa
            # NextVertex zwraca wierzcholek [0, 0, 0], czyli wraca do poziomu 0
            break # co konczy petle

    print("\nPomijanie dzieci wezlow zewnetrznych na poz. 2 (tj. 11_->, 12_, 21_, 22_->):")
    s = [0, 0, 0]
    level = 0
    while True:
        print(s, level)
        if(level == 2 and s[0] == s[1]): # pozycja pierwsza i druga musza byc takie same
            # tak jak 11_ i 22_ (sa to zewnetrzne wezly na poziomie 2)
            s, level = Bypass(s, level, 3, 2) 
            print("pomija dzieci wierzcholka wyzej")
        else:
            s, level = NextVertex(s, level, l, k)
        if level == 0:
            break
