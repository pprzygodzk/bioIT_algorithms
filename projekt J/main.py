import kmeans_lloyd as kml

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

setofCenters = []
setofMSEs = [] 

for k in range(3, 9):
    centers, MSE = kml.k_Means_Lloyd(I, k)
    setofMSEs.append(MSE)

try:
    file = open("oceny_i_wnioski.txt", 'a')
except IOError:
    print("Nie mozna otworzyc takiego pliku!")
else:
    for i in range(0, 6):
        file.write("\nDla k = " + str(i+3) + " blad kwadratowy sredni wynosi " + str(setofMSEs[i]))
    file.write("\nWNIOSKI:\n")
    file.write("1) k = " + str(setofMSEs.index(min(setofMSEs))+3) + " jest najbardziej optymalna liczba klasterow, na ktore mozna podzielic dane\n")
    file.write("2) im wieksze k, tym blad kwadratowy sredni jest mniejszy\n")
    file.write("(punkt 2. moze nie byc ukazany na wynikach, gdyz wspolrzedne poczatkowych punktow centralnych sa losowane i moze zdarzyc sie tak,\nze zaden z punktow w zestawie danych nie zostanie przyporzadkowany do jakiegos punktu centralnego, gdy jest zbyt daleko od calego zestawu)")
finally:
    file.close()