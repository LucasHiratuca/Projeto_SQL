import pandas as pd
import sqlite3

conn = sqlite3.connect('dados/processed/retail_sales.db')

query = """
        WITH vendas_classificadas AS (
            SELECT
                venda,
                CASE strftime('%m', data)
                    WHEN '01' THEN 'Janeiro'
                    WHEN '02' THEN 'Fevereiro'
                    WHEN '03' THEN 'Março'
                    WHEN '04' THEN 'Abril'
                    WHEN '05' THEN 'Maio'
                    WHEN '06' THEN 'Junho'
                    WHEN '07' THEN 'Julho'
                    WHEN '08' THEN 'Agosto'
                    WHEN '09' THEN 'Setembro'
                    WHEN '10' THEN 'Outubro'
                    WHEN '11' THEN 'Novembro'
                    WHEN '12' THEN 'Dezembro'
                END as mes,
                strftime('%m', data) AS mes_numerado
                FROM vendas
        ),

        vendas_agrupadas AS (
            SELECT 
                mes,
                mes_numerado,
                SUM(venda) AS vendas_totais
                FROM vendas_classificadas
                GROUP BY mes, mes_numerado
        )

        SELECT
            v1.mes,
            v1.vendas_totais,
            CASE 
            WHEN v1.mes = 'Janeiro' THEN
            -- Para Janeiro: compara com Dezembro (v2)
                CASE 
                    WHEN v1.vendas_totais > v2.vendas_totais THEN 'Superior🔥'
                    WHEN v1.vendas_totais < v2.vendas_totais THEN 'Inferior💔'
                    ELSE 'Igual☁️'
                END
                ELSE
            -- Para outros meses: compara com o anterior usando LAG
                CASE 
                    WHEN v1.vendas_totais > LAG(v1.vendas_totais) OVER (ORDER BY v1.mes_numerado) THEN 'Superior🔥'
                    WHEN v1.vendas_totais < LAG(v1.vendas_totais) OVER (ORDER BY v1.mes_numerado) THEN 'Inferior💔'
                    ELSE 'Igual☁️'
                END
            END as status
            FROM vendas_agrupadas v1
            LEFT JOIN vendas_agrupadas v2 ON v2.mes = 'Dezembro'
            ORDER BY v1.mes_numerado ASC; """

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()