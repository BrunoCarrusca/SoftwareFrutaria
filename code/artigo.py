import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta
from funcoes_globais import *

# CONEXÕES
conn = mysql.connector.connect(user='root', host='localhost', database='frutaria', autocommit=True)
cursor = conn.cursor()

# FUNÇÕES
def query_artigo(): 
    '''
    Lista dos artigos
    '''
    ArtigoQuery = 'SELECT * FROM artigo'
    cursor.execute(ArtigoQuery)
    ListaArtigos = cursor.fetchall()
    return ListaArtigos

def adicionar_artigo():
    from fornecedor import adicionar_fornecedor, query_fornecedores
    from menu import menu_artigo
    CLEAR()
    print('\nAdicionar Artigo\n')
    ListaArtigos = query_artigo() # Lista de todos os artigos
    ListaFornecedores = query_fornecedores() # Lista de todos os fornecedores
    ListaNomesFornecedores = [fornecedor[1] for fornecedor in ListaFornecedores] # Lista dos nomes dos fornecedores

    try:
        # Formulário para adicionar o artigo
        while True:
            uIn_NomeArtigo = str(input('Digite o nome do artigo: ')).title()
            uIn_QuantidadeArtigo = str(input('Digite a quantidade em stock do artigo (Se for nula, digite 0): '))
            uIn_PrecoArtigo = str(input('Digite o preço do quilo do artigo escrito: '))
            uIn_Fornecedor = str(input('Digite o nome do fornecedor: '))
            # Validação dos inputs
            if validacao_nome(uIn_Fornecedor, uIn_NomeArtigo) and validacao_numerica(uIn_QuantidadeArtigo)[0] and validacao_numerica(uIn_PrecoArtigo)[0] == True:
                break
            else:
                continue
        
        for fornecedor in ListaFornecedores:
            if uIn_Fornecedor not in ListaNomesFornecedores: # Se o fornecedor não estiver registado na base de dados
                adicionar_fornecedor()

        if uIn_NomeArtigo not in ListaArtigos:
            for fornecedor in ListaFornecedores:
                if uIn_Fornecedor == fornecedor[1]: # Se o nome de um fornecedor estiver dentro da lista
                    uIn_fornecedorId = fornecedor[0] # A variável uIn_fornecedorId será o id do fornecedor que
                    break
            QueryTabelaArtigo = 'INSERT INTO artigo (nome_artigo, quantidade_artigo, preco_artigo, id_fornecedor) VALUES (%s, %s, %s, %s)'
            cursor.execute(QueryTabelaArtigo, (uIn_NomeArtigo, uIn_QuantidadeArtigo, uIn_PrecoArtigo, uIn_fornecedorId))
            print('\nArtigo adicionado com sucesso.')
            time.sleep(2)
            return menu_artigo()
        else:
            time.sleep(2)
            print('Este produto já se encontra na base de dados.')
    except:
        ExceptResponse(adicionar_artigo) # Se o utilizador introduzir um valor inválido a um campo, será reiniciado a função

def eliminar_artigo():
    from menu import menu_artigo
    CLEAR()
    print('\nEliminar Artigo\n')
    ListaArtigos = [artigo[1] for artigo in query_artigo()] # Lista dos nomes dos artigos

    try:
        while True:
            uIn_Nome = str(input('Digite o nome do artigo que deseja eliminar: '))
            # Validação do nome
            if validacao_nome(uIn_Nome) == True:
                break
            else:
                print('Digite uma resposta válida.')
                continue
        if uIn_Nome in ListaArtigos:
            query = 'DELETE FROM artigo WHERE nome_artigo = %s'
            cursor.execute(query, (uIn_Nome,))
            print('Artigo elmiminado com sucesso.')
            time.sleep(2)
            return menu_artigo()
        else:
            print('Artigo não existente na base de dados.')
            time.sleep(2)
            return menu_artigo()
    except:
        ExceptResponse(eliminar_artigo)

