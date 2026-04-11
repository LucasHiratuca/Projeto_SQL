import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales_clean2.db')

query = """
    WITH ano_mes AS (
        SELECT
            SUM(Total_Amount) AS valor_total,
            substr(Date, 1, 4) AS ano,
            strftime('%m', Date) AS mes
        FROM vendas2
        GROUP BY ano, mes
    )
    
    SELECT 
        ano,
        mes,
        valor_total,
        SUM(valor_total) OVER (ORDER BY ano, mes) AS acumulado_global,
        SUM(valor_total) OVER (PARTITION BY ano ORDER BY mes) AS acumulado_anual
    FROM ano_mes;
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()