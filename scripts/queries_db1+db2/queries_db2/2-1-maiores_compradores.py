import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
    WITH compras_usuario AS (
        SELECT
            Customer_ID,
            SUM(Total_Amount) AS valor_total,
            DENSE_RANK() OVER (ORDER BY SUM(Total_Amount) DESC) AS rank
        FROM vendas2
        GROUP BY Customer_ID     
    ) 
    SELECT 
        Customer_ID,
        valor_total,
        rank  
    FROM compras_usuario 
    WHERE rank <= 10
    ORDER BY valor_total DESC;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()