def editar_artigo():
    from menu import menu_artigo
    CLEAR()
    print('\nEditar Artigo\n')
    ListaArtigos = [artigo[1] for artigo in query_artigo()] # Lista dos nomes dos artigos

    while True:
        uIn_NomeArtigo = str(input('Digite o nome do artigo: '))
        # Validação do nome
        if validacao_nome(uIn_NomeArtigo) == False:
            continue
        else:
            break
    
    if uIn_NomeArtigo in ListaArtigos:
        while True:
            # Pergunta qual parâmetro a editar
            parametro = int(input('''Qual parâmetro você deseja editar? 
                    [1] Nome do Artigo
                    [2] Quantidade em Stock
                    [3] Preço
                    >  '''))
            try:
                if 1 <= int(parametro) <= 3:
                    break
                else:
                    print('Digite um número entre 1 e 3.')
                    continue
            except:
                print('Digite uma resposta válida')
                continue

        # Parâmetro Nome    
        if parametro == 1:
            while True:
                uIn_NovoNomeArtigo = input('\nDigite o nome do artigo: ').title()
                # Validação do nome
                if validacao_nome(uIn_NovoNomeArtigo) == False:
                    continue
                else:
                    break
            query = 'UPDATE artigo SET nome_artigo = %s WHERE nome_artigo = %s'
            cursor.execute(query, (uIn_NovoNomeArtigo, uIn_NomeArtigo)) # Altera o nome do artigo na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_artigo()

        # Parâmetro Quantidade
        elif parametro == 2:
            while True:
                uIn_Quantidade = input('\nDigite a nova quantidade em stock (em Kg): ')
                # Validação numérica
                if validacao_numerica(uIn_Quantidade)[0] == False:
                    continue
                else:
                    break
            uIn_Quantidade = float(validacao_numerica(uIn_Quantidade)[1])
            query = 'UPDATE artigo SET quantidade_artigo = %s WHERE nome_artigo = %s'
            cursor.execute(query, (uIn_Quantidade, uIn_NomeArtigo)) # Altera a quantidade em stock do artigo na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_artigo()

        # Parâmetro Preço
        elif parametro == 3:
            while True:
                uIn_Preco = input('\nDigite o novo preço do artigo: ')
                # Validação numérica
                if validacao_numerica(uIn_Preco)[0] == False:
                    continue
                else:
                    break
            uIn_Preco = float(validacao_numerica(uIn_Preco)[1])
            query = 'UPDATE artigo SET preco_artigo = %s WHERE nome_artigo = %s'
            cursor.execute(query, (uIn_Preco, uIn_NomeArtigo)) # Altera o preço do artigo na base de dados.
            print('Dados alterados com sucesso.')
            time.sleep(2)
            return menu_artigo()
        
def dicionario_artigos():
    '''
    Cria uma lista de dicionários onde cada dicionário é um artigo sendo as chaves dos dicionários os parâmetros de um artigo.
    '''
    ListaArtigos = query_artigo() # Lista de todas as informações de cada artigo
    lista_dicionario_artigos = []
    for artigo in ListaArtigos:
        dicionario_artigos = {
            'ID Artigo': artigo[0],
            'Nome': artigo[1],
            'Quantidade (Kg)': artigo[2],
            'Preço (Kg)': artigo[3]
        }
        lista_dicionario_artigos.append(dicionario_artigos)
    return lista_dicionario_artigos

def apresentacao_artigos(lista_dicionario_artigos: list):
    '''
    Visualização de forma organizada de cada artigo dentro da lista
    '''
    print('-' * 150)
    if len(lista_dicionario_artigos) == 0: # Se a lista estiver vazia, não irá mostrar resultados.
        return print('Não há resultados!')
    for artigo in lista_dicionario_artigos: # Mostra cada artigo de uma forma organizada
        print(f'''
        ID Artigo: {artigo['ID Artigo']}
        Nome: {artigo['Nome']}
        Quantidade (Kg): {artigo['Quantidade (Kg)']}Kg
        Preço (Kg): {artigo['Preço (Kg)']}€
        ''')
    print(f'\nForam encontrados {len(lista_dicionario_artigos)} registos.') # Mostra quantos registos há na pesquisa.
    print('-' * 150)

def visualizar_stock():
    '''
    Visualizar o stock existente
    '''
    from menu import menu_artigo
    CLEAR()
    print('\nVisualizar Stock\n')
    lista_dicionario_artigos = dicionario_artigos() # Resgasta a lista de dicionários com cada artigo
        
    time.sleep(2)
    print('Estes foram os artigos encontrados: ')
    apresentacao_artigos(lista_dicionario_artigos) # Apresentação dos artigos

    # Pergunta ao utilizador se ele deseja salvar o resultado num ficheiro csv
    while True:
        uIn_Response = input('Deseja salvar o resultado num ficheiro CSV? (S/N) ').lower()
        if uIn_Response == 's' or uIn_Response == 'n':
            break
        else:
            print('Digite uma resposta válida')
            continue
    if uIn_Response == 's':
        salvar_csv(f'stock_{datetime.date.today()}', lista_dicionario_artigos)
        time.sleep(2)
        return menu_artigo()
    elif uIn_Response == 'n':
        time.sleep(2)
        return menu_artigo()
    
