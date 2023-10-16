#Ficheiro que vai conter o código de cada uma das opções no menu que aparece na consola

#Código da Opção 1 (Contar palavras de um dicionário)
def opc1(P):
    Linhas_mortas = 0
    for elemento in P:
        if elemento == '0':
            Linhas_mortas = Linhas_mortas + 1
    print(f"Total de palavras: {len(P) - Linhas_mortas}")
    print("------------------------------------------")

#Código da Opção 2 (Encontrar uma palavra)
def opc2(P):
    paux = 0
    pnaux = 0
    print("\n\n------------------------------------------")
    pal = input("\nDigite a palavra que deseja procurar:")
    try:
        for elemento in P:
            paux = paux + 1
            if elemento == pal:
                print(f"Palavra encontrada: {elemento}")
                print("------------------------------------------")
            else:
                pnaux = pnaux + 1
        if pnaux == paux:
            print("Palavra não encontrada!")
            print("------------------------------------------")
    except:
        print("Erro na digitaçáo. Repita por favor.")
        print("------------------------------------------")

#Código da Opção 3 (Ver quantas palavras começam por uma determinada letra)
def ocp3(P):
    numerolista = 0
    totalPalavras = 0
    l = input("Quantas palavras começam pela letra-> ")
    try:
        for elemento in P:
            numerolista = numerolista + 1
            comecoPalavra = 0
            for letra in elemento:
                comecoPalavra = comecoPalavra + 1
                if letra == l and comecoPalavra == 1:
                    print(f"Palavra -> '{P[numerolista - 1]}'")
                    totalPalavras = totalPalavras + 1
        print("\n------------------------------------")
        print(f"Palavras encontradas que começam pela letra '{l}': {totalPalavras}")
    except:
        print("Erro! Por favor insira um valor correcto.")


#Código da Opção 4(Demonstrar os atributos de uma dada palavra)
def ocp4(p, a, a2, d, d2):
    i = numerolista = vez = linhaEncontrada = linhaAux = nLista = 0
    listaEncontrados = [0,0,0,0,0,0,0,0]
    palavra = input("Digite a palavra quer ver os atributos->")
    palavra2 = palavra.strip()
    try:
        for elemento in p:
            numerolista = numerolista + 1
            if (elemento == palavra2 and linhaEncontrada == 0) or (elemento == palavra2 and listaEncontrados[nLista] == 0):
                    linhaEncontrada = numerolista-1
                    linhaAux = linhaEncontrada
                    listaEncontrados[nLista] = linhaAux
                    nLista = nLista + 1
        for elemento in a:
            if linhaEncontrada == i and listaEncontrados[1] == 0:
                if d[linhaEncontrada-1] != '0':
                    print(f"{d[linhaEncontrada-1]}:{d2[linhaEncontrada-1]}")
                    vez = 1
                linhaAux = linhaAux + 1
                while d[linhaAux] != '0' or a[linhaAux] != '0':
                    if d[linhaAux] != '0':
                        print(f"{d[linhaAux]}:{d2[linhaAux]}")
                        vez = 1
                    if a[linhaAux] != '0':
                        print(f"{a[linhaAux]}:{a2[linhaAux]}")
                        vez = 1
                    linhaAux = linhaAux + 1
            if listaEncontrados[0] == i and listaEncontrados[1] != 0:
                opc4_lista(palavra2, a, a2, d, d2, listaEncontrados)
                vez = 1
            i = i + 1
        if vez == 0: print(f"Não foram encontrados nenhum atributos para a palavra {palavra2}")
    except:
        print("Erro! Por favor insira um valor correcto.")


def opc4_lista(palavra, a, a2, d, d2, listaEncontrados):
    vezes = 0
    try:
        for elemento in listaEncontrados:
            vezes = vezes + 1
            if elemento != 0: print(f"\n{int(vezes)}º ocorrencia da palavra '{palavra}':")
            linhaAux = elemento
            if d[elemento - 1] != '0':
                print(f"{d[elemento - 1]}:{d2[elemento - 1]}")
            linhaAux = linhaAux + 1
            while d[linhaAux] != '0' or a[linhaAux] != '0':
                if d[linhaAux] != '0':
                    print(f"{d[linhaAux]}:{d2[linhaAux]}")
                if a[linhaAux] != '0':
                    print(f"{a[linhaAux]}:{a2[linhaAux]}")
                linhaAux = linhaAux + 1
    except:
        print("Erro! Tente novamente...")


#Código da Opção 5(Mostrar o nº de linguagens que existe de uma determinada palavra)
def ocp5(p, l):
    print("Função não completa...")
    """
    print("\n----------------------------------------------------")
    pal = input("Digita a palavra que quer verificar as linguagens existentes->")
    palavra = pal.strip()
    i = iaux = vez = 0
    try:
        for elemento in p:
            if elemento == palavra:
                vez = 1
                iaux = i
                while p[iaux] != '1':
                    print(f"Linguagem: {l[iaux]}; Palavra: {p[iaux]}")
                    iaux = iaux + 1
                iaux = i
                while p[iaux] != '1':
                    print(f"Linguagem: {l[iaux]}; Palavra: {p[iaux]}")
                    iaux = iaux - 1
            i = i + 1
    except:
        print("Erro pandfsbnfjes")
    """