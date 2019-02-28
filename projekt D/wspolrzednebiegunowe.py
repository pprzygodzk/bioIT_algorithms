import random as rd
import numpy as np

def polarcoordinates(k):
    """funkcja generuje losowe wspolrzedne biegunowe k punktow lezacych w jednostkowym okregu"""
    assert k > 0, "funkcja nie moze stworzyc mniej niz 1 punkt"
    polar_points = [] # tworzy pusta liste dla k punktow
    for i in range(k): # generuje k punktow
        point = [] # tworzy pusta liste dla wspolrzednych nowego punktu
        r = rd.uniform(0.0, 1.0) # zakres wartosci promienia jest od 0 do 1 (jednostkowy okreg)
        # rd.uniform generuje losowe liczby float z podanego zakresu
        point.append(r)
        theta = rd.uniform(0.0, 2.0*np.pi) # np.pi to liczba pi, katy sa podawane w radianach
        point.append(theta)
        assert point != [], "punkt nie moze nie posiadac wspolrzednych"
        polar_points.append(point) # dolacza punkt do listy punktow
    assert polar_points != [], "po wykonaniu funkcji lista musi zawierac przynajmniej 1 punkt"
    return polar_points

def from_polar_to_cartesian(polar_points):
    """funkcja przeksztalca wspolrzedne biegunowe punktu we wspolrzedne kartezjanskie"""
    assert polar_points != [], "wprowadzona lista punktow nie moze byc pusta"
    cartesian_points = [] # tworzy pusta liste dla przeksztalconych k punktow
    for i in range(len(polar_points)): # punkty znajduja sie w indeksach od 0 do len(polar_points)-1
        point = []
        x = polar_points[i][0] * np.cos(polar_points[i][1]) # np.cos to funkcja cosinus
        # w indeksie 0 znajduje sie promien r,
        # a w indeksie 1 znajduje sie kat theta
        assert x <= 1.0, "wspolrzedna x nie moze byc wieksza niz 1" # promien r wynosil od 0 do 1
        assert x >= -1.0, "wspolrzedna x nie moze byc mniejsza niz -1"
        point.append(x)
        y = polar_points[i][0] * np.sin(polar_points[i][1]) # np.sin to funkcja sinus
        assert y <= 1.0, "wspolrzedna y nie moze byc wieksza niz 1"
        assert y >= -1.0, "wspolrzedna y nie moze byc mniejsza niz -1"
        point.append(y)
        assert point != [], "punkt nie moze nie posiadac wspolrzednych"
        cartesian_points.append(point) # dolacza punkt o przeksztalconych wspolrzednych do listy punktow
    assert cartesian_points != [], "po wykonaniu funkcji lista musi zawierac przynajmniej 1 punkt"
    return cartesian_points

if __name__ == '__main__':
    print("Testy poprawnosci funkcji: ")
    test_polar_points = polarcoordinates(10)
    for i in range(10):
        assert test_polar_points[i][0] >= 0.0 and test_polar_points[i][0] <= 1.0, "funkcja zle losuje promien"
        assert test_polar_points[i][1] >= 0.0 and test_polar_points[i][1] <= 2.0*np.pi, "funkcja zle losuje kat theta"
    test_cartesian_points = from_polar_to_cartesian(test_polar_points)
    for i in range(10):
        assert test_cartesian_points[i][0] ** 2 + test_cartesian_points[i][1] ** 2 <= 1, "funkcja zle przeszktalca punkty"
        # odleglosc przeksztalconych punktow nie moze byc wieksza niz 1 (gdyz zawsze sa w jednostkowym okregu)