def artigos_mais_vendidos():
    '''
    Gera o ranking dos artigos mais vendidos em um período selecionado (1 dia, 1 semana ou 1 mês)
    e exibe um gráfico de barras.
    '''
    from menu import menu_artigo
    try:
        while True:
            uIn_periodo = int(input('''Qual período você deseja analisar? 
                                    [1] 1 Dia
                                    [2] 1 Semana
                                    [3] 1 Mês
                                    > '''))

            # Definir o intervalo de tempo com base no período selecionado
            agora = datetime.datetime.now()
            if uIn_periodo == 1:
                periodo = 'dia'
                data_inicio = agora - timedelta(days=1)
                break
            elif uIn_periodo == 2:
                periodo = 'semana'
                data_inicio = agora - timedelta(weeks=1)
                break
            elif uIn_periodo == 3:
                periodo = 'mês'
                data_inicio = agora - timedelta(days=30)
                break
            else:
                print("Digite um número entre 1 e 3.")
                continue
    except:
        ExceptResponse(artigos_mais_vendidos)

    # Consulta SQL para obter o ranking dos artigos mais vendidos no período
    query = f'''
        SELECT a.nome_artigo AS artigo, SUM(v.quantidade_venda_cliente) AS total_vendido
        FROM venda_cliente v
        INNER JOIN artigo a ON v.id_artigo = a.id_artigo
        WHERE v.data_venda_cliente >= '{data_inicio.strftime('%Y-%m-%d')}'
        GROUP BY a.nome_artigo
        ORDER BY total_vendido DESC
        LIMIT 10;
    '''

    # Executar a consulta e carregar os resultados em um DataFrame
    df = pd.read_sql_query(query, conn)

    if df.empty:
        print("Nenhuma venda encontrada no período selecionado.")

    # Exibir o ranking
    print("Ranking dos Artigos Mais Vendidos:")
    print(df)

    # Gerar o gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df['artigo'], df['total_vendido'], color='orange', edgecolor='black')
    plt.title(f"Artigos Mais Vendidos - Último {periodo.capitalize()}", fontsize=16)
    plt.xlabel("Artigos", fontsize=12)
    plt.ylabel("Quantidade Vendida (Kg)", fontsize=12)
    plt.xticks(rotation=45, fontsize=10, ha='right')
    plt.tight_layout()

    # Adicionar os valores acima das barras
    for i, valor in enumerate(df['total_vendido']):
        plt.text(i, valor + 0.5, str(valor), ha='center', fontsize=10)

    # Exibir o gráfico
    plt.show()

    while True:
        uIn_voltar_menu = input('Deseja voltar ao menu? (S/N) ').lower()
        if validacao_nome(uIn_voltar_menu):
            if uIn_voltar_menu == 's':
                return menu_artigo()
            elif uIn_voltar_menu == 'n':
                time.sleep(2)
                continue
            else:
                print('Digite uma resposta válida')
                continue
        else:
            print('Digite uma resposta válida')
            continue
            

def alertas_reposicao():
    '''
    Função que mostra os artigos na lista para reposição
    '''
    from menu import menu_artigo
    CLEAR()
    print('\nAlertas de Reposição\n')
    
    # Solicitar ao utilizador a quantidade mínima permitida
    while True:
        try:
            quantidade_minima = float(input('Digite a quantidade mínima permitida (em Kg) para alerta de reposição: '))
            if quantidade_minima >= 0:
                break
            else:
                print('Por favor, insira um valor positivo.')
        except:
            print('Por favor, insira um valor numérico válido.')
            ExceptResponse(alertas_reposicao)
    
    # Obter a lista de artigos
    ListaArtigos = dicionario_artigos()
    
    # Filtrar os artigos que estão abaixo da quantidade mínima
    artigos_para_repor = [artigo for artigo in ListaArtigos if artigo['Quantidade (Kg)'] < quantidade_minima]
    
    # Mostrar os artigos que precisam de reposição
    if artigos_para_repor:
        print('\nArtigos que precisam de reposição:')
        apresentacao_artigos(artigos_para_repor)
    else:
        print('\nNenhum artigo precisa de reposição no momento.')
    
    # Perguntar ao utilizador se deseja salvar o resultado num ficheiro csv
    while True:
        uIn_Response = input('Deseja salvar o resultado num ficheiro CSV? (S/N) ').lower()
        if uIn_Response == 's' or uIn_Response == 'n':
            break
        else:
            print('Digite uma resposta válida')
            continue
    if uIn_Response == 's':
        salvar_csv(f'alerta_reposicao_{datetime.date.today()}', artigos_para_repor)
        time.sleep(2)
        return menu_artigo()
    elif uIn_Response == 'n':
        time.sleep(2)
        return menu_artigo()