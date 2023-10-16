import ply.lex as plex
import My_Lib
#Main.py

#Projecto nº1 ,cadeira de Processamento de Linguagens ,curso LESI-PL;
#Elementos do grupo:
#Luis Esteves - 16960;
#Sérgio Ribeiro - 18858;
#Tema 1;


#Tokens que vamos utilizar ao longo do trabalho;
    #lg -> Dedicado para ler frases do tipo : DE = Getriebe
    #defe -> Dedicado para ler frases do tipo : +numero = Singular
    #skip -> Dedicado para fazer skip para quando encontra frases do tipo : #blablabla
    #descr -> Dedicado para ler frases do tipo : definicao = Aro de borracha, com ou sem câmara-de-ar, que (...)

tokens = ["lg", "defe", "skip", "descr"]
t_ignore = '\n'
#Queremos ignorar os paragrafos do texto
#t_ignore = "\n"
#Inicialiazação das variáveis que vamos utilizar ao longo do programa
    #Dicionários que vão tratar de guardas as nossas frases já com o split feito
palavras_dictionary = {}
defe_dictionary = {}
descr_dictionary = {}
    #Listas que vao guardar cada um dos elementos dos dicionários
Linguagens = []
Palavras = []
Caracteristica = []
Caract_p2 = []
Descricao = []
Descr_p2 = []

#Defenição no nosso token para ler frases do tipo: DE = Getriebe
#Fazemos split da string encontrada, em seguida guardamos num dicionário esse resultado.
#Por fim, anexamos os valores numa lista. No resto das lista anexamos '0'.
#Queremos que todas as listas tenham o mesmo numero de elementos, para um tratamneto mais fácil.
def t_lg(t):
    r"[A-Z]+(\-[A-Z]+)*[ ]*.[ ]*([A-Z]*[a-z]+[ ]*|.+)+"
    global palavras_dictionary, Linguagens, Palavras
    palavra = t.value
    tipo = 0
    palavras_dictionary = My_Lib.splitF(palavra, tipo)
    Linguagens.append(palavras_dictionary["Linguagem"])
    Palavras.append(palavras_dictionary["Palavra"])
    Caracteristica.append('0')
    Caract_p2.append('0')
    Descricao.append('0')
    Descr_p2.append('0')

#O mesmo processo de cima, mas agora para outro tipo de tokens.
#Para frases do tipo: +numero = Singular
def t_defe(t):
    r"\+.+[ ]*.[ ]*(\,?[ ]*.[ ]*)+"
    global defe_dictionary, Caracteristica, Caract_p2
    palavra = t.value
    tipo = 1
    defe_dictionary = My_Lib.splitF(palavra, tipo)
    Caracteristica.append(defe_dictionary["Característica"])
    Caract_p2.append(defe_dictionary["Palavra"])
    Descricao.append('0')
    Descr_p2.append('0')
    Linguagens.append('0')
    Palavras.append('0')

#O mesmo processo de cima, mas agora para outro tipo de tokens.
#Para frases do tipo: definicao = Aro de borracha, com ou sem câmara-de-ar, que (...)
def t_descr(t):
    r"[a-z]+[ ]*.[ ]*.+"
    global descr_dictionary, Descr_p2, Descricao
    palavra = t.value
    tipo = 2
    descr_dictionary = My_Lib.splitF(palavra, tipo)
    Descricao.append(descr_dictionary["Característica"])
    Descr_p2.append(descr_dictionary["Frase"])
    Caracteristica.append('0')
    Caract_p2.append('0')
    Linguagens.append('0')
    Palavras.append('0')

#Detecta quando ocorre um erro e menciona o mesmo.
def t_error(t):
    print(f"Unxpected token: '{t.value[:10]}'")
    exit(1)

#Faz skip para alguns tokens que queremos ignorar.
def t_skip(t):
    r"(\#[ ]*.+)|[ ]*.+"
    Descricao.append('0')
    Descr_p2.append('0')
    Caracteristica.append('0')
    Caract_p2.append('0')
    Linguagens.append('0')
    Palavras.append('0')
    pass


lexer = plex.lex()
#O utilizador insere o ficheiro que quer analiar.
f = input("Insira o ficheiro que quer analisar:")
fich = f.strip()
lexer.input(My_Lib.slurp(fich))
print("\n\n------------------------------------------")

#Conversão do ficheiro para um HTML e LATEX.
My_Lib.convert(fich)
My_Lib.convert2(fich)

token = lexer.token()
#Aqui aparece o menu em que o utizador vai poder análisar o texto como quiser.
My_Lib.menu(Linguagens, Palavras, Caracteristica, Caract_p2, Descricao, Descr_p2)
