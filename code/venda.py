import os
import mysql.connector
from funcoes_globais import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from datetime import timedelta

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()
diretorio_atual = os.getcwd()

# FUNÇÕES
def query_venda():
    '''
    Lista de Todas as Vendas na base de dados
    '''
    query = 'SELECT * FROM venda_cliente'
    cursor.execute(query)
    ListaVendas = cursor.fetchall()
    return ListaVendas

def editar_venda_BD(id_venda: int, parametro: str, valor):
    '''
    Função que edita a venda na base de dados
    '''
    if parametro == 'preco_venda_cliente':
        query = 'UPDATE venda_cliente SET preco_venda_cliente = %s WHERE id_venda_cliente = %s'
        cursor.execute(query, (valor, id_venda))
        time.sleep(2)
        return print('Dados atualizados com sucesso')

    elif parametro == 'quantidade_venda_cliente':
        query = 'UPDATE venda_cliente SET quantidade_venda_cliente = %s WHERE id_venda_cliente = %s'
        cursor.execute(query, (valor, id_venda))
        time.sleep(2)
        return print('Dados atualizados com sucesso')

    elif parametro == 'metodo_pagamento':
        query = 'UPDATE venda_cliente SET quantidade_venda_cliente = %s WHERE id_venda_cliente = %s'
        cursor.execute(query, (valor, id_venda))
        time.sleep(2)
        return print('Dados atualizados com sucesso')

    elif parametro == 'id_cliente':
        query = 'UPDATE venda_cliente SET id_cliente = %s WHERE id_venda_cliente = %s'
        cursor.execute(query, (valor, id_venda))
        time.sleep(2)
        return print('Dados atualizados com sucesso')
        
    elif parametro == 'id_artigo':
        query = 'UPDATE venda_cliente SET id_artigo = %s WHERE id_venda_cliente = %s'
        cursor.execute(query, (valor, id_venda))
        time.sleep(2)
        return print('Dados atualizados com sucesso')

def editar_venda():
    from menu import menu_venda
    CLEAR()
    print('\nEditar Venda')
    ListaVendasId = [venda[0] for venda in query_venda()] # Lista dos IDs das vendas

    try:
        while True:
            uIn_IdVenda = int(input('Digite o ID da venda: '))
            # Verificação de se o a venda existe na base de dados
            if uIn_IdVenda in ListaVendasId:
                break
            else:
                print('Esta venda não existe na base de dados')
                continue
        
        while True:
            try:
                uIn_parametro = int(input('''Qual parâmetro você deseja editar?
                                        [1] Quantidade
                                        [2] Método de Pagamento
                                        [3] Preço (Kg) do Artigo
                                        [4] Cliente
                                        [5] Artigo
                                        > '''))
                # Validação do input ao parâmetro que o utilizador deseja editar
                if 1 <= uIn_parametro <= 5:
                    break
                else:
                    print('Digite um número entre 1 e 4.')
                    continue
            except:
                print('Digite uma resposta válida')
                continue
        
        # Parâmetro Quantidade
        if uIn_parametro == 1:
            while True:
                uIn_NovaQuantidade = input('Digite a nova quantidade: ')
                if validacao_numerica(uIn_NovaQuantidade)[0] == True:
                    editar_venda_BD(uIn_IdVenda, 'quantidade_venda_cliente', validacao_numerica(uIn_NovaQuantidade)[1])
                    return menu_venda()
                elif validacao_numerica(uIn_NovaQuantidade)[0] == False:
                    print('Digite um valor numérico.')
                    continue
                
        # Parâmetro Método Pagamento
        elif uIn_parametro == 2:
            while True:
                uIn_MetodoPagamento = int(input('''Digite qual método de pagamento foi usado:
                                            [1] Cartão de Crédito
                                            [2] Cartão de Débito
                                            [3] Dinheiro
                                            > '''))
                if uIn_MetodoPagamento == 1:
                    editar_venda_BD(uIn_IdVenda, 'metodo_pagamento', 'Cartão de Crédito')
                    return menu_venda()
                elif uIn_MetodoPagamento == 2:
                    editar_venda_BD(uIn_IdVenda, 'metodo_pagamento', 'Cartão de Débito')
                    return menu_venda()
                elif uIn_MetodoPagamento == 3:
                    editar_venda_BD(uIn_IdVenda, 'metodo_pagamento', 'Dinheiro')
                    return menu_venda()
                else:
                    print('Digite um número entre 1 e 3.')
                    continue

        # Parâmetro Preço Artigo     
        elif uIn_parametro == 3:
            while True:
                uIn_PrecoArtigo = float(input('Digite o novo preço do artigo: '))
                if validacao_numerica(uIn_PrecoArtigo)[0] == True: # Se o novo preço do artigo for um número
                    editar_venda_BD(uIn_IdVenda, 'preco_venda_cliente', uIn_PrecoArtigo)
                    return menu_venda()
                elif validacao_numerica(uIn_PrecoArtigo)[0] == False: # Se o novo preço do artigo não for um número
                    validacao_numerica(uIn_PrecoArtigo)[1] # Escreve a mensagem de erro e pergunta novamente o novo preço do artigo
                    continue
                
        # Parâmetro Cliente
        elif uIn_parametro == 4:
            while True:
                uIn_cliente = str(input('Digite o nome correto para o cliente: '))
                if validacao_nome(uIn_cliente) == True:
                    id_cliente_correto = get_id_cliente(uIn_cliente)[0]
                    editar_venda_BD(uIn_IdVenda, 'id_cliente', id_cliente_correto)
                    return menu_venda()
                else:
                    print('Este cliente não existe na base de dados.')
                    continue
                
        # Parâmetro Artigo
        elif uIn_parametro == 5:
            while True:
                uIn_artigo = str(input('Digite o nome correto do artigo: '))
                if validacao_nome(uIn_artigo) == True:
                    id_artigo_correto = get_info_artigo(uIn_artigo)[0][0]
                    editar_venda_BD(uIn_IdVenda, 'id_artigo', id_artigo_correto)
                    return menu_venda()
                else:
                    print('Este artigo não existe na base de dados')
                    continue
    except:
        ExceptResponse(editar_venda)
        
