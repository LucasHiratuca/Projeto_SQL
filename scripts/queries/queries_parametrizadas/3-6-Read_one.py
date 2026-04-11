import sqlite3
import pandas as pd

def read_vendas(conn, transaction_id: int, ano: str):
    query = """
        SELECT * 
        FROM vendas2 
        WHERE Transaction_ID = ? 
          AND strftime('%Y', Date) = ?
    """
    df = pd.read_sql_query(query, conn, params=(transaction_id, ano))
    
    if df.empty:
        print(f"⚠️ Nenhuma transação encontrada para ID {transaction_id} no ano {ano}")
    else:
        print(f"✅ Transação {transaction_id} encontrada no ano {ano}:")
        print(df)
    
    return df

if __name__ == "__main__":
    conn = None
    try:
        conn = sqlite3.connect("dados/processed/retail_sales_clean2.db")
        
        transaction_id = int(input("Digite o ID da transação: "))
        ano = input("Digite o ano (YYYY): ")
        
        read_vendas(conn, transaction_id, ano)
        
    except ValueError as e:
        print(f"❌ Erro de valor: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
    finally:
        if conn:
            conn.close()