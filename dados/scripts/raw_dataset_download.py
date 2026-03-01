import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Autenticar
api = KaggleApi()
api.authenticate()

# 2. Definir dataset (identificador do Kaggle)
dataset = "tevecsystems/retail-sales-forecasting"  

# 3. Criar pasta se não existir
os.makedirs("./dados/raw", exist_ok=True)

# 4. Baixar dataset
print(f"📥 Baixando {dataset}...")
api.dataset_download_files(dataset, path="./dados/dataset", unzip=True)
print("✅ Download concluído!")

# 5. Carregar o CSV baixado
csv_files = [f for f in os.listdir("./dados/dataset") if f.endswith('.csv')]
if csv_files:
    df = pd.read_csv(os.path.join("./dados/raw", csv_files[0]))
    print(f"📊 Dataset carregado: {csv_files[0]}")
    print(df.head())