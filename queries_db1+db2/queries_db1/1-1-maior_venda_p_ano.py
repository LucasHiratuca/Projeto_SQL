import sqlite3
import pandas as pd

# Conecta 
conn = sqlite3.connect('dados/processed/retail_sales.db')

# 1. Executar uma query direto no Python
query = """
            WITH venda_ano AS (
                SELECT 
                    /* strftime('%y', data) AS ano, */
                    substr(data, 1, 4) AS ano,
                    venda * preco AS vendas_totais
                FROM vendas
            ),

            rankeamento AS ( 
                SELECT 
                    ano,
                    vendas_totais,
                    RANK() OVER (PARTITION BY ano ORDER BY vendas_totais DESC) AS ranks
                FROM venda_ano
            )

            SELECT 
                ano,
                vendas_totais,
                ranks
            FROM rankeamento
            WHERE ranks <= 3;
            """

resultado = pd.read_sql_query(query, conn)
print(resultado)

# Fechar conexão
conn.close()
