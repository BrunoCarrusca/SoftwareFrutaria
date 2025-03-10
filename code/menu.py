from administrador import *
from artigo import *
from fornecedor import *
from funcionario import *
from venda import *
import beaupy

# FUNÇÕES
def menu_administrador():
    '''
    Menu da Gestão do Administrador
    '''
    CLEAR()
    print('\nMenu Administrador\n')
    options = ['Adicionar Administrador', 'Editar Administrador', 'Eliminar Administrador', 'Voltar']
    while True:
        option = beaupy.select(options, return_index=True) + 1
        match option:
            case 1:
                return adicionar_administrador() # Adicionar novos administradores
            case 2:
                return editar_administrador() # Editar informações dos administradores existentes
            case 3:
                return eliminar_administrador() # Eliminar administradores
            case 4:
                return menu_principal() # Retornar ao menu principal do programa
            case _:
                print("\nErro: operação inválida\n")

def menu_artigo():
    '''
    Menu da Gestão dos Artigos
    '''
    CLEAR()
    print('\nMenu Artigo\n')
    options = ['Adicionar Artigo', 'Editar Artigo', 'Eliminar Artigo', 'Visualizar Artigos Mais Vendidos', 'Visualizar Stock', 'Visualizar Alertas de Reposição', 'Voltar']
    while True:
        option = beaupy.select(options, return_index=True) + 1
        match option:
            case 1:
                return adicionar_artigo() # Adicionar novos artigos
            case 2:
                return editar_artigo() # Editar informações dos artigos existentes
            case 3:
                return eliminar_artigo() # Eliminar artigos
            case 4:
                return artigos_mais_vendidos() # Visualizar os artigos mais vendidos de um período selecionado
            case 5:
                return visualizar_stock() # Visualizar o stock existente
            case 6:
                return alertas_reposicao()
            case 7:
                return menu_principal() # Retornar ao menu principal do programa
            case _:
                print("\nErro: operação inválida\n")

def menu_funcionario():
    '''
    Menu da Gestão do Funcionário
    '''
    CLEAR()
    print('\nMenu Funcionário\n')
    options = ['Adicionar Funcionário', 'Editar Funcionário', 'Eliminar Funcionário', 'Voltar']
    while True:
        option = beaupy.select(options, return_index=True) + 1
        match option:
            case 1:
                return adicionar_funcionario() # Adicionar novos funcionários
            case 2:
                return editar_funcionario() # Editar informações dos funcionários existentes
            case 3:
                return eliminar_funcionario() # Eliminar funcionários
            case 4:
                return menu_principal() # Retornar ao menu principal do programa
            case _:
                print("\nErro: operação inválida\n")

def menu_fornecedor():
    '''
    Menu da Gestão dos Fornecedores
    '''
    CLEAR()
    print('\nMenu Fornecedor\n')
    options = ['Adicionar Fornecedor', 'Editar Fornecedor', 'Eliminar Fornecedor', 'Visualizar Compras aos Fornecedores', 'Voltar']
    while True:
        option = beaupy.select(options, return_index=True) + 1
        match option:
            case 1:
                return adicionar_fornecedor() # Adicionar novos fornecedores
            case 2:
                return editar_fornecedor() # Editar informações dos fornecedores existentes
            case 3:
                return eliminar_fornecedor() # Eliminar fornecedores
            case 4:
                return compras_fornecedor() # Visualizar as últimas compras feitas aos fornecedores
            case 5:
                return menu_principal() # Retornar ao menu principal do programa
            case _:
                print("\nErro: operação inválida\n")

def menu_venda():
    '''
    Menu da Gestão das Vendas
    '''
    CLEAR()
    print('\nMenu Vendas\n')
    options = ['Adicionar Venda', 'Editar Venda', 'Visualizar Vendas', 'Previsão de Vendas', 'Voltar']
    while True:
        option = beaupy.select(options, return_index=True) + 1
        match option:
            case 1:
                return adicionar_venda() # Adiciona uma nova venda
            case 2:
                return editar_venda() # Editar informações sobre uma venda existente
            case 3:
                return visualizar_vendas_cliente() # Visualizar as últimas vendas
            case 4:
                return prever_vendas() # Realizar a previsão de vendas de um período selecionado
            case 5:
                return menu_principal() # Retornar ao menu principal do programa
            case _:
                print("\nErro: operação inválida\n")
                
def menu_principal():
    '''
    Menu Principal do Programa
    '''
    CLEAR()

    print('\nMenu Principal\n')
    options = ['Administrador', 'Artigo', 'Funcionário', 'Fornecedor', 'Vendas', 'Encerrar']
    opcao = beaupy.select(options, return_index=True) + 1
    while True:
        match opcao:
            case 1:
                return menu_administrador()
            case 2:
                return menu_artigo()
            case 3:
                return menu_funcionario()
            case 4:
                return menu_fornecedor()
            case 5:
                return menu_venda()
            case 6:
                return print('Obrigado por utilizar o programa!')
            case _:
                print("\nErro: operação inválida\n")

# GLOBALS
menu_principal()