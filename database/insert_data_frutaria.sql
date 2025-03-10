USE frutaria;

INSERT INTO administrador(nome_administrador, num_telemovel_administrador, endereco_administrador, email_administrador)
VALUES ('João Silva', '+351912345678', 'Rua das Flores, 123, 1000-001 Lisboa, Portugal', 'joao.silva@example.com'),
    ('Maria Oliveira', '+351967891234', 'Avenida dos Aliados, 45, 4000-064 Porto, Portugal', 'maria.oliveira@example.com'),
    ('Carlos Mendes', '+351934567890', 'Praça da República, 10, 3000-002 Coimbra, Portugal', 'carlos.mendes@example.com');

INSERT INTO funcionario(nome_funcionario, num_telemovel_funcionario, endereco_funcionario, email_funcionario)
VALUES ('Pedro Ferreira', '+351911234567', 'Rua do Carmo, 15, 1100-099 Lisboa, Portugal', 'pedro.ferreira@example.com'),
    ('Sofia Martins', '+351926789012', 'Avenida da Liberdade, 200, 1250-001 Lisboa, Portugal', 'sofia.martins@example.com'),
    ('Ricardo Alves', '+351938765432', 'Rua da Paz, 30, 4150-580 Porto, Portugal', 'ricardo.alves@example.com'),
    ('Helena Ramos', '+351952341678', 'Rua das Oliveiras, 50, 2400-013 Leiria, Portugal', 'helena.ramos@example.com'),
    ('Tiago Nunes', '+351914567890', 'Rua do Mercado, 90, 2600-124 Vila Franca de Xira, Portugal', 'tiago.nunes@example.com'),
    ('Beatriz Rocha', '+351922345678', 'Avenida Marginal, 500, 2750-427 Cascais, Portugal', 'beatriz.rocha@example.com'),
    ('Fernando Lopes', '+351933214567', 'Rua das Amoreiras, 12, 1495-027 Oeiras, Portugal', 'fernando.lopes@example.com'),
    ('Cláudia Pinto', '+351945678901', 'Praça do Comércio, 1, 1100-148 Lisboa, Portugal', 'claudia.pinto@example.com');

INSERT INTO fornecedor(nome_fornecedor, num_telemovel_fornecedor, email_fornecedor, endereco_fornecedor)
VALUES ('Frutiverso Portugal', '+351921234567', 'contact@frutiversopt.com', 'Rua da Inovação, 10, 1000-050 Lisboa, Portugal'),
    ('Sabores do Pomar', '+351923456789', 'info@saborespomar.com', 'Avenida Verde, 20, 2000-100 Santarém, Portugal'),
    ('Horta Lusitana', '+351934567890', 'sales@hortalusitana.com', 'Rua do Progresso, 30, 3000-300 Coimbra, Portugal'),
    ('EcoFrutas Ibérica', '+351945678901', 'support@ecofrutasiberica.com', 'Estrada Rural, 40, 4000-400 Porto, Portugal'),
    ('Delícias da Terra', '+351956789012', 'hello@deliciasterrapt.com', 'Avenida do Mar, 50, 5000-500 Faro, Portugal');

INSERT INTO artigo(nome_artigo, quantidade_artigo, preco_artigo, id_fornecedor)
VALUES ('Maça Gala', 76, 1.69, 3),
    ('Laranja', 69, 1.29, 5),
    ('Pêra Rocha', 52, 1.99, 2),
    ('Kiwi', 43, 2.99, 4),
    ('Couve Coração de Boi', 29, 0.99, 1),
    ('Manga Maturada', 35, 2.19, 2),
    ('Morango', 50, 3.19, 3),
    ('Dióspiro', 48, 2.89, 4),
    ('Maçã', 50, 2.00, 1),
    ('Banana', 75, 1.50, 2),
    ('Abacaxi', 30, 3.50, 5),
    ('Melancia', 25, 1.20, 3),
    ('Limão', 80, 1.00, 4),
    ('Cereja', 15, 5.00, 2),
    ('Uva', 50, 3.50, 3),
    ('Pêssego', 45, 2.60, 4),
    ('Maracujá', 25, 4.20, 5),
    ('Framboesa', 10, 6.00, 1),
    ('Mandarina', 70, 1.70, 3),
    ('Mamão', 40, 2.90, 4),
    ('Figo', 30, 4.50, 5),
    ('Ameixa', 55, 2.50, 1),
    ('Pitaya', 10, 7.00, 3),
    ('Alho Seco', 20, 3.10, 4);