def dicionario_vendas():
    '''
    Criação de uma lista de dicionários onde cada dicionário é uma venda sendo as chaves dos dicionários os parâmetros de uma venda.
    '''
    ListaVendas = query_venda()
    lista_dicionario_vendas = []
    for venda in ListaVendas:
        dicionario_vendas = {
            'ID Venda': venda[0],
            'ID Cliente': venda[1],
            'ID Artigo': venda[2],
            'ID Funcionário': venda[3],
            'Quantidade (Kg)': venda[4],
            'Preço (Kg)': venda[5],
            'Preço Total': venda[6],
            'Data': venda[7],
            'Hora': venda[8],
            'Método de Pagamento': venda[9]
        }
        lista_dicionario_vendas.append(dicionario_vendas)
    return lista_dicionario_vendas

def apresentacao_vendas(lista_dicionario_vendas: list):
    '''
    Visualização de forma organizada de cada venda dentro da lista
    '''
    print('-' * 150)
    if len(lista_dicionario_vendas) == 0: # Se a lista estiver vazia, não irá mostrar resultados.
        return print('Não há resultados!')
    for venda in lista_dicionario_vendas: # Mostra cada venda de uma forma organizada
        print(f'''
        ID Venda: {venda['ID Venda']}
        ID Cliente: {venda['ID Cliente']}
        ID Artigo: {venda['ID Artigo']}
        ID Funcionário: {venda['ID Funcionário']}
        Quantidade (Kg): {venda['Quantidade (Kg)']}Kg
        Preço (Kg): {venda['Preço (Kg)']}€
        Preço Total: {venda['Preço Total']}€
        Data: {venda['Data']}
        Hora: {venda['Hora']}
        Método de Pagamento: {venda['Método de Pagamento']}
        ''')
    print(f'\nForam encontrados {len(lista_dicionario_vendas)} registos.') # Mostra quantos registos há na pesquisa.
    print('-' * 150)

