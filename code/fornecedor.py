import time
import os
import mysql.connector
from funcoes_globais import *

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()
diretorio_atual = os.getcwd()

# FUNÇÕES
def query_fornecedores(): 
    '''
    Lista dos fornecedores
    '''
    FornecedorQuery = 'SELECT * FROM fornecedor'
    cursor.execute(FornecedorQuery)
    ListaFornecedores = cursor.fetchall()
    return ListaFornecedores

def query_compras(): 
    '''
    Lista de todas as compras feitas aos fornecedores
    '''
    ComprasFornecedorQuery = 'SELECT * FROM compra_fornecedor'
    cursor.execute(ComprasFornecedorQuery)
    ListaCompras = cursor.fetchall()
    return ListaCompras

def adicionar_fornecedor():
    from menu import menu_fornecedor
    CLEAR()
    print('\nAdicionar Fornecedor\n')
    lista = query_fornecedores() # Retorna a lista de todos os fornecedores
    
    # Formulário de criação de um fornecedor
    try:
        while True:
            uIn_Fornecedor = str(input('Digite o nome do fornecedor: ')).title()
            uIn_NumTelemovel = str(input('Digite o número de telemóvel do fornecedor: '))
            uIn_Endereco = str(input('Digite o endereço do fornecedor: '))
            uIn_Email = str(input('Digite o email do fornecedor: '))
            # Validação dos inputs
            if validacao_nome(uIn_Fornecedor) and validacao_num_telemovel(uIn_NumTelemovel) and validacao_email(uIn_Email) == True:
                break
            else:
                continue
        # Criação do fornecedor na BD
        if uIn_Fornecedor not in lista:
            uIn_QueryFornecedor = 'INSERT INTO fornecedor (nome_fornecedor, num_telemovel_fornecedor, endereco_fornecedor, email_fornecedor) VALUES (%s, %s, %s, %s)'
            cursor.execute(uIn_QueryFornecedor, (uIn_Fornecedor, uIn_NumTelemovel, uIn_Endereco, uIn_Email))
            print('\nFornecedor inserido com sucesso')
            time.sleep(2)
            return menu_fornecedor()
        else:
            print('Este fornecedor já se encontra na base de dados.')
            time.sleep(2)
            return menu_fornecedor()
    except:
        ExceptResponse(adicionar_fornecedor)

def eliminar_fornecedor():
    from menu import menu_fornecedor
    CLEAR()
    print('\nEliminar Fornecedor\n')
    ListaFornecedor = [fornecedor[1] for fornecedor in query_fornecedores()] # Lista dos nomes de todos os fornecedores

    try:
        while True:
            uIn_Nome = str(input('Digite o nome do fornecedor que deseja eliminar: ')).title()
            # Validação do nome
            if validacao_nome(uIn_Nome) == True:
                break
            else:
                print('Digite uma resposta válida')
                continue
            
        # Eliminação do fornecedor
        if uIn_Nome in ListaFornecedor:
            query = 'DELETE FROM fornecedor WHERE nome_fornecedor = %s'
            cursor.execute(query, (uIn_Nome,))
            print('Fornecedor elmiminado com sucesso.')
            time.sleep(2)
            return menu_fornecedor()
        else:
            print('Fornecedor não existente na base de dados.')
            time.sleep(2)
            return menu_fornecedor()
    except:
        ExceptResponse(eliminar_fornecedor) # Resposta automática caso o utilizador digitar uma resposta inválida

