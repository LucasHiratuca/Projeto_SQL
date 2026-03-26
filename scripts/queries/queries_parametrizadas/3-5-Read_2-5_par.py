import sqlite3
import pandas as pd

def select_vendas(conn) -> pd.DataFrame:

    query = """
    WITH por_receita AS (
        SELECT
            Product_Category,
            SUM(Total_Amount) AS valor,
            RANK() OVER (ORDER BY SUM(Total_Amount) DESC) AS rank_receita
        FROM vendas2
        GROUP BY Product_Category
    ),

    por_quantidade AS (
        SELECT
            Product_Category,
            COUNT(*) AS valor,
            RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_quantidade
        FROM vendas2
        GROUP BY Product_Category
    )

    SELECT
        r.Product_Category,
        r.valor AS receita,
        q.valor AS quantidade,
        r.rank_receita,
        q.rank_quantidade
    FROM por_receita r
    JOIN por_quantidade q ON r.Product_Category = q.Product_Category
    ORDER BY r.rank_receita;
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