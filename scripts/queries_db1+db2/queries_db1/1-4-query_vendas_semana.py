

import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales1.db')

query = """
        SELECT 
        CASE strftime('%w', data)
            WHEN '0' THEN 'Domingo'
            WHEN '1' THEN 'Segunda'
            WHEN '2' THEN 'Terça'
            WHEN '3' THEN 'Quarta'
            WHEN '4' THEN 'Quinta'
            WHEN '5' THEN 'Sexta'
            WHEN '6' THEN 'Sábado'
        END as dia_semana,    
        AVG(venda) as media_vendas,
        MAX(venda) as maximo_vendas,
        SUM(venda) as total_vendas
        FROM vendas
        GROUP BY dia_semana
        ORDER BY total_vendas DESC;
        """

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()
