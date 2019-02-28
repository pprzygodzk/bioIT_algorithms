class Node:
    def __init__(self, initdata):
        """konstruktor obiektu klasy"""
        assert initdata == int or float, "wartosc klucza elementu w danym wezle musi byc liczba!"
        assert initdata >= 0, "wartosc klucza elementu w danym wezle nie moze byc ujemna!"
        self.data = initdata
        self.next = None
    
    def getData(self):
        """zwraca wartosc klucza w danym wezle"""
        return self.data
    
    def getNext(self):
        """zwraca link (przekierowanie) do nastepnego wezla"""
        return self.next
    
    def setData(self, newdata):
        """ustawia nowa wartosc klucza w danym wezle"""
        assert newdata == int or float, "wartosc klucza elementu w danym wezle musi byc liczba!"
        assert newdata >= 0, "wartosc klucza elementu w danym wezle nie moze byc ujemna!"
        self.data = newdata
        
    def setNext(self, newnext):
        """ustawia link do nowego wezla"""
        self.next = newnext
        

class UnorderedList:
    def __init__(self):
        """konstruktor obiektu klasy"""
        self.head = None # tworzy "glowe" kolejki priorytetowej
        
    def isEmpty(self):
        """sprawdza, czy lista z dowiazaniami jest pusta"""
        return self.head == None # jesli "glowa" jest pusta, zwraca True 
    
    def add(self, item):
        """dolacza nowy element do listy"""
        assert item == int or float, "wartosc klucza elementu musi byc liczba!"
        assert item >= 0, "wartosc klucza elementu nie moze byc ujemna!"
        newnode = Node(item) # tworzy nowy wezel, ktorego klucz ma wartosc podana jako item
        newnode.setNext(self.head) # ustawia link do None (jezeli jest to pierwszy element
        # w liscie) lub do "glowy" kolejki priorytetowej (zlozonej z jednego lub wiecej wezlow,
        # jezeli przed dodaniem elementu byly jakies inne elementy w liscie)
        self.head = newnode # "glowa" kolejki staje sie nowy wezel (jezeli jest to pierwszy
        # element w liscie) lub nowo utworzony lancuch (jezeli przed dodaniem elementu
        # byly jakies inne elementy w liscie)
        
    def size(self):
        """zwraca rozmiar (ilosc elementow) listy"""
        current = self.head # zaczyna liczenie od "glowy" listy
        count = 0 
        while current != None: # dopoki nie natrafi na brak elementu (None)
            count = count + 1 # dolicza jeden po wejsciu do kazdego wezla
            current = current.getNext() # przechodzi do nastepnego wezla
        return count
    
    def search(self, item):
        """wyszukuje, czy klucz o wartosci item znajduje sie w liscie"""
        assert item == int or float, "wartosc szukanego klucza musi byc liczba!"
        current = self.head # zaczyna przeszukiwanie od "glowy" listy
        found = False # nie znaleziono
        while current != None and not found: # dopoki nie natrafi na brak elementu (None)
            # not found = True, umozliwi nam wykonywanie petli, dopoki nie znajdzie klucza
            if current.getData() == item: # jesli klucz w obecnym wezle jest kluczem, jakiego szukamy
                found = True # to znaleziono; not found = False konczy petle while
            else: # jesli klucz w obecnym wezle nie jest tym, ktorego szukamy
                current = current.getNext() # to przejdz do nastepnego wezla
        return found
    
    def remove(self, item):
        """usuwa klucz o wartosci item z listy (jezeli sie w niej znajduje)"""
        assert item == int or float, "wartosc klucza, ktory chcemy usunac, musi byc liczba!"
        current = self.head # zaczyna przeszukiwanie od "glowy" listy
        previous = None # poczatkowy previous jest None (nic nie ma przed "glowa")
        found = False # nie znaleziono
        while not found: # dopoki nie znajdzie klucza, gdyz not found = True
            if current.getData() == item: # jesli klucz w obecnym wezle jest kluczem, jakiego szukamy
                found = True # to znaleziono; not found = False konczy petle while
            else: # jesli klucz w obecnym wezle nie jest tym, ktorego szukamy
                previous = current # previous jest teraz wezlem current
                current = current.getNext() # current jest teraz wezlem next
                # pozwala to na przesuwanie sie wzdluz listy
        if previous == None: # jesli klucz, ktorego szukamy, byl na poczatku listy
            self.head = current.getNext() # lista zaczyna sie od nastepnego elementu (odcinamy "glowe")
        else: # jesli klucz, ktorego szukamy, byl w srodku listy
            previous.setNext(current.getNext()) # ustawia link z poprzedniego elementu do nastepnego
            # elementu (wykasowuje nasz element z naszej listy, gdyz traci on link kierujacy
            # z poprzedniego do niego i link kierujacy z niego do nastepnego)
                
    def get_max(self):
        """zwraca klucz o najwiekszej wartosci i usuwa go z listy"""
        current = self.head # zaczyna przeszukiwanie od "glowy" listy
        maxkey_value = -1 # poczatkowa wartosc to -1, gdyz najmniejsza wartosc klucza
        # w kolejce priorytetowej jest rowna 0
        while current != None: # dopoki nie natrafi na brak elementu (None)
            if current.getData() > maxkey_value: # jesli klucz w obecnym wezle ma wieksza
                # wartosc niz klucz o maksymalnej wartosci
                maxkey_value = current.getData() # to wartosc klucza z obecnego wezla
                # ustawia jako wartosc maksymalna
            current = current.getNext() # przechodzi do nastepnego wezla
        self.remove(maxkey_value) # usuwa z listy klucz o wartosci maksymalnej
        return maxkey_value # i zwraca klucz o maksymalnej wartosci
    
    def printlistwithnodes(self):
        """drukuje wszystkie elementy w liscie z dowiazaniami"""
        current = self.head
        if current != None:
            while current != None: # dopoki nie natrafi na brak elementu
                if current.getNext() != None:
                    print(current.getData(), end = " --> ")
                else:
                    print(current.getData())
                current = current.getNext()
        else:
            print("Lista jest pusta!")

