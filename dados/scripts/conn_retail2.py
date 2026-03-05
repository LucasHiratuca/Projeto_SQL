# queries/02-maiores_vendas.py
import sqlite3
import pandas as pd

# 1. CONECTAR AO BANCO (linha única!)
conn = sqlite3.connect('../processed/retail_sales.db')

# 2. FAZER A QUERY (exemplo)
query = """
SELECT 
    Product Category,
    SUM(Quantity * Price per Unit) as total_vendas
FROM vendas
GROUP BY Product Category
ORDER BY total_vendas DESC
"""

# 3. EXECUTAR E VER RESULTADO
df = pd.read_sql(query, conn)
print(df)

# 4. FECHAR CONEXÃO
conn.close()