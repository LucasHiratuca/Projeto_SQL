import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean.db')

query = """
    WITH compras_usuario AS (
        SELECT
            Customer_ID,
            SUM(Total_Amount) AS valor_total
        FROM vendas2
        GROUP BY Customer_ID     
    ) 
    SELECT 
        Customer_ID,
        valor_total  
    FROM compras_usuario 
    ORDER BY valor_total DESC
    LIMIT 10;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()