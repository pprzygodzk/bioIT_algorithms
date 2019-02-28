import random as r
import math
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import axes3d # potrzebne do wykresow 3D

#
# **********************************************************************
# PUSZCZENIE SKRYPTU OBRAZUJE JAK DZIALA ALGORYTM LLOYDA KROK PO KROKU
# WRAZ Z WYKRESAMI
# **********************************************************************
#

def make_random_cluster_centers(k, m):
    """tworzy k losowych punktow centralnych (centrow klastrow)
    k - liczba punktow centralnych c = liczba klastrow
    c - punkt centralny taki, ze:
        c = (c1, c2, ..., cm)
    m - liczba wspolrzednych punktu centralnego = wymiar przestrzeni"""
    
    assert k > 0, "wymagany jest minimum jeden punkt centralny"
    assert m >= 2, "punkt musi miec minimum 2 wspolrzedne, aby znajdowal sie w przestrzeni"
    
    centers = [] # zestaw punktow centralnych
    if __name__ == '__main__':
        print("LOSOWE PUNKTY CENTRALNE:")
    for j in range(k): # k punktow centralnych
        c_j = [r.uniform(0.0, 15.0) for mm in range(m)] # r.uniform(a, b) losuje liczbe float
        # z zakresu od a do b
        if __name__ == '__main__':
            print("C", j, ":", c_j)
        centers.append(c_j)
    
    assert centers != [], "zestaw punktow centralnych nie moze byc pusty po wykonanych operacjach"
    return centers

def assignment_data_to_closest_cluster_centers(set_of_data, centers, k, m, n):
    """przypisuje punkt x_i do najblizszego punktu centralnego c, wokol ktorego
    tworzony jest klaster
    set_of_data - zestaw m-wymiarowych punktow x_i (gdzie i = 1, ..., n)
    centers - zestaw m-wymiarowych punktow centralnych c
    k - liczba punktow centralnych = liczba klastrow
    m - liczba wspolrzednych punktu w zestawie danych = wymiar przestrzeni
    n - liczba punktow w zestawie danych"""
    
    assert set_of_data != [], "zestaw danych musi zawierac jakies punkty!"
    assert centers != [], "zestaw punktow centralnych musi zawierac jakies punkty!"
    assert k == len(centers), "podana liczba punktow centralnych musi zgadzac sie z rzeczywista"
    assert k < len(set_of_data), "liczba punktow centralnych musi byc mniejsza niz liczba danych"
    assert n == len(set_of_data), "podana liczba punktow w zestawie danych musi zgadzac sie z rzeczywista"
    assert m >= 2, "punkt musi miec minimum 2 wspolrzedne, aby znajdowal sie w przestrzeni"
    
    Clusters = [[] for j in range(k)] # zbior k pustych klastrow
    if __name__ == '__main__':
        print("\nODLEGLOSCI PUNKTU X od PUNKTU CENTRALNEGO C:")
    for i in range(n):
        distances = []
        for j in range(k):
            distance_xi_centerj = 0
            for mm in range(m):
                distance_xi_centerj += (set_of_data[i][mm]-centers[j][mm])**2
            distances.append(math.sqrt(distance_xi_centerj)) # obliczanie odleglosci euklidesowej
        minimal_distance_xi = min(distances) # funkcja min zwraca najmniejsza wartosc z listy
        classification = distances.index(min(distances)) # funkcja index zwraca indeks, w jakim
        # znajduje sie najmniejsza odleglosc w liscie odleglosci (jest to jednoczesnie indeks
        # punktu centralnego w centers i indeks klastera wokol tego punktu w Clusters)
        Clusters[classification] = Clusters[classification] + [set_of_data[i]] # dolacza punkt x
        # do klasteru wokol odpowiedniego punktu centralnego
        if __name__ == '__main__':
            print("Punkt X", i, "jest w najmniejszej odleglosci", minimal_distance_xi, "od C", classification)
    
    if __name__ == '__main__':
        print("\n\nUTWORZONE KLASTRY PO PRZYPISANIU PUNKTOW DO NAJBLIZSZYCH CENTROW:")
        print(Clusters, '\n')
    return Clusters

def update_coordinates_of_cluster_centers(k, m, Clusters):
    """wylicza nowe wspolrzedne dla punktow centralnych, korzystajac z sredniej arytmetycznej
    odpowiadajacych wspolrzednych punktow w klastrach
    k - liczba punktow centralnych = liczba klastrow
    m - liczba wspolrzednych punktu centralnego = wymiar przestrzeni
    Clusters = zestaw klastrow wraz z punktami nalezacymi do danego klastera"""
    
    assert k > 0, "wymagany jest minimum jeden punkt centralny"
    assert k == len(Clusters), "liczba punktow centralnych musi byc rowna liczbie klastrow"
    assert m >= 2, "punkt musi miec minimum 2 wspolrzedne, aby znajdowal sie w przestrzeni"
    
    new_centers = [] # zestaw punktow centralnych
    if __name__ == '__main__':
        print("NOWE PUNKTY CENTRALNE:")
    for j in range(k): # tworzy k punktow centralnych
        new_center_j = [] # j-ty punkt centralny
        for mm in range(m): # m-wymiarowy punkt
            new_center_j_mm = 0
            for i in range(len(Clusters[j])):
                new_center_j_mm += Clusters[j][i][mm] # dodaje do siebie wspolrzedne punktow
                # przynaleznych do klasteru, dla ktorego nowy punkt centralny chcemy wyliczyc
            if len(Clusters[j]) != 0: # nie mozna przez 0 dzielic
                new_center_j_mm /= len(Clusters[j]) # srednia arytmetyczna
            new_center_j.append(new_center_j_mm) # dolacza wspolrzedna do punktu
        if __name__ == '__main__':
            print("C", j, ":", new_center_j)
        new_centers.append(new_center_j) # dolacza punkt centralny do zestawu
        
    assert new_centers != [], "zestaw punktow centralnych nie moze byc pusty po wykonanych operacjach!"
    return new_centers

