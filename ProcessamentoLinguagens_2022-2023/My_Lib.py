# my_lib.py
import Opcs
import codecs
import docutils.core
#My_Lib.py
#Aqui temos algumas funçóes que nos vão ser úteis ao longo do projecto.

#Tem o trabalho de ler o ficheiro que o utilizador insere e em seguida imprimir o mesmo na consola.
def slurp(filename):
    fh = codecs.open(filename, 'rb', encoding='utf-8')
    contents = fh.readlines()
    fh.close()
    documento = ""
    print("Ficheiro que vai ser anlisado:\n")
    for linha in contents:
        documento = documento + linha
    print(documento)
    return documento

#Converte o ficheiro para HTML.
def convert(filename):
    fh = codecs.open(filename, 'rb', encoding='utf-8')
    contents = fh.readlines()
    fh.close()
    with open("suleiman.html", "w") as e:
        for lines in contents:
            if lines != '\n': e.write(lines + "<br>\n")

def convert2(filename):
    docutils.core.publish_file(
        source_path=filename,
        destination_path="output.tex",
        writer_name="latex")


#Faz split dos tokens encontrados.
def splitF(palavra, tipo):
    if tipo == 0:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                palavras_dictionary = {"Linguagem": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary
            if letra == ':':
                p = palavra.split(":")
                palavras_dictionary = {"Linguagem": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary
            if letra == ',':
                p = palavra.split(",")
                palavras_dictionary = {"Linguagem": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary
    elif tipo == 1:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                palavras_dictionary = {"Característica": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary
            if letra == ':':
                p = palavra.split(":")
                palavras_dictionary = {"Característica": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary
            if letra == ',':
                p = palavra.split(",")
                palavras_dictionary = {"Característica": p[0].strip(), "Palavra": p[1].strip()}
                return palavras_dictionary

    elif tipo == 2:
        for letra in palavra:
            if letra == '=':
                p = palavra.split("=")
                palavras_dictionary = {"Característica": p[0].strip(), "Frase": p[1].strip()}
                return palavras_dictionary
            if letra == ':':
                p = palavra.split(":")
                palavras_dictionary = {"Característica": p[0].strip(), "Frase": p[1].strip()}
                return palavras_dictionary
            if letra == ',':
                p = palavra.split(",")
                palavras_dictionary = {"Característica": p[0].strip(), "Frase": p[1].strip()}
                return palavras_dictionary

#Menu que o utilizador vai poder interagir.
def menu(l, p, a, a2, d, d2):
    numero = 0
    while numero != '6':
        print("------------------------------------")
        print("\n1) Contar o nº de palavras que o dicionario tem;")
        print("2) Procurar uma palavra;")
        print("3) Contar nº de palavras que começam com uma letra em concreto;")
        print("4) Demonstrar os atributos de uma dada palavra")
        print("5) Mostrar o nº de linguagens que existe de uma determinada palavra;")
        print("6) Sair;")
        try:
            numero = input("Digite a opção que deseja:\n")
            if numero.isdigit():
                if numero == '1':
                    Opcs.opc1(p)
                elif numero == '2':
                    Opcs.opc2(p)
                elif numero == '3':
                    Opcs.ocp3(p)
                elif numero == '4':
                    Opcs.ocp4(p, a, a2, d, d2)
                elif numero == '5':
                    Opcs.ocp5(p, l)
            else:
                print("Erro!Insira um numero entre 1-6.")
        except:
            print("Erro!Digite algum numero por favor.")


