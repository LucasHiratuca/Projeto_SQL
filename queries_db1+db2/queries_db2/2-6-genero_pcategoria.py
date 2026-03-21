import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean.db')

query = """
    WITH masc_cat AS (
        SELECT
            Gender,
            Product_Category,
            COUNT(*) AS qnt_masc
        FROM vendas2
        WHERE Gender = 'Male'
        GROUP BY Product_Category
    ),

    fem_cat AS (
        SELECT
            Gender,
            Product_Category,
            COUNT(*) AS qnt_fem
        FROM vendas2
        WHERE Gender = 'Female'
        GROUP BY Product_Category
    )

    SELECT
        m.Product_Category,
        ROUND((CAST(m.qnt_masc AS FLOAT) / (m.qnt_masc + f.qnt_fem) * 100), 2) AS porc_masc,
        ROUND((CAST(f.qnt_fem AS FLOAT) / (m.qnt_masc + f.qnt_fem) * 100), 2) AS porc_fem
    FROM masc_cat m
    JOIN fem_cat f ON m.Product_Category = f.Product_Category;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()