def MeanSquaredError(set_of_data, centers):
    """oblicza sredni blad kwadratowy (blad dystorsji) zestawu punktow X = {x1, x2, ..., xn}
    od zestawu centrow klastrow C = {c1, c2, ..., ck}
    set_of_data - zestaw danych (punktow) X = {x1, x2, ..., xn}
    centers - zestaw centrow klastrow"""
    
    assert set_of_data != [] and centers != [], "oba zestawy punktow nie moga byc puste!"
    
    S = 0 # poczatkowa suma rowna sie 0
    n = len(set_of_data)
    m = len(set_of_data[0])
    k = len(centers)
    
    for i in range(n): # n punktow
        distances = [] # lista odleglosci punktu xi od kazdego z centrow
        for j in range(k): # k centrow klastrow
            distance_xi_centerj = 0
            for mm in range(m): # m-wymiarowe punkty
                distance_xi_centerj += (set_of_data[i][mm]-centers[j][mm])**2
            distances.append(distance_xi_centerj)
        minimal_distance_xi = min(distances) # zwraca najmniejsza wartosc,
        # inaczej d(xi, C) = min[d(xi, ci)]
        S += minimal_distance_xi # suma od i = 0 do n-1 odleglosci punktu xi od zestawu centrow
        # podniesionych do kwadratu        
    MSE = S/n # sredni blad kwadratowy
    return MSE

def k_Means_Lloyd(set_of_data, k):
    """dla podanego zestawu danych n punktow o m wymiarach szuka
    k punktów centralnych, dla których błąd kwadratowy sredni
    jest minimalny
    set_of_data - zestaw danych (m-wymiarowych punktow x_i (gdzie i = 1, ..., n))
    k - liczba punktow centralnych = liczba klastrow"""
    
    assert set_of_data != [], "zestaw danych nie moze byc pusty!"
    assert k < len(set_of_data), "liczba punktow centralnych musi byc mniejsza niz liczba danych"
    assert k > 0, "wymagany przynajmniej 1 punkt centralny"
    
    n = len(set_of_data) # liczba punktow w zestawie danych
    m = len(set_of_data[0]) # liczba wspolrzednych jednego punktu (wymiar przestrzeni)
    
    centers = make_random_cluster_centers(k, m)
    
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'] # 8 roznych kolorow, gdyz liczba danych
    # zawiera sie w 10, a punktow centralnych nie moze byc wiecej niz 10 (gdy k = n, to punkty
    # centralne pokrywaja sie z punktami w zestawie danych)
    if __name__ == '__main__':
        plot1 = pl.figure(figsize = (8, 8))
        ax = plot1.gca(projection = '3d') # umozliwia to wykres 3D
        for data in set_of_data:
            ax.scatter(data[0], data[1], data[2], color = 'k') # jako ze punkty sa w 3 wymiarach
            # to dla uproszczenia indeksy 0, 1, 2 (m = 3), gdy m > 3 to bedzie niepoprawnie
        for center in centers:
            ax.scatter(center[0], center[1], center[2], color = colors[centers.index(center)], label = 'pkt centralny')
        pl.title('Punkty z zestawu danych bez przyporzadkowania do punktow centralnych')
        ax.legend(loc = 3)
        pl.show()
    
    while True: 
        Clusters = assignment_data_to_closest_cluster_centers(set_of_data, centers, k, m, n)
        MSE = MeanSquaredError(set_of_data, centers)
    
        if __name__ == '__main__':
            print("Blad kwadratowy sredni: ", MSE)
            
            plot2 = pl.figure(figsize = (8, 8))
            ax = plot2.gca(projection = '3d')
            for i in range(k):
                for j in range(len(Clusters[i])):
                    ax.scatter(Clusters[i][j][0], Clusters[i][j][1], Clusters[i][j][2], color = colors[i], alpha = 0.4)
                    # alpha umozliwia transparentne punkty (zeby rozroznic od centrow klastrow)
            for center in centers:
                ax.scatter(center[0], center[1], center[2], color = colors[centers.index(center)])
            pl.title('Punkty z zestawu danych uporzadkowane w klastry')
            pl.show()
        
        new_centers = update_coordinates_of_cluster_centers(k, m, Clusters)
        
        if centers == new_centers: # gdy nie zachodza zadne zmiany we wspolrzednych punktow centralnych
            break # konczymy algorytm
        else:
            centers = new_centers # w przeciwnym razie w kolejnej iteracji za punkty centralne
            # ustalamy punkty centralne o nowych wspolrzednych

    return new_centers, MSE


if __name__ == '__main__':
    I = [[10.0, 8.0, 10.0],
         [10.0, 0.0, 9.0],
         [4.0, 8.5, 3.0],
         [9.5, 0.5, 8.5],
         [4.5, 8.5, 2.5],
         [10.5, 9.0, 12.0],
         [5.0, 8.5, 11.0],
         [2.7, 8.7, 2.0],
         [9.7, 2.0, 9.0],
         [10.2, 1.0, 9.2]]
    # I[i][j] to poziom ekspresji genu i w eksperymencie j
    k = 3
    k_Means_Lloyd(I, k)