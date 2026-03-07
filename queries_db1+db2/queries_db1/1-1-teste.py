import sqlite3
import pandas as pd

# Conecta 
conn = sqlite3.connect('dados/processed/retail_sales.db')

# 1. Executar uma query direto no Python
query = "SELECT * FROM vendas LIMIT 15;"
resultado = pd.read_sql_query(query, conn)
print(resultado)

# Fechar conexão
conn.close()