import random as rd

if __name__ == '__main__':
    print("***TEST POPRAWNOSCI IMPLEMENTACJI***")
    print("***Implementowanie prostej kolejki na liscie z dowiazaniami:***")
    
    test_PQ_listwithnodes = UnorderedList()
    for i in range(20):
        PQkey = rd.randint(0, 400)
        test_PQ_listwithnodes.add(PQkey)

    test_PQ_listwithnodes.printlistwithnodes() # sprawdza dzialanie funkcji printlistwithnodes
    # oraz czy funkcja add poprawnie dowiazuje elementy do listy
    assert test_PQ_listwithnodes.size() == 20, "blad dzialania funkcji size"
    print("Rozmiar kolejki =", test_PQ_listwithnodes.size(), '\n') # sprawdza dzialanie funkcji size
    
    while not test_PQ_listwithnodes.isEmpty():
        print("Obslugiwany element o najwiekszym kluczu =", test_PQ_listwithnodes.get_max())
        # sprawdza dzialanie funkcji get_max (czy poprawnie usuwa elementy z listy wedlug priorytetow
        # ich kluczy)
    
    assert test_PQ_listwithnodes.isEmpty() == True, "funkcja get_max niepoprawnie usuwa elementy z kolejki"
    print("Czy kolejka jest pusta? ", test_PQ_listwithnodes.isEmpty()) # sprawdza dzialanie
    # funkcji isEmpty
    
    
    print("\n\n***Proba obsluzenia elementu z pustej kolejki:***")
    test_PQ_listwithnodes_2 = UnorderedList()
    try:
        print("Obslugiwany element o najwiekszym kluczu =", test_PQ_listwithnodes.get_max())
    except AttributeError:
        print("Nie mozna pobrac elementu z pustej kolejki!")
        # funkcja remove w wywolanym get_maxie szuka maxkey_value = -1,
        # petla wykonuje sie bez konca i zaczyna porownywac te wartosc z wartoscia klucza w currencie
        # (wezel None, ktory nie istnieje), ktora jest NoneType
        