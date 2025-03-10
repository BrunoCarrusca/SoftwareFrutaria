# Projeto Final CESAE Digital - Sistema de Gestão de Frutaria

Este projeto consiste num sistema de gestão para uma frutaria, desenvolvido em Python e utilizando uma base de dados MySQL. O sistema permite a gestão de administradores, funcionários, fornecedores, artigos, vendas e compras, oferecendo uma interface de linha de comandos para interação com o utilizador.

## Funcionalidades Principais

- **Gestão de Administradores**: Adicionar, editar e eliminar administradores.
- **Gestão de Funcionários**: Adicionar, editar e eliminar funcionários.
- **Gestão de Fornecedores**: Adicionar, editar e eliminar fornecedores, além de visualizar compras feitas aos fornecedores.
- **Gestão de Artigos**: Adicionar, editar e eliminar artigos, visualizar stock, gerar alertas de reposição e analisar os artigos mais vendidos.
- **Gestão de Vendas**: Adicionar e editar vendas, visualizar vendas realizadas e realizar previsões de vendas futuras.
- **Relatórios e Análises**: Exportar dados para ficheiros CSV, gerar gráficos de vendas e previsões de vendas.

## Estrutura do Projeto

O projeto está organizado em vários ficheiros Python, cada um responsável por uma funcionalidade específica:

- **administrador.py**: Gestão de administradores.
- **artigo.py**: Gestão de artigos e stock.
- **fornecedor.py**: Gestão de fornecedores e compras.
- **funcionario.py**: Gestão de funcionários.
- **funcoes_globais.py**: Funções utilitárias globais, como validação de dados e manipulação de ficheiros CSV.
- **menu.py**: Menu principal e submenus do sistema.
- **venda.py**: Gestão de vendas e previsões.

## Base de Dados

A base de dados MySQL foi criada utilizando o ficheiro `script_database_frutaria.sql`, que define as tabelas necessárias para o funcionamento do sistema. O ficheiro `insert_data_frutaria.sql` contém dados de exemplo para popular a base de dados.

### Tabelas Principais

- **fornecedor**: Armazena informações sobre os fornecedores.
- **administrador**: Armazena informações sobre os administradores.
- **cliente**: Armazena informações sobre os clientes.
- **funcionario**: Armazena informações sobre os funcionários.
- **artigo**: Armazena informações sobre os artigos disponíveis na frutaria.
- **venda_cliente**: Registra as vendas realizadas aos clientes.
- **compra_fornecedor**: Registra as compras feitas aos fornecedores.

## Requisitos

- Python 3.x
- MySQL
- Bibliotecas Python: `mysql-connector-python`, `pandas`, `matplotlib`, `scipy`, `beaupy`

## Instalação e Execução

1. **Configuração da Base de Dados**:
   - Execute o script `script_database_frutaria.sql` para criar a base de dados e as tabelas.
   - Execute o script `insert_data_frutaria.sql` para inserir dados de exemplo.

2. **Instalação das Dependências**:
   ```bash
   pip install mysql-connector-python pandas matplotlib scipy beaupy

Diagrama de Use Cases:
![drawio_software_frutaria](https://github.com/user-attachments/assets/78c3615a-8fc9-4777-bc94-91ba39f01602)

Diagrama de Classes:
![diagrama_classes](https://github.com/user-attachments/assets/50b042dd-253a-47f9-91ad-7d050925cf0d)
