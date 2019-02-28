import numpy

class PriorityQueue_HeapMax:
    def __init__(self):
        """konstruktor obiektu klasy"""
        self.heapmax = []
        if __name__ == '__main__':
            print("Konstruktor zostal wywolany")
        
    def __del__(self):
        """destruktor obiektu klasy"""
        self.heapmax.clear()
        if __name__ == '__main__':
            print("Destruktor zostal wywolany")
        
    def isEmpty(self):
        """sprawdza, czy kolejka priorytetowa na kopcu MAX jest pusta"""
        return self.heapmax == [] # jezeli jest pusta, zwraca True
    
    def size(self):
        """zwraca rozmiar (ilosc elementow) kolejki priorytetowej na kopcu MAX"""
        return len(self.heapmax)
    
    def fixUP(self):
        """po dolaczeniu nowego elementu do kolejki naprawia kopiec MAX od dolu,
        aby najwieksze wartosci znajdowaly sie w korzeniu, a najmniejsze w lisciach"""
        i = self.size()-1 # ostatni dolaczony element do kolejki o rozmiarze n znajduje sie na indeksie n-1
        parent = lambda i: int((i-1)/2) # wyrazenie zwracajace indeks ojca elementu w kopcu MAX
        while i > 0 and self.heapmax[parent(i)] < self.heapmax[i]: # jesli element jest wiekszy niz ojciec elementu
            self.heapmax[parent(i)], self.heapmax[i] = self.heapmax[i], self.heapmax[parent(i)]
            # to zamien element z ojcem elementu
            i = parent(i)
    
    def fixDOWN(self, i):
        """po obsluzeniu (usunieciu) elementu z korzenia kolejki naprawia kopiec MAX od gory,
        aby najwieksze wartosci znajdowaly sie w korzeniu, a najmniejsze w lisciach"""
        assert i >= 0, "indeks elementu nie moze byc ujemny"
        left = lambda i: 2*i+1 # wyrazenie zwracajace indeks lewego syna elementu
        right = lambda i: 2*i+2 # wyrazenie zwracajace indeks prawego syna elementu
        while left(i) < self.size(): # dopoki znajduje sie w kopcu MAX (indeks syna elementu
            # nie moze byc wiekszy niz rozmiar kolejki)
            j = i
            
            if left(i) < self.size() and self.heapmax[left(i)] > self.heapmax[j]:
                # sprawdza czy lewy syn elementu jest wiekszy niz element
                j = left(i) 
            if right(i) < self.size() and self.heapmax[right(i)] > self.heapmax[j]:
                # sprawdza czy prawy syn elementu jest wiekszy niz lewy syn elementu
                j = right(i)
                
            if j != i: # jesli j nie jest rowne i
                self.heapmax[j], self.heapmax[i] = self.heapmax[i], self.heapmax[j]
                # zamien syna elementu z elementem
                i = j # schodzi "w dol"
            else:
                break # jesli synowie elementu sa mniejsi niz element, to przerwij petle
    
    def enqueue(self, item):
        """dolacza nowy element do kolejki priorytetowej"""
        assert item == int or float, "wartosc klucza elementu musi byc liczba!"
        assert item >= 0, "wartosc klucza elementu nie moze byc ujemna!"
        self.heapmax.append(item)
        self.fixUP() # naprawia kopiec od dolu
    
    def dequeue_max(self):
        """pobiera element o najwiekszym kluczu (z korzenia kopca MAX), zwraca jego wartosc
        i usuwa go z kopca"""
        maxkey = self.heapmax[0] # indeks 0 to korzen kopca MAX
        self.heapmax[self.size()-1], self.heapmax[0] = self.heapmax[0], self.heapmax[self.size()-1]
        self.heapmax.pop(self.size()-1)
        self.fixDOWN(0) # naprawia kopiec od gory
        return maxkey
    
    def printheapmax(self):
        """drukuje kolejke priorytetowa w postaci kopca MAX"""
        left = lambda i: 2*i+1 # wyrazenie zwracajace indeks lewego syna
        if self.isEmpty() == False: # jesli kopiec nie jest pusty
            print("Poziomy kopca:\n")
            i = 0 # i to indeks elementu, ktory rozpoczyna kazdy poziom kopca
            while i < self.size(): # dopoki znajduje sie w kopcu MAX (indeks elementu nie moze
                # byc wiekszy niz rozmiar kolejki)
                print(int(numpy.log2(i+1)), end = ':\t') # i-ty element znajduje sie na poziomie kopca MAX wyrazonym jako log2(i+1)
                j = i
                while j < self.size() and j < left(i): # drukuje wszystkie elementy na danym poziomie kopca MAX
                    print(self.heapmax[j], end = '  ')
                    j += 1
                i = left(i) # przechodzi do syna elementu i, a wiec zaczyna kolejny poziom kopca MAX
                print('\n')
        else:
            print("Kopiec jest pusty")

import random as rd

if __name__ == '__main__':
    print("***TEST POPRAWNOSCI IMPLEMENTACJI***")
    print("***Implementowanie prostej kolejki na kopcu MAX:***")
    
    test_PQ_heapmax = PriorityQueue_HeapMax()
    
    for i in range(20): # kolejka priorytetowa losowych 20 liczb
        PQkey = rd.randint(0, 400)
        test_PQ_heapmax.enqueue(PQkey)
        
    test_PQ_heapmax.printheapmax() # sprawdza dzialanie funkcji printheapmax oraz czy funkcja
    # enqueue poprawnie umieszcza elementy na kopcu
    assert test_PQ_heapmax.size() == 20, "blad dzialania funkcji size"
    print("Rozmiar kolejki =", test_PQ_heapmax.size(), '\n') # sprawdza dzialanie funkcji size
    
    while not test_PQ_heapmax.isEmpty():
        print("\nObslugiwany element o najwiekszym kluczu =", test_PQ_heapmax.dequeue_max())
        print("Kopiec MAX po obsluzeniu elementu:\n")
        test_PQ_heapmax.printheapmax()
    
    assert test_PQ_heapmax.isEmpty() == True, "funkcja dequeue_max niepoprawnie usuwa elementy z kopca"
    print("Czy kopiec jest pusty? ", test_PQ_heapmax.isEmpty()) # sprawdza dzialanie funkcji isEmpty
    
    
    print("\n\n***Proba obsluzenia elementu z pustej kolejki:***")
    test_PQ_heapmax_2 = PriorityQueue_HeapMax()
    try:
        print("Obslugiwany element o najwiekszym kluczu =", test_PQ_heapmax_2.dequeue_max())
    except IndexError:
        print("Kopiec jest pusty, nie mozna obsluzyc elementow!")