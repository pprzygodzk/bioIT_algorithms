import random as r

def cartesiancoordinates(k, l):
    """funkcja losuje i zwraca wspolrzedne k punktow kartezjanskich dla l-wymiaru"""
    assert k > 0, "nie mozna stworzyc mniej niz 1 punktu"
    assert l >= 2, "punkty tworzone sa dla przestrzeni min. 2-wymiarowych"
    k_points = [] # tworzy pusta liste, w ktorej zostanie umieszczone k punktow
    for i in range(k): # generuje k punktow (indeksy od 0 do k-1)
        point = [] # tworzy pusta liste dla wspolrzednych nowego punktu
        # nastepuje to na poczatku kazdej iteracji tej petli, gdyz w przeciwnym razie
        # nowe wspolrzedne bylyby dolaczane do wspolrzednych poprzedniego punktu
        for j in range(l): # generuje l wspolrzednych (indeksy od 0 do l-1)
            x = r.uniform(-1.0, 1.0) # losuje liczbe float z zakresu -1.0 do 1.0 i przypisuje ja do wspolrzednej
            point.append(x) # dolacza wspolrzedna do punktu
            assert point != [], "punkt nie moze nie posiadac wspolrzednych"
        k_points.append(point)
    assert k_points != [], "po wykonaniu funkcji lista punktow nie moze byc pusta (musial byc stworzony min. 1 punkt)"
    return k_points

if __name__ == '__main__':
    print("Testy poprawnosci funkcji: ")
    test_points_2D = cartesiancoordinates(10, 2)
    for i in range(10):
        assert test_points_2D[i][0] >= -1.0 and test_points_2D[i][0] <= 1.0, "funkcja nie losuje wspolrzednych z zakresu -1.0 do 1.0"
        assert test_points_2D[i][1] >= -1.0 and test_points_2D[i][1] <= 1.0, "funkcja nie losuje wspolrzednych z zakresu -1.0 do 1.0"
        assert test_points_2D[i][0] ** 2 + test_points_2D[i][1] ** 2 <= 2, "suma kwadratow punktow nie moze byc wieksza od 2"
        # kwadraty wartosci z koncow przedzialu (najwieksze) daja sume rowna 2,
        # tj. (-1)^2 + 1^2 = 2,
        # wiec wszystkie wylosowane liczby dadza sume mniejsza lub rowna dwa