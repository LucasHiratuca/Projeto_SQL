import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_ver2.db')

df = pd.read_sql_query("SELECT * FROM vendas2 LIMIT 100", conn)

# ── 1. Colunas ────────────────────────────────────────────────────────────────
print("=" * 50)
print("COLUNAS:")
print(df.columns.tolist())

# ── 2. Tipos de dados ─────────────────────────────────────────────────────────
print("=" * 50)
print("TIPOS:")
print(df.dtypes)

# ── 3. Nulos ──────────────────────────────────────────────────────────────────
print("=" * 50)
print("NULOS:")
print(df.isnull().sum())

# ── 4. Amostra dos dados ──────────────────────────────────────────────────────
print("=" * 50)
print("AMOSTRA (5 linhas):")
print(df.head())

# ── 5. Estatísticas básicas ───────────────────────────────────────────────────
print("=" * 50)
print("ESTATÍSTICAS:")
print(df.describe(include='all'))

conn.close()