import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
    WITH soma_user AS (
        SELECT
            Customer_ID,
            strftime('%Y', Date) AS ano_user,
            strftime('%m', Date) AS mes_user,
            SUM(Total_Amount) AS valor_total_user
        FROM vendas2
        GROUP BY Customer_ID, ano_user, mes_user
    ),
    
    ano_mes AS (
        SELECT
            SUM(Total_Amount) AS valor_total_mes,
            strftime('%Y', Date) AS ano_month,
            strftime('%m', Date) AS mes_month
        FROM vendas2
        GROUP BY ano_month, mes_month
    )

    SELECT 
        Customer_ID,
        ano_user,
        mes_user,
        valor_total_user,
        valor_total_mes,
        ROUND((CAST(s.valor_total_user AS FLOAT) / a.valor_total_mes * 100), 2) AS percentual_contribuicao
        FROM soma_user s
        JOIN ano_mes a ON s.ano_user = a.ano_month
        AND s.mes_user = a.mes_month;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()