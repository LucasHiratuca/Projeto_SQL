import os
import pandas as pd
import sqlite3
from kaggle.api.kaggle_api_extended import KaggleApi

# Autenticar
api = KaggleApi()
api.authenticate()

# Dataset
dataset = "tevecsystems/retail-sales-forecasting"

# Pastas
os.makedirs("./dados/dataset", exist_ok=True)
os.makedirs("./dados/processed", exist_ok=True)

# Download
print("📥 Baixando dataset...")
api.dataset_download_files(dataset, path="./dados/dataset", unzip=True)

# Carregar CSV
csv_files = [f for f in os.listdir("./dados/dataset") if f.endswith('.csv')]
if csv_files:
    df = pd.read_csv(os.path.join("./dados/dataset", csv_files[0]))
    
    # Criar banco SQLite
    conn = sqlite3.connect("./dados/processed/retail_sales.db")
    df.to_sql('vendas', conn, if_exists='replace', index=False)
    conn.close()
    
    print("✅ Banco SQLite criado em: ./dados/processed/retail_sales.db")
else:
    print("❌ Nenhum CSV encontrado")