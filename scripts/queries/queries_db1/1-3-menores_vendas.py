#TOP 10 MENORES VENDAS (Excluindo 0)

import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales1.db')

query = """
        SELECT venda, COUNT(venda) as frequencia
        FROM vendas 
        WHERE venda > 0
        GROUP BY venda
        ORDER BY venda ASC
        LIMIT 10;"""
resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()
