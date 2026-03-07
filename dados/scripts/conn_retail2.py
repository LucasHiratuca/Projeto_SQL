import os
import sqlite3
import pandas as pd

# 1. CONECTAR AO BANCO (linha única!)

csv_files = [f for f in os.listdir("./dados/clean_dataset") if f.endswith('.csv')]
if csv_files:
    df = pd.read_csv(os.path.join("./dados/clean_dataset", csv_files[0]))
    
    # Criar banco SQLite
    conn = sqlite3.connect('./dados/processed/retail_sales_ver2.db')
    df.to_sql('vendas2', conn, if_exists='replace', index=False)
    conn.close()
    
    print("✅ Banco SQLite criado em: ./dados/processed/retail_sales.db")
else:
    print("❌ Nenhum CSV encontrado")


# 4. FECHAR CONEXÃO
conn.close()