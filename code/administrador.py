import os
import mysql.connector
from funcoes_globais import *

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()
diretorio_atual = os.getcwd()

# FUNÇÕES
def query_administrador(): 
    '''
    Lista dos administradores
    '''
    AdministradorQuery = 'SELECT * FROM administrador'
    cursor.execute(AdministradorQuery)
    ListaAdministrador = cursor.fetchall()
    return ListaAdministrador

def adicionar_administrador():
    '''
    Função que adiciona um administrador
    '''
    from menu import menu_administrador
    CLEAR()
    print('\nAdicionar Administrador\n')
    ListaNomesAdministradores = [administrador[1] for administrador in query_administrador()] # Lista dos nomes dos administradores

    # Formulário de criação de um administrador
    try:
        while True:
            uIn_NomeAdm = str(input('Digite o nome do administrador: ')).title()
            uIn_NumTelemovelAdm = str(input('Digite o número de telemóvel: '))
            uIn_EnderecoAdm = str(input('Digite o endereço: '))
            uIn_EmailAdm = str(input('Digite o email: '))

            # Validação dos inputs
            if validacao_nome(uIn_NomeAdm) and validacao_num_telemovel(uIn_NumTelemovelAdm) and validacao_email(uIn_EmailAdm) == True:
                break
            else:
                continue
            
        # Criação do novo administrador a base de dados
        if uIn_NomeAdm not in ListaNomesAdministradores:
            query = 'INSERT INTO administrador(nome_administrador, num_telemovel_administrador, endereco_administrador, email_administrador) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (uIn_NomeAdm, uIn_NumTelemovelAdm, uIn_EnderecoAdm, uIn_EmailAdm))
            print('\nFuncionário adicionado com sucesso.')
            time.sleep(2)
            return menu_administrador()
        else:
            print('Este administrador já se encontra na base de dados.')
            time.sleep(2)
            return menu_administrador()
    except:
        ExceptResponse(adicionar_administrador) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função

def eliminar_administrador():
    from menu import menu_administrador
    CLEAR()
    print('\nEliminar Administrador\n')
    ListaAdministrador = [administrador[1] for administrador in query_administrador()] # Lista dos nomes dos administradores

    try:
        while True:
            uIn_Nome = str(input('Digite o nome do administrador que deseja eliminar: ')).title()
            # Validação do input
            if validacao_nome(uIn_Nome) == True:
                break
            else:
                continue
        # Eliminação do administrador
        if uIn_Nome in ListaAdministrador:
            query = 'DELETE FROM administrador WHERE nome_administrador = %s'
            cursor.execute(query, (uIn_Nome,))
            print('Administrador elmiminado com sucesso.')
            time.sleep(2)
            return menu_administrador()
        else:
            print('Administrador não existente na base de dados.')
            time.sleep(2)
            return eliminar_administrador()
    except:
        ExceptResponse(eliminar_administrador) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função

def editar_administrador():
    from menu import menu_administrador
    CLEAR()
    print('\nEditar Administrador\n')
    ListaAdministrador = [administrador[1] for administrador in query_administrador()]

    try:
        while True:
            uIn_NomeAdministrador = str(input('Digite o nome do administrador: ')).title()
            # Validação do nome
            if validacao_nome(uIn_NomeAdministrador) == True:
                break
            else:
                print('Digite uma resposta válida')
                continue
    except:
        ExceptResponse(editar_administrador) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função
    
    if uIn_NomeAdministrador in ListaAdministrador:
        try:
            # Pergunta qual parâmetro a editar
            while True:
                parametro = int(input('''Qual parâmetro você deseja editar? 
                        [1] Nome Completo
                        [2] Número de Telemóvel
                        [3] Endereço
                        [4] Email
                        >  '''))
                break
            
            # Parâmetro Nome
            if parametro == 1:
                while True:
                    uIn_NovoNomeAdministrador = input('\nDigite o nome completo: ').title()
                    # Validação do nome
                    if validacao_nome(uIn_NovoNomeAdministrador) == False:
                        print('Digite uma resposta válida')
                        continue
                    else:
                        break
                query = 'UPDATE administrador SET nome_administrador = %s WHERE nome_administrador = %s'
                cursor.execute(query, (uIn_NovoNomeAdministrador, uIn_NomeAdministrador)) # Altera o nome do administrador na base de dados.
                print('Dados alterados com sucesso.')
                time.sleep(2)
                return menu_administrador()

            # Parâmetro Número Telemóvel
            elif parametro == 2:
                while True:
                    uIn_NumTelemovel = input('\nDigite o novo número de telemóvel: ')
                    # Validação do número de telemóvel
                    if validacao_num_telemovel(uIn_NumTelemovel) == False:
                        print('Digite uma resposta válida.')
                        continue
                    else:
                        break
                query = 'UPDATE administrador SET num_telemovel_administrador = %s WHERE nome_administrador = %s'
                cursor.execute(query, (uIn_NumTelemovel, uIn_NomeAdministrador)) # Altera o número de telemóvel do administrador na base de dados.
                print('Dados alterados com sucesso.')
                time.sleep(2)
                return menu_administrador()

            # Parâmetro Endereço
            elif parametro == 3:
                uIn_Endereco = input('\nDigite o endereço: ')
                query = 'UPDATE administrador SET endereco_administrador = %s WHERE nome_administrador = %s'
                cursor.execute(query, (uIn_Endereco, uIn_NomeAdministrador)) # Altera o endereço do administrador na base de dados.
                print('Dados alterados com sucesso.')
                time.sleep(2)
                return menu_administrador()

            # Parâmetro Email
            elif parametro == 4:
                while True:
                    uIn_Email = input('\nDigite o email: ')
                    # Validação do email
                    if validacao_email(uIn_Email) == False:
                        print('Digite uma resposta válida')
                        continue
                    else:
                        break
                query = 'UPDATE administrador SET email_administrador = %s WHERE nome_administrador = %s'
                cursor.execute(query, (uIn_Email, uIn_NomeAdministrador)) # Altera o email do administrador na base de dados.
                print('Dados alterados com sucesso.')
                time.sleep(2)
                return menu_administrador()
        except:
            ExceptResponse(editar_administrador) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função