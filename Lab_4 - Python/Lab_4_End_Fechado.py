import math

# Tamanho da tabela (modifique aqui para testar outros valores de M) #
M = 200 # 200, 500 ou 1000

CHAVE = 0
DADO = 1
COLISAO = 0
TAXA_OCUPACAO = 1

def  computeHash(chave):
    sPi = str(math.pi)*4    # Concatena a string da constante Pi 4 vezes para chegar aos 50 caracteres necessários
    end = 0
    for a in range(0,len(chave)):
        end += ord(chave[a]) * ord(sPi[a])  # Multiplica o caracter a da chave pelo dígito a de Pi, a indo de 0 a len(chave)
    return end % M  # Retorna o resto da divisão da soma das multiplicações por M

def  insertHash(HashTable, element, nums_1_2):
    end = computeHash(element[CHAVE])   # end gerada pela função hash
    if HashTable[end] == None:  
        HashTable[end] = [element]
        nums_1_2[TAXA_OCUPACAO] += (100.0/M)    # Vai calculando a taxa de ocupação da tabela durante a execução do programa
    else:
        HashTable[end].append(element)  
        nums_1_2[COLISAO]+=1    # Se houver dados no end, incrementa o número de colisões
    
           
def searchHash(HashTable, chave):
    end = computeHash(chave)
    if HashTable[end] == None:
        print(chave + " não encontrado no dataset")
        return
    else:
        for i in range(0, len(HashTable[end])):
            if HashTable[end][i][CHAVE] == chave:
                print(chave + " é " + HashTable[end][i][DADO])
                return

#################################################### INÍCIO ####################################################

# Inicializa tabela hash #
HashTable = [None]*M  # HashTable é uma lista de lista de tuples

# Abre arquivo do dataset #
arquivo = open("dataset.txt",'r',1,"utf-8") # Codificação UTF-8
tabela_dados_aux = arquivo.readlines()
arquivo.close()

# Adiciona os dados do arquivo na tabela_dados #
tabela_dados = []
for linha in tabela_dados_aux:
    linha = linha[:-1]  # Remove \n do final da string
    tuple_aux = linha.partition(';')    # Particiona a linha num tuple (chave, ';', dado)
    tuple_aux = (tuple_aux[0],tuple_aux[2]) # Remove o ';'
    tabela_dados.append(tuple_aux) # Adiciona à tabela_dados

nums_1_2 = [0, 0]   # Lista com o número de colisões e a taxa de ocupação da tabela
insercoes = 0
for element in tabela_dados:    # Insere os dados na HashTable
    insertHash(HashTable, element, nums_1_2)
    insercoes += 1

i = 0
for a in HashTable: # Printa a HashTable
    print(i, a)
    i += 1

print("\nTaxa de ocupação da tabela: " + str(nums_1_2[TAXA_OCUPACAO]) + "%")
print("Número de colisões: " + str(nums_1_2[COLISAO]))
print("Número médio de colisões: " + str(nums_1_2[COLISAO]/float(insercoes)) + "\n\n")

# Limpa tabela de entrada e abre arquivo queries #
tabela_dados_aux.clear()
arquivo = open("queries.txt",'r')
tabela_dados_aux = arquivo.readlines()
arquivo.close()

for nome_artistico in tabela_dados_aux:
    nome_artistico = nome_artistico[:-1]  # Remove \n do final da string
    searchHash(HashTable, nome_artistico)