def visualizar_vendas_cliente():
    '''
    Visualizar as últimas vendas feitas aos clientes
    '''
    from menu import menu_venda
    CLEAR()
    print('\nVisualizar Vendas\n')
    ListaDicionarioVendas = dicionario_vendas() # Cria uma lista de dicionários com todas as vendas em detalhe
    
    time.sleep(2)
    CLEAR()
    print('Estes foram os registos de vendas encontrados: ')
    apresentacao_vendas(ListaDicionarioVendas) # Apresentação das vendas
    
    # Pergunta ao utilizador se ele deseja salvar a pesquisa num ficheiro csv
    while True:
        try:
            uIn_Response = input('Deseja salvar o resultado num ficheiro CSV? (S/N) ').lower()
            if uIn_Response == 's' or uIn_Response == 'n':
                break
            else:
                print('Digite uma resposta válida')
                continue
        except:
            print('Digite uma resposta válida')

    if uIn_Response == 's':
        salvar_csv(f'pesquisa_vendas_{datetime.date.today()}', ListaDicionarioVendas)
        time.sleep(2)
        return menu_venda()
    elif uIn_Response == 'n':
        time.sleep(2)
        return menu_venda()

def adicionar_venda():
    CLEAR()
    print('\nAdicionar Venda\n')

    try:
        # Formulário de venda
        while True:
            uIn_cliente = str(input('Digite o nome do cliente: ')).title()
            uIn_Artigo = str(input('Digite o artigo comprado: ')).title()
            uIn_Funcionario = str(input('Digite o nome do funcionário: ')).title()
            uIn_Quantidade = str(input('Digite a quantidade comprada pelo cliente: '))
            uIn_MetodoPagamento = int(input('''Digite qual método de pagamento foi usado:
                                            [1] Cartão de Crédito
                                            [2] Cartão de Débito
                                            [3] Dinheiro
                                            > '''))
            if 1 <= uIn_MetodoPagamento <= 4:
                break
            else:
                print('Digite um número entre 1 e 4')
                continue
    except:
        ExceptResponse(adicionar_venda) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função

    # Validação dos inputs
    if validacao_nome(uIn_cliente, uIn_Funcionario, uIn_Artigo) == True:
        if validacao_numerica(uIn_Quantidade)[0] == True:
            uIn_Quantidade = validacao_numerica(uIn_Quantidade)[1]
            if uIn_MetodoPagamento == 1:
                inserir_venda_BD(uIn_cliente, uIn_Artigo, uIn_Funcionario, uIn_Quantidade, 'Cartão de Crédito')
            elif uIn_MetodoPagamento == 2:
                inserir_venda_BD(uIn_cliente, uIn_Artigo, uIn_Funcionario, uIn_Quantidade, 'Cartão de Débito')
            elif uIn_MetodoPagamento == 3:
                inserir_venda_BD(uIn_cliente, uIn_Artigo, uIn_Funcionario, uIn_Quantidade, 'Dinheiro')
        else:
            ExceptResponse(adicionar_venda)
    else:
        ExceptResponse(adicionar_venda)

def atualizar_tabela_artigo(id_artigo: int, quantidade: float):
    '''
    Atualiza a quantidade de um artigo quando há uma venda a um cliente ou se há uma compra a um fornecedor
    '''
    # Pega a quantidade existente em estoque
    query = 'SELECT quantidade_artigo FROM artigo WHERE id_artigo = %s'
    cursor.execute(query, (id_artigo,))
    quantidade_existente = float(cursor.fetchall()[0][0])

    # Faz o cálculo para saber qual será a nova quantidade após a venda para o cliente
    quantidade_nova = quantidade_existente - quantidade

    # Atualiza a quantidade na base de dados
    query = 'UPDATE artigo SET quantidade_artigo = %s WHERE id_artigo = %s'
    cursor.execute(query, (quantidade_nova, id_artigo))
    return True

