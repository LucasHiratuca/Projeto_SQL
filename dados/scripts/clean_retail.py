import pandas as pd
import sqlite3

# ── 1. Ler o CSV original direto ──────────────────────────────────────────────
df = pd.read_csv('dados/raw_datasets/retail_sales_dataset.csv') # ajuste o sep se necessário

# ── 2. Limpar colunas ─────────────────────────────────────────────────────────
df.columns = df.columns.str.strip().str.replace(' ', '_')

# ── 3. Corrigir tipos ─────────────────────────────────────────────────────────
df['Age']            = pd.to_numeric(df['Age'],            errors='coerce')
df['Quantity']       = pd.to_numeric(df['Quantity'],       errors='coerce')
df['Price_per_Unit'] = pd.to_numeric(df['Price_per_Unit'], errors='coerce')
df['Date']           = pd.to_datetime(df['Date'],          errors='coerce')

# ── 4. Salvar no banco ────────────────────────────────────────────────────────
conn = sqlite3.connect('dados/processed/retail_sales_clean.db')  # ← linha correta?
df.to_sql('vendas2', conn, if_exists='replace', index=False)

print("✅ Importado direto, sem passar pelo Orange")
print(df.dtypes)
print(df.head())

conn.close()