import numpy as np

                     # 1   2    3    4    5    6    7    8
Profile = np.array([[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7],  # A (adenina)
                    [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2],  # C (cytozyna)
                    [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1],  # G (guanina)
                    [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]]) # T (tymina)
# macierz Profile okresla prawdopodobienstwo wystapienia danej zasady na i-tym miejscu w motywie

def distribuanta(p, i):
    """dystrybuanta - funkcja zbierajaca prawdopodobienstwa i zwracajaca zasade azotowa, ktorej
    prawdopodobienstwo p odpowiada prawdopodienstwu wystapienia danej zasady na i-tym miejscu w motywie"""
    assert p >= 0, "prawdopodobienstwo nigdy nie moze byc mniejsze niz 0"
    assert p <= 1, "prawdopodobienstwo nigdy nie moze byc wieksze niz 1"
    assert i >= 0, "kolumny w macierzy Profile sa indeksowane od 0"
    assert i <= 7, "kolumny w macierzy Profile sa indeksowane do 7"
    t = lambda x, y : x + y # wyrazenie lambda tworzace punkty skokowe
    t1 = t(0.0, Profile[0][i]) # punkt skokowy dystrybuanty (przy wystapieniu A)
    t2 = t(t1, Profile[1][i]) # punkt skokowy dystrybuanty (przy wystapieniu C)
    t3 = t(t2, Profile[2][i]) # punkt skokowy dystrybuanty (przy wystapieniu G)
    t4 = t(t3, Profile[3][i]) # punkt skokowy dystrybuanty (przy wystapieniu T)  
    assert t4 > 0.99999999999 and t4 < 1.00000000001, "suma prawdopodobienstw musi byc rowna 1"
    # przez to, ze dodajemy 0.1 (float) t4 nie jest rowne 1, ale np. 0.99999... lub 1.0000001...
    # floatowe 0.1 w Pythonie nie jest reprezentowane dokladnie, lecz posiada pewien blad precyzji
    
    if p >= 0 and p <= t1:
        return "A" # prawdopodobienstwa od 0 do t1 odpowiadaja wystapieniu A
    elif p > t1 and p <= t2:
        return "C" # prawdopodobienstwa od t1 do t2 odpowiadaja wystapieniu C
    elif p > t2 and p <= t3:
        return "G" # prawdopodobienstwa od t2 do t3 odpowiadaja wystapieniu G
    elif p > t3 and p <= t4:
        return "T" # prawdopodobienstwa od t3 do t4 = 1 odpowiadaja wystapieniu T

if __name__ == '__main__':
    print("Testy poprawnosci funkcji: ")
    test_motif = ""
    for i in range(8):
        test_motif += distribuanta(0.7, i) # przykladowa wartosc prawdopodobienstwa,
        # ktora "zagwarantuje" wystepowanie roznych liter
    assert test_motif == "GCCGGCTA", "blad dzialania funkcji dystrubanty"
    
    test_motif2 = ""
    for i in range(8):
        test_motif2 += distribuanta(0.99999999999, i) # przyjeto prawdopodobienstwo prawie 1,
        # gdyz w Pythonie ze wzgledu na bledy precyzji suma wszystkich prawdopodobienstw moze byc
        # minimalnie mniejsza niz 1
    assert test_motif2 == "TGTTTTTG", "blad dzialania funkcji dystrybuanty"
    # dla 2 i 8 miejsca w motywie prawdopodobienstwo wystapienia T wynosi 0,
    # dlatego dystrybuanta bierze pod uwage poprzednia zasade, czyli G
    # (przy T nie wystepuje punkt skokowy)
    
    test_motif3 = ""
    for i in range(8):
        test_motif3 += distribuanta(0.0, i)
    assert test_motif3 == "AAAAAAAA", "blad dzialania funkcji dystrybuanty"