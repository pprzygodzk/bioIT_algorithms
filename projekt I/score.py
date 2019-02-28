def Score(s, DNA, k):
    """oblicza score uzgodnionego łańcucha profilu (konsensus)
    dla danej macierzy motywow (alignment) o dlugosci k
    zbudowanej na startowych indeksach s w sekwencjach DNA
    s - krotka startowych indeksow
    DNA - lista nici nukleotydowych
    k - dlugosc szukanego motywu"""
    
    assert k >= 2, "najmniejszy mozliwy motyw nie powinien byc krotszy niz 2 zasady azotowe (1 zas. azot. to nie motyw)"
    assert DNA != [], "lista nici nukleotydowych nie moze byc pusta"
    for i in range(len(DNA)):
        assert DNA[i] != "", "nici nukleotydowe musza byc jakims ciagiem znakow, aby obliczyc z nich score"
    assert k < len(DNA[0]), "dlugosc motywu nie moze byc wieksza niz dlugosc sekwencji DNA"
    assert s != (), "krotka musi zawierac jakies startowe indeksy"
    
    score = 0 # poczatkowa przypisana wartosc score to 0
    
    if __name__ == '__main__':
        print("*****FUNKCJA Score:*****")
        print("Indeksy startowe [s] w sekwencjach DNA: ", s)
        print("Dlugosc szukanego motywu: ", k)
        print("Poczatkowy score: ", score)
    
    for i in range(k): # pętla po kolejnych pozycjach w motywie (po kolumnach od indeksu 0 do k-1) 
        cnt = dict(zip("acgt", (0, 0, 0, 0))) # tworzy slownik, ktory reprezentuje
        # pusta jednokolumnowa macierz dla i-tej pozycji w motywie (i-ta kolumna macierzy Profile)
        
        if __name__ == '__main__':
            print("\nAnalizowana pozycja na motywie: ", i+1)
            print("Poczatkowy count (i-ta kolumna macierzy Profile):", cnt)
            
        for j, s_val in enumerate(s): # petla po motywach zaczynajacych sie od s_val-tej pozycji w j-tej nici
            assert j < len(DNA), """w krotce nie moze byc wiecej indeksow startowych niz
            liczba nici nukleotydowych [t] (j jest od 0 do t-1)"""
            assert s_val <= len(DNA[0])-k, "pozycje startowe nie moga byc wieksze niz n-k (n to dlugosc pojedynczej nici)" 
            
            if __name__ == '__main__':
                print("Analizowany motyw:", DNA[j][s[j]:s[j]+k], "\tZasada na", i+1, "pozycji w motywie:", DNA[j][s_val+i])
                #[s[j]:s[j]+k] oznacza, że wycinamy motyw z sekwencji DNA od miejsca s[i] (i-ty indeks w krotce s)
                # do miejsca s[i]+k (motyw musi miec dlugosc k)
            
            base = DNA[j][s_val+i] # przypisuje zasade azotowa, ktora znajduje sie w j-tej
            # sekwencji DNA na i-tej pozycji motywu (motywy zaczynaja sie od s_val, dlatego musimy
            # uwzglednic to przesuniecie w indeksie)
            assert cnt.__contains__(base) == True, "przypisana litera z sekwencji musi byc zasada azotowa (sekwencje nie byly sekwencjami DNA)"
            cnt[base] += 1 # przy kazdym wystapieniu danej zasady dolicza 1
            # do jej wartosci w slowniku (zlicza, ile razy dana zasada wystepuje na i-tej pozycji
            # we wszystkich motywach)
        
        assert max(cnt.values()) != 0, """w motywie musza wystapic zasady azotowe (musi
        nastapic zliczenie przy wystapieniu), wiec wprowadzone sekwencje nie sa sekwencjami DNA"""
        score += max(cnt.values()) # pobiera maksymalna wartosc ze slownika i dolicza ja do ogolnego score'a
        
        if __name__ == '__main__':
            print("Count po zliczeniach zasad: ", cnt)
            print("***Najwieksza wartosc w i-tej kolumnie:", max(cnt.values()), '***')
            print("***Score po dodaniu najwiekszej wartosci:", score, '***')
    
    assert score != 0, "po wykonanych operacjach score nie moze sie rownac 0"
    assert score <= k*len(DNA), "najlepsze dopasowanie (najwiekszy score) jest rowny k*t (t to liczba sekwencji)"
    assert score >= (k*len(DNA))/4, "najgorsze dopasowanie (najmniejszy score) jest rowny (k*t)/4)"
    return score

if __name__ == '__main__':
    # testy dla Score:
    test_DNA_1 = ['tagggtc', 'tagcagt', 'tagagcg', 'tagtgct', 'tagccat']
    k1 = 3
    
    s_1 = (0, 0, 0, 0, 0)
    wynik_1 = Score(s_1, test_DNA_1, k1)
    print("Wynik_1 =", wynik_1, '\n\n')
    assert wynik_1 == 15, "blad dzialania funkcji Score"
    
    s_2 = (1, 1, 1, 1, 1)
    wynik_2 = Score(s_2, test_DNA_1, k1)
    print("Wynik_2 =", wynik_2, '\n\n')
    assert wynik_2 == 12, "blad dzialania funkcji Score"
    
    test_DNA_2 = ['ctagattg', 'gtgcaatg', 'aaccgtca']
    k2 = 4
    
    s_3 = (1, 1, 2)
    wynik_3 = Score(s_3, test_DNA_2, k2)
    print("Wynik_3 =", wynik_3, '\n\n')
    assert wynik_3 == 7, "blad dzialania funkcji Score"
    
    s_4 = (3, 2, 4)
    wynik_4 = Score(s_4, test_DNA_2, k2)
    print("Wynik_4 =", wynik_4, '\n\n')
    assert wynik_4 == 7, "blad dzialania funkcji Score"
    
    s_5 = (4, 0, 4)
    wynik_5 = Score(s_5, test_DNA_2, k2)
    print("Wynik_5 =", wynik_5, '\n\n')
    assert wynik_5 == 7, "blad dzialania funkcji Score"