import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean.db')

query = """
    WITH soma_user AS (
        SELECT
            Customer_ID,
            SUM(Total_Amount) AS valor_total
        FROM vendas2
        GROUP BY Customer_ID
    ),
    
    com_media AS (
        SELECT
            Customer_ID,
            valor_total,
            ROUND(AVG(valor_total) OVER (), 2) AS media_geral
        FROM soma_user
    )

    SELECT *
    FROM com_media
    WHERE valor_total >= media_geral;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()