def inserir_venda_BD(uIn_cliente, uIn_Artigo, uIn_Funcionario, uIn_Quantidade, uIn_MetodoPagamento):
    '''
    Função que serve para inserir uma venda a base de dados
    '''
    from menu import menu_venda
    id_cliente = get_id_cliente(uIn_cliente)[0] # Função que resgasta o id do cliente
    id_artigo = get_info_artigo(uIn_Artigo)[0][0] # Função que resgata o id do artigo
    id_funcionario = get_id_funcionario(uIn_Funcionario)[0] # Função que resgasta o id do funcionário

    quantidade_venda_cliente = uIn_Quantidade # Quantidade comprada pelo cliente
    preco_venda_cliente = get_info_artigo(uIn_Artigo)[0][1] # Função que resgasta o preço do artigo
    preco_total_venda_cliente = float(preco_venda_cliente) * float(quantidade_venda_cliente) # O preço total da compra é o preço do quilo do artigo * quantidade levada pelo cliente
    preco_total_venda_cliente = round(preco_total_venda_cliente, 2)

    data_venda_cliente = datetime.date.today() # Data da compra
    hora_venda_cliente = datetime.datetime.now().time() # Hora da compra
    metodo_pagamento = uIn_MetodoPagamento # Método de pagamento do cliente
    query = 'INSERT INTO venda_cliente(id_cliente, id_artigo, id_funcionario, quantidade_venda_cliente, preco_venda_cliente, preco_total_venda_cliente, data_venda_cliente, hora_venda_cliente, metodo_pagamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(query, (id_cliente, id_artigo, id_funcionario, quantidade_venda_cliente, preco_venda_cliente, preco_total_venda_cliente, data_venda_cliente, hora_venda_cliente, metodo_pagamento))
    atualizar_tabela_artigo(id_artigo=int(id_artigo), quantidade=float(quantidade_venda_cliente)) # Função que atualiza automaticamente o estoque do artigo, retirando a quantidade que o cliente levou
    print('\nVenda registada com sucesso!')
    time.sleep(2)
    return menu_venda()
    
def prever_vendas():
    '''
    Realiza previsões de qual valor será obtido e qual a quantidade de produtos vendidos no dia/semana/mês seguinte
    '''
    from menu import menu_venda
    # Carregar os dados de vendas
    ListaDicionarioVendas = dicionario_vendas()
    vendas = pd.DataFrame(ListaDicionarioVendas)
    data_inicio = datetime.date.today()

    try:
        while True:
            uIn_periodo_analise = int(input('''Qual será o período desejado para a análise?
                                            [1] 1 dia
                                            [2] 1 semana
                                            [3] 1 mês
                                            > '''))
            if 1 <= uIn_periodo_analise <= 3:
                break
            else:
                print('Digite um número entre 1 e 3')
                continue
    except:
        ExceptResponse(prever_vendas)    
    
    # Filtrar os dados para o período de análise
    if uIn_periodo_analise == 1:
        data_fim = data_inicio + timedelta(days=1)
    elif uIn_periodo_analise == 2:
        data_fim = data_inicio + timedelta(weeks=1)
    elif uIn_periodo_analise == 3:
        data_fim = data_inicio + timedelta(weeks=4)
    
    vendas_periodo = vendas[(vendas['Data'] >= data_inicio) & (vendas['Data'] < data_fim)]
    
    # Preparar os dados para a regressão linear
    X = np.array(range(len(vendas_periodo)))
    y_valor = [float(valor) for valor in vendas_periodo['Preço Total'].values]
    y_quantidade = [float(quantidade) for quantidade in vendas_periodo['Quantidade (Kg)'].values]
    
    # Realizar a regressão linear para o valor total de vendas
    rl_valor = stats.linregress(X, y_valor)
    slope_valor = rl_valor.slope
    intercept_valor = rl_valor.intercept
    
    # Realizar a regressão linear para a quantidade vendida
    rl_quantidade = stats.linregress(X, y_quantidade)
    slope_quantidade = rl_quantidade.slope
    intercept_quantidade = rl_quantidade.intercept
    
    # Prever os valores para o próximo período
    X_futuro = len(vendas_periodo)
    valor_previsto = slope_valor * X_futuro + intercept_valor
    quantidade_prevista = slope_quantidade * X_futuro + intercept_quantidade
    
    # Gerar gráficos
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X, y_valor, color='blue', label='Dados Reais')
    plt.plot(X, slope_valor * X + intercept_valor, color='red', label='Regressão Linear')
    plt.title('Previsão do Valor Total de Vendas')
    plt.xlabel('Dias')
    plt.ylabel('Valor Total de Vendas (€)')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.scatter(X, y_quantidade, color='green', label='Dados Reais')
    plt.plot(X, slope_quantidade * X + intercept_quantidade, color='orange', label='Regressão Linear')
    plt.title('Previsão da Quantidade Vendida')
    plt.xlabel('Dias')
    plt.ylabel('Quantidade Vendida (Kg)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f'''Valor previsto de vendas: {valor_previsto :.2f}€ 
Quantidade prevista vendida: {quantidade_prevista :.3f} Kg''')
    time.sleep(6)
    return menu_venda()