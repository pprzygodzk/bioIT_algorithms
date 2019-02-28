import bruteforcemotifsearch as b
import greedymotifsearch as g
import randomizedmotifsearch as r

set_of_DNA = ['tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta',
'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg']


# BRUTE FORCE MOTIF SEARCH
try:
    file1 = open("bruteforcemotifsearch.txt", 'a')
except IOError:
    print("Nie mozna otworzyc tego pliku")
else:
    bestscore = 0
    for l in range(75, 80):
        motifs, score = b.BruteForceMotifSearch(set_of_DNA, 10, len(set_of_DNA[0]), l)
        if score >= bestscore:
            bestscore = score
            bestmotifs = motifs
            l_longest = l
    file1.write("\nMETODA BRUTALNEJ SILY (sprawdza wszystkie motywy po kolei):\n")
    file1.write("Najdluzszy motyw w tym zestawie sekwencji ma dlugosc " + str(l_longest) + " i uzyskamy go z macierzy motywow w pozycjach startowych s: " + str(bestmotifs) + "\n")
    file1.write("Score dla lancucha konsensusu tej macierzy wynosi: " + str(bestscore) + "\n")
finally:
    file1.close()


# GREEDY MOTIF SEARCH (z zastosowaną regułą Laplace'a)
try:
    file2 = open("greedymotifsearch.txt", 'a')
except IOError:
    print("Nie mozna otworzyc tego pliku")
else:
    BestScore = 0
    for l in range(75, 80):
        Motifs, Score = g.GreedyMotifSearch(set_of_DNA, l, 10)
        if Score >= BestScore:
            BestScore = Score
            BestMotifs = Motifs
            l_Longest = l
    file2.write("\nMETODA ZACHŁANNA (tworzy macierz motywow w oparciu o aktualnie atrakcyjne alternatywy dla motywu):\n")
    file2.write("Najdluzszy motyw w tym zestawie sekwencji ma dlugosc " + str(l_Longest) + " i uzyskamy go na podstawie macierzy motywow:\n")
    file2.write(str(BestMotifs) + '\n')
    file2.write("Score dla lancucha konsensusu tej macierzy wynosi: " + str(BestScore) + "\n")
finally:
    file2.close()


# RANDOMIZED MOTIF SEARCH (z zastosowaniem pseudozliczeń)
try:
    file3 = open("randomizedmotifsearch.txt", 'a')
except IOError:
    print("Nie mozna otworzyc tego pliku")
else:
    rdBestScore = 0
    for l in range(75, 80):
        rdMotifs, rdScore = r.RandomizedMotifSearch(set_of_DNA, l, 10)
        if rdScore >= rdBestScore:
            rdBestScore = rdScore
            rdBestMotifs = rdMotifs
            rd_l_longest = l
    file3.write("\nMETODA LOSOWA (realizacja związana jest z eksperymentem losowym):\n")
    file3.write("Najdluzszy motyw w tym zestawie sekwencji ma dlugosc " + str(rd_l_longest) + " i uzyskamy go na podstawie macierzy motywow:\n")
    file3.write(str(rdBestMotifs) + '\n')
    file3.write("Score dla lancucha konsensusu tej macierzy wynosi: " + str(rdBestScore) + "\n")
finally:
    file3.close()