INSERT INTO cliente(nome_cliente, num_telemovel_cliente, endereco_cliente, email_cliente)
VALUES ('Miguel Santos', '+351912345671', 'Rua Nova, 12, 1200-123 Lisboa, Portugal', 'miguel.santos@example.com'),
    ('Laura Ferreira', '+351934567892', 'Avenida do Conhecimento, 45, 1500-456 Lisboa, Portugal', 'laura.ferreira@example.com'),
    ('André Costa', '+351947891234', 'Rua da Liberdade, 10, 4000-456 Porto, Portugal', 'andre.costa@example.com'),
    ('Sara Nogueira', '+351910234567', 'Avenida Principal, 123, 3000-678 Coimbra, Portugal', 'sara.nogueira@example.com'),
    ('Paulo Almeida', '+351926789012', 'Rua das Estrelas, 50, 8000-789 Faro, Portugal', 'paulo.almeida@example.com'),
    ('Carolina Mendes', '+351914567890', 'Praça do Sol, 90, 2500-123 Leiria, Portugal', 'carolina.mendes@example.com'),
    ('Inês Rocha', '+351911234567', 'Rua do Comércio, 21, 5000-456 Vila Real, Portugal', 'ines.rocha@example.com'),
    ('Ricardo Fonseca', '+351938765432', 'Praça Verde, 89, 3500-234 Viseu, Portugal', 'ricardo.fonseca@example.com'),
    ('Ana Lopes', '+351965432109', 'Rua das Flores, 123, 4100-789 Porto, Portugal', 'ana.lopes@example.com'),
    ('Helena Ribeiro', '+351952341678', 'Avenida Central, 45, 4700-098 Braga, Portugal', 'helena.ribeiro@example.com'),
    ('Tiago Martins', '+351914567891', 'Praça Nova, 67, 2300-123 Tomar, Portugal', 'tiago.martins@example.com'),
    ('Beatriz Gonçalves', '+351922345679', 'Rua do Horizonte, 12, 7600-234 Beja, Portugal', 'beatriz.goncalves@example.com');

INSERT INTO compra_fornecedor(id_artigo, id_administrador, id_fornecedor, quantidade_compra_fornecedor, preco_compra_fornecedor, preco_total_compra_fornecedor, data_compra_fornecedor, hora_compra_fornecedor)
VALUES (1, 1, 2, 7, 1.50, 10.5, '2025-01-10', '10:30:00'),
    (2, 2, 2, 5, 2.50, 12.5, '2025-01-11', '11:00:00'),
    (3, 3, 3, 45, 0.99, 44.55, '2025-01-12', '09:15:00'),
    (4, 1, 4, 20, 1.25, 25, '2025-01-13', '14:45:00'),
    (5, 2, 5, 15, 3.40, 51, '2025-01-14', '13:20:00'),
    (6, 3, 1, 30, 0.80, 24, '2025-01-15', '16:00:00'),
    (7, 1, 3, 10, 2.14, 21.4, '2025-01-16', '10:10:00');

INSERT INTO venda_cliente(id_cliente, id_artigo, id_funcionario, quantidade_venda_cliente, preco_venda_cliente, preco_total_venda_cliente, data_venda_cliente, hora_venda_cliente, metodo_pagamento)
VALUES (1, 3, 2, 5, 10.00, 50.00, '2025-01-01', '10:15:00', 'Cartão de Crédito'),
    (2, 5, 3, 2, 20.00, 40.00, '2025-01-02', '11:00:00', 'Dinheiro'),
    (3, 7, 1, 1, 15.50, 15.50, '2025-01-03', '09:45:00', 'Cartão de Débito'),
    (4, 9, 5, 3, 12.00, 36.00, '2025-01-04', '13:30:00', 'Multibanco'),
    (5, 12, 4, 4, 25.00, 100.00, '2025-01-05', '14:10:00', 'Cartão de Crédito'),
    (6, 10, 6, 2, 18.00, 36.00, '2025-01-06', '16:25:00', 'Dinheiro'),
    (7, 15, 7, 1, 30.00, 30.00, '2025-01-07', '17:45:00', 'Cartão de Débito'),
    (8, 18, 8, 6, 8.50, 51.00, '2025-01-08', '08:30:00', 'Cartão de Crédito'),
    (9, 20, 2, 3, 22.00, 66.00, '2025-01-09', '12:00:00', 'Multibanco'),
    (10, 23, 3, 5, 10.00, 50.00, '2025-01-10', '15:45:00', 'Dinheiro'),
    (11, 1, 1, 2, 50.00, 100.00, '2025-01-11', '10:10:00', 'Cartão de Crédito'),
    (12, 6, 2, 3, 25.00, 75.00, '2025-01-12', '11:15:00', 'Cartão de Débito'),
    (1, 8, 4, 4, 12.50, 50.00, '2025-01-13', '09:20:00', 'Multibanco'),
    (2, 11, 6, 5, 9.00, 45.00, '2025-01-14', '13:40:00', 'Dinheiro'),
    (3, 14, 8, 6, 7.50, 45.00, '2025-01-15', '15:30:00', 'Cartão de Crédito'),
    (4, 17, 1, 3, 20.00, 60.00, '2025-01-16', '14:15:00', 'Cartão de Débito'),
    (5, 19, 3, 2, 30.00, 60.00, '2025-01-17', '08:55:00', 'Multibanco'),
    (6, 22, 5, 1, 45.00, 45.00, '2025-01-18', '09:50:00', 'Dinheiro'),
    (7, 4, 7, 3, 12.00, 36.00, '2025-01-19', '10:45:00', 'Cartão de Crédito'),
    (8, 13, 2, 2, 15.00, 30.00, '2025-01-20', '13:20:00', 'Multibanco'),
    (9, 16, 4, 4, 22.50, 90.00, '2025-01-21', '16:30:00', 'Cartão de Débito'),
    (10, 21, 6, 6, 8.00, 48.00, '2025-01-22', '14:50:00', 'Cartão de Crédito'),
    (11, 2, 8, 1, 60.00, 60.00, '2025-01-23', '10:30:00', 'Dinheiro'),
    (12, 9, 3, 3, 25.50, 76.50, '2025-01-24', '11:40:00', 'Multibanco'),
    (1, 5, 7, 2, 20.00, 40.00, '2025-01-25', '12:15:00', 'Cartão de Débito');