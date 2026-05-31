-- ==========================================
-- CRIAÇÃO DA TABELA PRINCIPAL DE ESTOQUE
-- ==========================================

CREATE TABLE estoque_producao (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    quantidade_estoque INT,
    quantidade_minima INT,
    unidade VARCHAR(20),
    preco_unitario DECIMAL(10,2),
    fornecedor VARCHAR(100),
    ultima_atualizacao DATE,
    linha_producao VARCHAR(50),
    status VARCHAR(20)
);

-- ==========================================
-- (OPCIONAL) INSERÇÃO DE EXEMPLO
-- ==========================================

INSERT INTO estoque_producao (
    id_produto,
    nome_produto,
    categoria,
    quantidade_estoque,
    quantidade_minima,
    unidade,
    preco_unitario,
    fornecedor,
    ultima_atualizacao,
    linha_producao,
    status
) VALUES
(1, 'Fio Algodão', 'Têxtil', 120, 50, 'kg', 12.50, 'Fornecedor A', '2026-05-25', 'Linha 1', 'OK'),
(2, 'Tecido Jeans', 'Têxtil', 30, 40, 'm', 25.00, 'Fornecedor B', '2026-05-25', 'Linha 2', 'CRÍTICO'),
(3, 'Elástico Industrial', 'Acessório', 200, 80, 'm', 3.50, 'Fornecedor C', '2026-05-25', 'Linha 1', 'OK');

-- ==========================================
-- RELATÓRIO: VALOR TOTAL EM ESTOQUE
-- ==========================================

SELECT
    id_produto,
    nome_produto,
    quantidade_estoque,
    preco_unitario,
    (quantidade_estoque * preco_unitario) AS valor_total
FROM estoque_producao
ORDER BY valor_total DESC;

-- ==========================================
-- PRODUTOS ABAIXO DO ESTOQUE MÍNIMO
-- ==========================================

SELECT
    id_produto,
    nome_produto,
    quantidade_estoque,
    quantidade_minima,
    fornecedor
FROM estoque_producao
WHERE quantidade_estoque < quantidade_minima
ORDER BY quantidade_estoque ASC;

-- ==========================================
-- ANÁLISE POR CATEGORIA
-- ==========================================

SELECT
    categoria,
    COUNT(id_produto) AS total_produtos,
    SUM(quantidade_estoque) AS estoque_total,
    AVG(preco_unitario) AS preco_medio
FROM estoque_producao
GROUP BY categoria
ORDER BY estoque_total DESC;

-- ==========================================
-- ANÁLISE POR LINHA DE PRODUÇÃO
-- ==========================================

SELECT
    linha_producao,
    COUNT(id_produto) AS total_produtos,
    SUM(quantidade_estoque) AS estoque_total
FROM estoque_producao
GROUP BY linha_producao
ORDER BY estoque_total DESC;

-- ==========================================
-- PRODUTOS EM STATUS CRÍTICO
-- ==========================================

SELECT
    id_produto,
    nome_produto,
    quantidade_estoque,
    quantidade_minima,
    status
FROM estoque_producao
WHERE status = 'CRÍTICO'
ORDER BY quantidade_estoque ASC;