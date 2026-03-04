#TOP 10 VENDAS ENTRE OS VALORES ACIMA DE 100

import pandas as pd
import sqlite3

# 1. Conectar com o db
conn = sqlite3.connect('dados/processed/retail_sales.db')

# 2. Executar uma query direto no Python
query = """
        SELECT "data", venda
        FROM vendas 
        WHERE venda > 100
        ORDER BY venda desc
        LIMIT 10;"""
resultado = pd.read_sql_query(query, conn)
print(resultado)


conn.close()

