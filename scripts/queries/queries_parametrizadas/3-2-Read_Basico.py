import sqlite3
import pandas as pd

def select_vendas(conn) -> pd.DataFrame:

    query = """
        SELECT * 
        FROM vendas2
        LIMIT 10;
    """

    df = pd.read_sql_query(query, conn)
    print(f"✅ {len(df)} registros lidos com sucesso!")
    return df


if __name__ == "__main__":
    conn = sqlite3.connect("dados/processed/retail_sales_clean2.db")
    try:
        df = select_vendas(conn)
        print(df)

    except ValueError as e:
        print(f"❌ Erro de valor — limite deve ser um número inteiro: {e}")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    finally:
        conn.close()