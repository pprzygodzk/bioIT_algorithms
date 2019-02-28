import branchandboundmotifsearch as bnb
import bruteforcemotifsearchagain as bf

DNA = ['tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat',
       'cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt',
       'gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt',
       'aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg',
       'accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac',
       'tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc',
       'gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta',
       'atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta',
       'ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac',
       'ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg']

t = len(DNA)
n = len(DNA[0])
l = 78

try:
    file = open("wyniki_przeszukiwania.txt", 'a')
except IOError:
    print("Nie mozna otworzyc pliku!")
else:
    file.write("\nSZUKANIE MOTYWU O DŁUGOŚCI 78 W ZESTAWIE SEKWENCJI DNA:\n")
    bestMotif_bnb = bnb.BranchAndBoundMotifSearch(DNA, t, n, l)
    file.write("Wynik przeszukiwania metodą BranchAndBound: " + str(bestMotif_bnb) + '\n')
    bestMotif_bf = bf.BruteForceMotifSearchAgain(DNA, t, n, l)
    file.write("Wynik przeszukiwania metodą BruteForce: " + str(bestMotif_bf) + '\n')
    file.write("Wyniki reprezentuja pozycje startowe w sekwencjach DNA, dla których 78-mery tworzą motyw.\n")
finally:
    file.close()