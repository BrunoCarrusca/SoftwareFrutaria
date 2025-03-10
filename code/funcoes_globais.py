import os
import time
import datetime
import csv
import mysql.connector

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()
diretorio_atual = os.getcwd()

# FUNÇÕES
def CLEAR(): 
    '''
    Limpar o terminal
    '''
    os.system('cls')
    
def ExceptResponse(function):
    '''
    Para caso o utilizador digitar uma resposta inválida
    '''
    print('Digite uma resposta válida')
    time.sleep(3)
    function()

def salvar_csv(nome_arquivo: str, lista_de_dicionarios: list):
    '''
    Função para exportar os resultados das pesquisas para um ficheiro CSV
    '''
    # Abre o arquivo em modo de escrita
    with open(f'{nome_arquivo}.csv', mode="w", newline="", encoding="utf-8") as arquivo:
        # Obtém as chaves do primeiro dicionário para usar como cabeçalho
        cabecalho = lista_de_dicionarios[0].keys()
        
        # Cria o objeto escritor
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        
        # Escreve o cabeçalho
        escritor.writeheader()
        
        # Escreve os dados
        escritor.writerows(lista_de_dicionarios)
    
    print(f"CSV criado e salvo como: {nome_arquivo}")

def ErroHandle(titleMsg, DescMsg): 
    '''
    Criação do ficheiro LOG para colocar os erros do programa.
    '''
    msg = "----------------------------------------------\n"
    msg += f'Datetime: {datetime.datetime.now()}\n'
    msg += f'Title: {titleMsg} \n'
    msg += f'Description: {DescMsg}\n\n'

    logFile = open(diretorio_atual+'/log.txt', 'a')
    logFile.write(msg)
    logFile.close()

def validacao_numerica(valor_numerico: str):
    '''
    Converte uma string numérica com vírgulas em um número float, substituindo ',' por '.'.
    '''
    try:
        # Substitui a vírgula pelo ponto
        valor_formatado = valor_numerico.replace(',', '.')
        return True, float(valor_formatado)
    except ValueError:
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu letras num parâmetro numérico.')
        return False, print("Erro: Valor numérico inválido.")

def validacao_nome(*args: str):
    '''
    Validação para o parâmetro nome
    '''
    result = 0
    for nome in args:
        if not nome:
            print('Erro: Nome não pode estar vazio.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um nome.')
            return False
        elif nome.isdigit():
            print('Erro: Nome não pode conter números.')
            ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu números no parâmetro nome.')
            return False
        else:
            result += 1
    if result == len(args):
        return True

    
def validacao_num_telemovel(num_telefone: str): 
    '''
    Validação para o número de telemóvel
    '''
    if not num_telefone.isdigit():
        print('Erro: O número deve conter apenas dígitos.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu letras para o número de telemóvel.')
        return False
    elif len(num_telefone) != 9:
        print('Erro: O número deve ter exatamente 9 dígitos.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu um número de telemóvel diferente de 9 dígitos.')
        return False
    else:
        return True
    
def validacao_email(email: str):
    '''
    Validação para o parâmetro email
    '''
    if not email:
        print('Erro: Email não pode estar vazio.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador não inseriu um email.')
        return False
    elif '@' not in email:
        print('Erro: Email inválido. Deve conter @.')
        ErroHandle('Erro de Preenchimento', 'O Utilizador inseriu um email inválido.')
        return False
    else:
        return True
    
def get_id_cliente(nome_cliente: str):
    '''
    Função que devolve o id do cliente a partir do nome do mesmo
    '''
    query = 'SELECT id_cliente FROM cliente WHERE nome_cliente = %s'
    cursor.execute(query, (nome_cliente,))
    ID_cliente = cursor.fetchone()
    return ID_cliente

def get_info_artigo(nome_artigo: str):
    '''
    Função que devolve as informações id_artigo e preço_artigo a partir do nome do mesmo
    '''
    query = 'SELECT id_artigo, preco_artigo FROM artigo WHERE nome_artigo = %s'
    cursor.execute(query, (nome_artigo,))
    Info_artigo = cursor.fetchall()
    return Info_artigo

def get_id_funcionario(nome_funcionario: str):
    '''
    Função que devolve o id do funcionário a partir do nome do mesmo
    '''
    query = 'SELECT id_funcionario FROM funcionario WHERE nome_funcionario = %s'
    cursor.execute(query, (nome_funcionario,))
    ID_funcionario = cursor.fetchone()
    return ID_funcionario