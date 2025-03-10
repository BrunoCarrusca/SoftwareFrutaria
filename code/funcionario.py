import mysql.connector
import os
from funcoes_globais import *

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()
diretorio_atual = os.getcwd()

# FUNÇÕES
def query_funcionario():
    '''
    Lista dos funcionários
    '''
    FuncionarioQuery = 'SELECT * FROM funcionario'
    cursor.execute(FuncionarioQuery)
    ListaFuncionarios = cursor.fetchall()
    return ListaFuncionarios

def adicionar_funcionario():
    from menu import menu_funcionario
    CLEAR()
    print('\nAdicionar Funcionário\n')
    ListaNomesFuncionarios = [funcionario[1] for funcionario in query_funcionario()] # Lista dos nomes de todos os funcionários

    try:
        # Formulário
        while True:
            uIn_NomeFuncionario = str(input('Digite o nome do funcionário: ')).title()
            uIn_NumTelemovelFunc = str(input('Digite o número de telemóvel: '))
            uIn_EnderecoFunc = str(input('Digite o endereço: '))
            uIn_EmailFunc = str(input('Digite o email: '))
            # Validação dos inputs
            if validacao_nome(uIn_NomeFuncionario) and validacao_num_telemovel(uIn_NumTelemovelFunc) and validacao_email(uIn_EmailFunc) == True:
                break
            else:
                continue
        if uIn_NomeFuncionario not in ListaNomesFuncionarios:
            query = 'INSERT INTO funcionario(nome_funcionario, num_telemovel_funcionario, endereco_funcionario, email_funcionario) VALUES (%s, %s, %s, %s)'
            cursor.execute(query, (uIn_NomeFuncionario, uIn_NumTelemovelFunc, uIn_EnderecoFunc, uIn_EmailFunc))
            print('\nFuncionário adicionado com sucesso.')
            time.sleep(2)
            return menu_funcionario()
        else:
            print('Este funcionário já se encontra na base de dados.')
    except:
        ExceptResponse(adicionar_funcionario) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função

def eliminar_funcionario():
    from menu import menu_funcionario
    CLEAR()
    print('\nEliminar Funcionário\n')
    ListaNomesFuncionarios = [funcionario[1] for funcionario in query_funcionario()] # Lista de todos os nomes dos funcionários

    try:
        while True:
            uIn_NomeFuncionario = str(input('Digite o nome do funcionário que deseja eliminar: '))
            # Validação do nome
            if validacao_nome(uIn_NomeFuncionario) == True:
                break
            else:
                print('Digite uma resposta válida')
                continue
        if uIn_NomeFuncionario in ListaNomesFuncionarios:
            query = 'DELETE FROM funcionario WHERE nome_funcionario = %s'
            cursor.execute(query, (uIn_NomeFuncionario,))
            print('Funcionário elmiminado com sucesso.')
            time.sleep(2)
            return menu_funcionario()
        else:
            print('Funcionário não existente na base de dados.')
            time.sleep(2)
            return eliminar_funcionario()
    except:
        ExceptResponse(eliminar_funcionario)

def editar_funcionario():
    from menu import menu_funcionario
    CLEAR()
    print('\nEditar Funcionário\n')
    ListaNomesFuncionarios = [funcionario[1] for funcionario in query_funcionario()] # Lista de todos os nomes dos funcionários

    while True:
        uIn_NomeFuncionario = str(input('Digite o nome do funcionário: ')).title()
        # Validação do nome
        if validacao_nome(uIn_NomeFuncionario) == False:
            print('Digite um nome válido.')
            continue
        else:
            break
    
    if uIn_NomeFuncionario in ListaNomesFuncionarios:
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
        
        # Parâmetro Nome
        if parametro == 1:
            while True:
                uIn_NovoNomeFuncionario = input('\nDigite o nome completo: ').title()
                # Validação do nome
                if validacao_nome(uIn_NomeFuncionario) == False:
                    continue
                else:
                    break
            query = 'UPDATE funcionario SET nome_funcionario = %s WHERE nome_funcionario = %s'
            cursor.execute(query, (uIn_NovoNomeFuncionario, uIn_NomeFuncionario)) # Altera o nome do funcionário na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_funcionario()

        # Parâmetro Número Telemóvel
        elif parametro == 2:
            while True:
                uIn_NumTelemovel = input('\nDigite o novo número de telemóvel: ')
                # Validação do número de telemóvel
                if validacao_num_telemovel(uIn_NumTelemovel) == False:
                    continue
                else:
                    break
            query = 'UPDATE funcionario SET num_telemovel_funcionario = %s WHERE nome_funcionario = %s'
            cursor.execute(query, (uIn_NumTelemovel, uIn_NomeFuncionario)) # Altera o número de telemóvel do funcionário na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_funcionario()

        # Parâmetro Endereço
        elif parametro == 3:
            uIn_Endereco = input('\nDigite o endereço: ')
            query = 'UPDATE funcionario SET endereco_funcionario = %s WHERE nome_funcionario = %s'
            cursor.execute(query, (uIn_Endereco, uIn_NomeFuncionario)) # Altera o número de telemóvel do funcionário na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_funcionario()

        # Parâmetro Email
        elif parametro == 4:
            while True:
                uIn_Email = input('\nDigite o email: ')
                # Validação do email
                if validacao_email(uIn_Email) == False:
                    continue
                else:
                    break
            query = 'UPDATE funcionario SET email_funcionario = %s WHERE nome_funcionario = %s'
            cursor.execute(query, (uIn_Email, uIn_NomeFuncionario)) # Altera o email do funcionário na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_funcionario()