def editar_fornecedor():
    from menu import menu_fornecedor
    CLEAR()
    print('\nEditar Fornecedor\n')
    ListaFornecedor = [fornecedor[1] for fornecedor in query_fornecedores()] # Lista dos nomes de todos os fornecedores

    while True:
        uIn_NomeFornecedor = str(input('Digite o nome do fornecedor: '))
        # Validação do nome
        if validacao_nome(uIn_NomeFornecedor) == False:
            print('Digite uma resposta válida')
            continue
        else:
            break
    
    # Escolha do parâmetro a editar
    if uIn_NomeFornecedor in ListaFornecedor:
        while True:
            try:
                parametro = int(input('''Qual parâmetro você deseja editar? 
                        [1] Nome Completo
                        [2] Número de Telemóvel
                        [3] Endereço
                        [4] Email
                        >  '''))
                if 1 <= parametro <= 4:
                    break
                else:
                    print('Digite um número entre 1 e 4')
                    continue
            except:
                print('Digite uma resposta válida')
                continue

        # Mudar o nome do fornecedor    
        if parametro == 1:
            while True:
                uIn_NovoNomeFornecedor = input('\nDigite o nome completo: ').title()
                # Validação do nome
                if validacao_nome(uIn_NovoNomeFornecedor) == False:
                    print('Digite uma resposta válida')
                    continue
                else:
                    break
            query = 'UPDATE fornecedor SET nome_fornecedor = %s WHERE nome_fornecedor = %s'
            cursor.execute(query, (uIn_NovoNomeFornecedor, uIn_NomeFornecedor)) # Altera o nome do fornecedor na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_fornecedor()

        # Mudar o número de telemóvel do fornecedor  
        elif parametro == 2:
            while True:
                uIn_NumTelemovel = input('\nDigite o novo número de telemóvel: ')
                # Validação do número de telemóvel
                if validacao_num_telemovel(uIn_NumTelemovel) == False:
                    print('Digite uma resposta válida')
                    continue
                else:
                    break
            query = 'UPDATE fornecedor SET num_telemovel_fornecedor = %s WHERE nome_fornecedor = %s'
            cursor.execute(query, (uIn_NumTelemovel, uIn_NomeFornecedor)) # Altera o número de telemóvel do fornecedor na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_fornecedor()

        # Mudar o endereço do fornecedor  
        elif parametro == 3:
            uIn_Endereco = input('\nDigite o endereço: ')
            query = 'UPDATE fornecedor SET endereco_fornecedor = %s WHERE nome_fornecedor = %s'
            cursor.execute(query, (uIn_Endereco, uIn_NomeFornecedor)) # Altera o número de telemóvel do fornecedor na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_fornecedor()

        # Mudar o email do fornecedor  
        elif parametro == 4:
            while True:
                uIn_Email = input('\nDigite o email: ')
                # Validação do email
                if validacao_email(uIn_Email) == False:
                    print('Digite uma resposta válida')
                    continue
                else:
                    break
            query = 'UPDATE fornecedor SET email_fornecedor = %s WHERE nome_fornecedor = %s'
            cursor.execute(query, (uIn_Email, uIn_NomeFornecedor)) # Altera o email do fornecedor na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_fornecedor()

def dicionario_compras():
    '''
    Cria uma lista de dicionários onde cada dicionário é uma compra sendo as chaves dos dicionários os parâmetros de uma compra.
    '''
    ListaCompras = query_compras() # Lista de todas as compras feitas a um fornecedor
    lista_dicionario_compras = []
    for compra in ListaCompras:
        dicionario_compras = {
            'ID Compra': compra[0],
            'ID Artigo': compra[1],
            'ID Administrador': compra[2],
            'ID Fornecedor': compra[3],
            'Quantidade (Kg)': compra[4],
            'Preço (Kg)': compra[5],
            'Preço Total': compra[6],
            'Data': compra[7],
            'Hora': compra[8]
        }
        lista_dicionario_compras.append(dicionario_compras)
    return lista_dicionario_compras

def apresentacao_compras(lista_dicionario_compras: list):
    '''
    Visualização de forma organizada de cada compra dentro da lista
    '''
    print('-' * 150)
    if len(lista_dicionario_compras) == 0: # Se a lista estiver vazia, não irá mostrar resultados.
        return print('Não há resultados!')
    for compra in lista_dicionario_compras: # Mostra cada compra de uma forma organizada
        print(f'''
        ID Compra: {compra['ID Compra']}
        ID Artigo: {compra['ID Artigo']}
        ID Administrador: {compra['ID Administrador']}
        ID Fornecedor: {compra['ID Fornecedor']}
        Quantidade (Kg): {compra['Quantidade (Kg)']}Kg
        Preço (Kg): {compra['Preço (Kg)']}€
        Preço Total: {compra['Preço Total']}€
        Data: {compra['Data']}
        Hora: {compra['Hora']}
        ''')
    print(f'\nForam encontrados {len(lista_dicionario_compras)} registos.') # Mostra quantos registos há na pesquisa.
    print('-' * 150)

def compras_fornecedor():
    '''
    Visualizar as últimas compras feitas aos fornecedores
    '''
    from menu import menu_fornecedor
    CLEAR()
    print('\nVisualizar Compras aos Fornecedores\n')
    lista_dicionario = dicionario_compras() # Criação da lista de dicionários
    
    time.sleep(2)
    CLEAR()
    print('Estes foram os registos de compras encontrados: ')
    apresentacao_compras(lista_dicionario) # Apresentação da lista de compras

    while True:
        uIn_Response = input('Deseja salvar o resultado num ficheiro CSV? (S/N) ').lower()
        if uIn_Response == 's':
            salvar_csv(f'compras_fornecedor{datetime.date.today()}', lista_dicionario) # Criação de um ficheiro csv com a pesquisa feita
            print('Pesquisa salva com sucesso.')
            time.sleep(2)
            return menu_fornecedor()
        elif uIn_Response == 'n':
            time.sleep(2)
            return menu_fornecedor()
        else:
            print('Digite uma resposta válida')
            continue