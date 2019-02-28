class PriorityQueue_List:
    def __init__(self):
        """konstruktor obiektu klasy"""
        self.PQ_list = []
        if __name__ == '__main__':
            print("Konstruktor zostal wywolany")
    
    def __del__(self):
        """destruktor obiektu klasy"""
        self.PQ_list.clear()
        if __name__ == '__main__':
            print("Destruktor zostal wywolany")
    
    def isEmpty(self):
        """sprawdza, czy kolejka priorytetowa na liscie jest pusta"""
        return self.PQ_list == [] # jezeli jest pusta, zwraca True
    
    def size(self):
        """zwraca rozmiar kolejki priorytetowej na liscie"""
        return len(self.PQ_list)
    
    def enqueue(self, item):
        """dolacza nowy element do kolejki priorytetowej"""
        assert item == int or float, "wartosc klucza elementu w kolejce priorytetowej musi byc liczba!"
        assert item >= 0, "wartosc klucza elementu w kolejce priorytetowej nie moze byc ujemna!"
        self.PQ_list.insert(0, item) # wstawia element przed indeksem 0
        # indeks 0 jest "ogonem" kolejki
    
    def dequeue_max(self):
        """wyszukuje element o najwiekszym kluczu (odpowiednik get_max),
        zwraca jego wartosc i usuwa go z kolejki (odpowiednik pop_back)"""
        indexmax = 0 # rozpoczynamy wyszukiwanie od "ogona" kolejki
        PQsize = self.size()
        for i in range(1, PQsize):
            if self.PQ_list[i] > self.PQ_list[indexmax]:
                indexmax = i 
        return self.PQ_list.pop(indexmax) # zwraca element z listy w indeksie indexmax
    
    def printPQ(self):
        """drukuje wszystkie elementy znajdujace sie w kolejce priorytetowej"""
        i = 0
        print("Elementy w kolejce:")
        while i < self.size():
            print("nr ", i, "=", self.PQ_list[i], '\t')
            i += 1
        if self.size() == 0:
            print("Kolejka jest pusta")

import random as rd

if __name__ == '__main__':
    print("***TEST POPRAWNOSCI IMPLEMENTACJI***")
    print("***Implementowanie prostej kolejki na zwyklej liscie:***")
    test_PQ_list = PriorityQueue_List()
    
    for i in range(20): # kolejka priorytetowa losowych 20 liczb
        PQkey = rd.randint(0, 400)
        test_PQ_list.enqueue(PQkey)
    
    test_PQ_list.printPQ() # sprawdza dzialanie funkcji printPQ oraz czy funkcja enqueue
    # poprawnie umiescila 20 liczb na liscie
    assert test_PQ_list.size() == 20, "blad dzialania funkcji size"
    print("Rozmiar kolejki =", test_PQ_list.size(), '\n') # sprawdza dzialania funkcji size
    
    while not test_PQ_list.isEmpty():
        print("Obslugiwany element o najwiekszym kluczu =", test_PQ_list.dequeue_max())
        # sprawdza dzialanie funkcji dequeue.max (czy poprawnie usuwa elementy o najwiekszych
        # kluczach z kolejki)
    
    assert test_PQ_list.isEmpty() == True, "funkcja dequeue_max niepoprawnie usuwa elementy z kolejki"
    print("Czy kolejka jest pusta? ", test_PQ_list.isEmpty()) # sprawdza dzialanie funkcji isEmpty
    
    
    print("\n\n***Proba obsluzenia elementu z pustej kolejki:***")
    test_PQ_list_2 = PriorityQueue_List()
    try:
        print("Obslugiwany element o najwiekszym kluczu =", test_PQ_list_2.dequeue_max())
    except IndexError:
        print("Lista jest pusta, nie mozna obsluzyc elementow!")
