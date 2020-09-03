import math

# Tamanho da tabela (modifique aqui para testar outros valores de M) #
M = 199 # 199, 499 ou 997 - Precisa ser primo para o DuploHashing

CHAVE = 0
DADO = 1
NUM_COLISOES = 0
MAX_COLISOES = 1
TAXA_OCUPACAO = 2

def  computeHash(chave):
    sPi = str(math.pi)*4    # Concatena a string da constante Pi 4 vezes para chegar aos 50 caracteres necessários
    end = 0
    for a in range(0,len(chave)):   # a indo de 0 a len(chave)
        end += ord(chave[a]) * ord(sPi[a])  # Multiplica o caracter a da chave pelo dígito a de Pi
    return end % M  # Retorna o resto da divisão da soma das multiplicações por M

def  insertHash(HashTable, element, nums_1_2):
    j = 1
    nums_1_2[TAXA_OCUPACAO] += (100.0/M)    # Vai calculando a taxa de ocupação da tabela durante a execução do programa
    end = computeHash(element[CHAVE])   # end gerado pela função hash
    if HashTable[end] == None:  # Se não houver dados no end, grava
        HashTable[end] = element
    else:   # Se houver dados no end
        while HashTable[end] != None:   # Enquando não encontrar um end vazio
            end = j*recomputeHash(element[CHAVE])   # Duplo Hashing
            while M <= end: # Se o endereço ultrapassar o tamanho da tabela, volta pro início
                end -= M
            j+=1
            nums_1_2[NUM_COLISOES]+=1   # Incrementa número de colisões
            if(nums_1_2[MAX_COLISOES]<j): 
                nums_1_2[MAX_COLISOES] = j  # Compara para ver se não é o maior número de colisões numa única inserção
        HashTable[end] = element
           
def searchHash(HashTable, chave):
    j = 1
    end = computeHash(chave)
    try:    # Tenta encontrar o valor nos endereços
        if HashTable[end][CHAVE] == chave:  # Mesmo raciocínio da inserção e duplo hashing
            print(chave + " é " + HashTable[end][DADO])
        else:
            while HashTable[end][CHAVE] != chave:
                end = j*recomputeHash(chave)
                while M <= end:
                    end -= M
                j+=1
            print(chave + " é " + HashTable[end][DADO])
    except TypeError:   # Se houve erro, é porque não há endereço para a chave dada, ou seja, o dado não foi encontrado
        print(chave + " não encontrado no dataset")

def recomputeHash(chave): # Função de realeatorização: semelhante à função hash, mas trocando Pi por e
    sE = str(math.e)*4
    end = 0
    for a in range(0,len(chave)):
        end += ord(chave[a]) * ord(sE[a])
    return end % M

#################################################### INÍCIO ####################################################

# Inicializa tabela hash #
HashTable = [None]*M  # HashTable é uma lista de tuples

# Abre arquivo do dataset e insere dados na tabela de entrada #
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

nums_1_2 = [0, 0, 0]   # Lista com o número de colisões, máximo de colisões em uma única inserção e a taxa de ocupação da tabela
insercoes = 0
for element in tabela_dados:    # Insere os dados na HashTable
    insertHash(HashTable, element, nums_1_2)
    insercoes += 1

i = 0
for a in HashTable: # Printa a HashTable
    print(i, a)
    i += 1

print("\nTaxa de ocupação da tabela: " + str(nums_1_2[TAXA_OCUPACAO]) + "%")
print("Número médio de colisões: " + str(nums_1_2[NUM_COLISOES]/float(insercoes)))
print("Número máximo de colisões em uma única inserção: " + str(nums_1_2[MAX_COLISOES]) + "\n\n")


# Limpa tabela de entrada e abre arquivo queries #
tabela_dados_aux.clear()
arquivo = open("queries.txt",'r',1,"utf-8") # Codificação UTF-8
tabela_dados_aux = arquivo.readlines()
arquivo.close()

for nome_artistico in tabela_dados_aux:
    nome_artistico = nome_artistico[:-1]  # Remove \n do final da string
    searchHash(HashTable, nome_artistico)