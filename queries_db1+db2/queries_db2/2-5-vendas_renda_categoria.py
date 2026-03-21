import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean.db')

query = """
    WITH por_receita AS (
        SELECT
            Product_Category,
            SUM(Total_Amount) AS valor,
            DENSE_RANK() OVER (ORDER BY SUM(Total_Amount) DESC) AS rank_receita
        FROM vendas2
        GROUP BY Product_Category
    ),

    por_quantidade AS (
        SELECT
            Product_Category,
            COUNT(*) AS valor,
            DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rank_quantidade
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

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()