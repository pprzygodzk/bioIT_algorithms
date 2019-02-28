import PQ_list as l
import PQ_heapmax as hm
import PQ_listwithnodes as lwn
import time as t
import random as rd
import matplotlib.pyplot as pl

# ***
# TESTY WYDAJNOSCI OBSLUGI KOLEJKI PRIORYTETOWEJ:
# ***

# NA LISCIE:
PQ_l = l.PriorityQueue_List()
PQ_list_times = []
n_list = []

for i in range(10, 17):
    n = 2**i
    n_list.append(n)
    time_start = t.time() # funkcja time zwraca czas
    for j in range(n):
        PQkey = rd.randint(1, 150000) # randint losuje liczby calkowite z podanego zakresu
        PQ_l.enqueue(PQkey)
    for j in range(n):
        PQ_l.dequeue_max()
    time_end = t.time()
    t_i = time_end-time_start # czas dzialania dla 2^i danych
    PQ_list_times.append(t_i)

pl.figure(figsize = (8, 8))
pl.loglog(n_list, PQ_list_times, basex = 2, basey = 2, color = 'k') # czarny


# NA KOPCU MAX:
PQ_hm = hm.PriorityQueue_HeapMax()
PQ_heapmax_times = []
n_heapmax = []

for i in range(10, 17):
    n = 2**i
    n_heapmax.append(n)
    time_start = t.time()
    for j in range(n):
        PQkey = rd.randint(1, 150000)
        PQ_hm.enqueue(PQkey)
    for j in range(n):
        PQ_hm.dequeue_max()
    time_end = t.time()
    t_i = time_end-time_start
    PQ_heapmax_times.append(t_i)
    

pl.loglog(n_heapmax, PQ_heapmax_times, basex = 2, basey = 2, color = 'r') # czerwony


# NA LISCIE Z DOWIAZANIAMI:
PQ_lwn = lwn.UnorderedList()
PQ_lwn_times = []
n_lwn = []

for i in range(10, 17):
    n = 2**i
    n_lwn.append(n)
    time_start = t.time()
    for j in range(n):
        PQkey = rd.randint(1, 150000)
        PQ_lwn.add(PQkey)
    for j in range(n):
        PQ_lwn.get_max()
    time_end = t.time()
    t_i = time_end-time_start
    PQ_lwn_times.append(t_i)
    
pl.loglog(n_lwn, PQ_lwn_times, basex = 2, basey = 2, color = 'g') # zielony
pl.show()


# WNIOSKI:
try:
    file = open("wnioski.txt", 'a')
except IOError:
    print("Blad otwarcia pliku!")
else:
    file.write("Wykres przedstawia czas tworzenia i obsluzenia wszystkich elementow (os Y) dla roznej liczby danych (os X)\nrosnacej wykladniczo. Krzywa czarna przedstawia czas dzialania dla kolejki priorytetowej\nna zwyklej liscie, krzywa czerwona - na kopcu MAX, a krzywa zielona - na liscie z dowiazaniami.\nNajbardziej wydajna implementacja jest kopiec MAX, gdyz dla rosnacych wykladniczo danych czas dzialania\nwzrasta powoli (krzywa czerwona rosnie najwolniej). Najmniej wydajna implementacja jest lista\nz dowiazaniami, gdyz jej czas dzialania jest najwiekszy ze wszystkich kolejek oraz rosnie najszybciej\ndla rosnacych wykladniczo danych (krzywa szybko rosnie do gory).\n")
finally:
    file.close()