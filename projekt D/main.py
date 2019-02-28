import wspolrzednekartezjanskie as wk
import wspolrzednebiegunowe as wb
import motywy as m

import matplotlib.pyplot as pl
import random as rd

n = 15000
# CZĘŚĆ 1. WSPÓŁRZĘDNE KARTEZJAŃSKIE
points_2D = wk.cartesiancoordinates(n, 2)

pl.figure(figsize = (7,7))
print("""Rozklad gestosci dla wspolrzednych kartezjanskich jest jednostajny -
oznacza to, ze kazdy punkt ma dokladnie takie samo prawdopodobienstwo
wystapienia w danym miejscu. Dowodzi temu wykres nr 1, ktory dla wielu
losowych punktow zawierajacych sie w jednostkowym okregu, przyjmuje forme
kola, w ktorym punkty rozlozone sa rownomiernie, tj. nie ma miejsc, gdzie
punkty wystepuja rzadziej lub czesciej. Czestosc ich wystepowania jest taka
sama w calym kole.\n\n""")
for i in range(n):
    if points_2D[i][0] ** 2 + points_2D[i][1] ** 2 <= 1:
        pl.plot(points_2D[i][0], points_2D[i][1], 'r.')
    else:
        pl.plot(points_2D[i][0], points_2D[i][1], 'c.')

# CZĘŚĆ 2. WSPÓŁRZĘDNE BIEGUNOWE
n_polar_points = wb.polarcoordinates(n)
n_cartesian_points = wb.from_polar_to_cartesian(n_polar_points)
pl.figure(figsize = (7, 7))
print("""Rozklad gestosci dla wspolrzednych biegunowych nie jest jednostajny -
oznacza to, ze w danym miejscu wystepuja rozne prawdopodobienstwa wystapienia
punktow. Dowodzi temu wykres nr 2, ktory dla wielu losowych punktow
zawierajacych sie w jednostkowym okregu ma forme radiacyjna - w srodku
wystepuja obszary bardziej zageszczone, natomiast na zewnatrz czestosc
wystepowania punktow jest mala. Spowodowane to jest tym, ze wraz
ze zwiekszeniem dlugosci promienia, zwieksza sie tez dlugosc okregu, ktory
nalezy zapelnic i ktory jest zakreslany przez ten promien. Stad punkty
wystepuja tam coraz rzadziej.\n\n""")
for i in range(n):
    pl.plot(n_cartesian_points[i][0], n_cartesian_points[i][1], 'k.')

# CZĘŚĆ 3. MOTYWY
Motifs = []
for k in range(1000): # generuje 1000 motywow
    motif = "" # pusty motyw na poczatku kazdej iteracji petli k (po motywach)
    for i in range(8):
        p = rd.uniform(0.0, 1.0) # losuje prawdopodobienstwo (float) z zakresu od 0 do 1
        motif += m.distribuanta(p, i) # dodaje zasade azotowa na i-tym miejscu w motywie
    Motifs.append(motif) # dolacza motyw do listy motywow
print("Wyszukane motywy:")
print(Motifs)