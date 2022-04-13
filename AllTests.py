# PALÍNDROMO
def palindrome(word):
    if word[::-1].lower() == word.lower():
        print('PALINDROME!')
        print(word[::-1].upper())
    else:
        print('NOT PALINDROME')
        print(word[::-1].upper())

# palindrome('Masato')


# MATRIZ
def mostrar_matriz():
    Matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for l in Matriz:
        for i in l:
            print(i, end=' ')
        print()

# mostrar_matriz()


# CRIANDO MATRIZ
def criar_matriz():
    matriz = []

    for indice_linha in range(10):
        linha = []
        for indice_coluna in range(15):
            linha.append(indice_coluna + indice_linha)
        matriz.append(linha)

    for linha in range(10):
        for coluna in range(15):
            print(f'{matriz[linha][coluna]:<4}', end='')
        print()

# criar_matriz()


# CÁLCULO DA VARIÂNCIA
import numpy as np

def variancia(dados, tipo=1):
    
    n = len(dados)
    media = np.mean(dados)

    s2 = [(dados[k] - media) ** 2 for k in range(0, len(dados))]

    s2 = sum(s2)

    if tipo == 1:
        s2 = s2 / n
    elif tipo == 2:
        s2 = s2 / (n - 1)
    
    print(s2)

# variancia([40000, 18000, 12000, 150000, 30000, 140000, 300000, 40000, 800000])


# FATORIAL
def fatorial(num):
    cont = num
    fat = 1
    while cont > 0:
        fat *= cont
        cont -= 1
    return fat

# print(fatorial(5))


# CÁLCULO DE COMBINAÇÕES
def combinations(n, p):
    C = fatorial(n) / (fatorial(p) * fatorial(n - p))
    print(C)

# combinations(60, 6)


# VERIFICANDO SE PALAVRAS EXISTEM EM UMA WORDLIST
def spellChecker(phrase):
    
    wordlist = []
    not_in_wordlist = []

    with open('words.txt', 'r') as file:
        filelines = file.readlines()
        for i in filelines:
            wordlist.append(i.lower().strip())
        
    phrase_low = phrase.lower().replace(',', '').split()
    for i in range(len(phrase_low)):
        if phrase_low[i] not in wordlist:
            not_in_wordlist.append(phrase_low[i])
    
    return not_in_wordlist



# PROBABILIDADE DE VALOR EM UMA AMOSTRA
def probabilidade_amostra():
    from random import randint

    lancamentos = 100000
    vezes = {
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0,
        7 : 0,
        8 : 0,
        9 : 0,
        10 : 0,
        11 : 0,
        12 : 0
    }

    def lancar():
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)

        somatoria = dado1 + dado2

        vezes[somatoria] = vezes[somatoria] + 1


    def imprimir():
        for k,v in vezes.items():
            print(f'{k} : {v} -> {(v / lancamentos) * 100:.0f}%')


    def main():
        for i in range(lancamentos):
            lancar()

        imprimir()


    main()

# probabilidade_amostra()


# CONTANDO CARACTERES UNICOS
def char_unicos():
    letras = {}


    def unicos(texto):
        for caracter in texto:
            letras[caracter] = 0
        print(letras)
        return len(letras)


    def main():
        texto = 'Hello World'
        print(unicos(texto))


    main()

# char_unicos()


# ANAGRAMA COM DICT
def dict_anagram():
    dp1 = {}
    dp2 = {}

    def anagram(texto1, texto2):
        for caractere in texto1:
            if caractere not in dp1:
                dp1[caractere] = 1
            else:
                dp1[caractere] += 1

        for caractere in texto2:
            if caractere not in dp2:
                dp2[caractere] = 1
            else:
                dp2[caractere] += 1
        print(dp1)
        print(dp2)
        

    def main():
        texto1 = 'roma'
        texto2 = 'amor'

        anagram(texto1, texto2)

        if dp1 == dp2:
            print('ANAGRAMA!')
        else:
            print('N ANAGRAMA...')


    main()

# dict_anagram()
