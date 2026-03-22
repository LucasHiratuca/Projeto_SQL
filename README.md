<div align="center">
  
  # 📊 Análise de Vendas no Varejo
  
  [![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
  [![Orange](https://img.shields.io/badge/Orange-3.38%2B-orange)](https://orange.biolab.si/)
  [![SQLite](https://img.shields.io/badge/SQLite-3-003B57)](https://www.sqlite.org/)
  [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

</div>

## 📌 Sobre o Projeto

Projeto focado em engenharia de dados, com ênfase em queries SQL avançadas aplicadas a um pipeline simples de ingestão e análise. O objetivo é demonstrar o uso de CTEs, Window Functions e JOINs em um contexto de dados reais — estrutura que pode ser
diretamente aplicada em ferramentas como dbt, Airflow ou Spark SQL.

---

## 📐 Conceitos SQL Aplicados

| Conceito | Onde foi usado |
|---|---|
| **CTE** (`WITH`) | Todas as queries do banco 2 + Queries 1 e 5 do primeiro banco |
| **Window Functions** (`OVER`) | Receita acumulada, ranking de categorias |
| **Self JOIN** | Comparação com mês de referência em vendas mensais (Query 1-5) |
| **JOIN** | Percentual por cliente no mês, gênero por categoria |
**LAG** | Comparação de vendas mês a mês (banco 1) |
| **DENSE_RANK()** | Ranking de categorias por quantidade e receita |
| **CASE WHEN** | Tradução de dia numérico para nome da semana |
| **strftime/substr** | Extração de ano, mês e dia da semana de datas |
| **Divisão inteira** | Correção com `* 1.0` para porcentagens corretas |

---

## 🗂️ Estrutura do Projeto
```
TREINO_SQL/
├── dados/
│   ├── processed/                  # Bancos de dados SQLite prontos para análise
│   │   ├── retail_sales_clean2.db  # Banco limpo, importado via pandas
│   │   └── retail_sales1.db        # Banco original
│   ├── raw_datasets/               # Dados brutos
│   │   ├── retail_sales_ver2.csv   # Dataset original
│   │   └── mock_kaggle.csv         # Dataset auxiliar
│   └── report/                     # Exploração e relatórios
│       ├── orange_data_cleaning/   # Análise exploratória feita no Orange
│       │   ├── missing_values.png  # Valores ausentes
│       │   ├── redundant_column.png
│       │   ├── structure.png       # Estrutura do dataset
│       │   └── unique.png          # Valores únicos
│       └── retail_sales_dataset2.csv
├── scripts/                        # Scripts Python
│   ├── queries_db1+db2/
│   │   ├── queries_db1/            # Queries do banco 1
│   │   └── queries_db2/            # Queries do banco 2
│   ├── clean_retail2.py            # Limpeza e importação do dataset
│   ├── download_conn_retail1.py    # Conexão e download do banco 1
│   └── README.md
├── .gitignore
└── README.md
```

---

## 📦 Datasets

**Banco 1 — `retail_sales1.db`**
Dataset de vendas com foco em séries temporais — análise por dia, semana e mês.

**Banco 2 — `retail_sales_clean2.db`**
Dataset de varejo com foco em comportamento de clientes e categorias de produtos.

Os dois bancos são independentes e treinam contextos diferentes de análise, elas não possuem relação entre si. A decisão de abordar 2 datasets diferentes, veio da ideia de extrair dados de duas formas diferentes, uma por meio da API do Kaggle, e a outra por download na máquina e conversão em tabela SQLite por meio da biblioteca Pandas

---

## 🧹 Processo de Limpeza

A exploração inicial foi feita no **Orange Data Mining** para identificar visualmente valores ausentes, colunas redundantes e inconsistências na estrutura do dataset.

O problema encontrado foi que ao exportar pelo Orange, o arquivo era salvo com todas as colunas colapsadas em uma só, separadas por `\t`, com linhas de metadata no topo, corrompendo a leitura pelo SQLite.

A solução foi importar o CSV original **direto pelo pandas**, sem passar pelo Orange:
```python
df = pd.read_csv('dados/raw_datasets/retail_sales_dataset.csv')
df.columns = df.columns.str.strip().str.replace(' ', '_')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.to_sql('vendas2', conn, if_exists='replace', index=False)
```

-Vale destacar, que a limpeza foi efetuada apenas no segundo dataset, que tinha espaços como separadores. O primeiro dataset (mock_kaggle.csv) não teve limpeza, por não ter dados ausentes ou colunas com nomenclatura que geraria problema para o SQLite

---

## 🔍 Queries Desenvolvidas

### Banco 1
| Arquivo | Pergunta respondida |
|---|---|
| `1-1-maior_venda_p_ano.py` | Qual foi a maior venda por ano? |
| `1-2-maiores_vendas.py` | Quais foram as maiores vendas? |
| `1-3-menores_vendas.py` | Quais foram as menores vendas? |
| `1-4-query_vendas_semana.py` | Como as vendas se distribuem por semana? |
| `1-5-vendas_mes_passado.py` | Qual foi o volume de vendas no mês passado? |

### Banco 2
| Arquivo | Pergunta respondida |
|---|---|
| `2-1-maiores_compradores.py` | Quais clientes geraram mais receita? |
| `2-2-compradores_acima_media.py` | Quais clientes compraram acima da média? |
| `2-3-renda_acumulada.py` | Qual a receita acumulada mês a mês? |
| `2-4-join_compradores_rendap.py` | Qual o percentual de cada cliente na receita do mês? |
| `2-5-vendas_renda_categoria.py` | Ranking de categorias por quantidade e receita? |
| `2-6-genero_pcategoria.py` | Qual o percentual de cada gênero por categoria? |

---

## 🚀 Como Rodar

**1. Instalar dependências:**
```bash
pip install pandas sqlite3
```

**2. Limpar e importar o dataset:**
```bash
python scripts/clean_retail2.py
python scripts/download_conn_retail1.py
```

**3. Rodar uma query:**
```bash
python scripts/queries_db1+db2/queries_db2/2-1-maiores_compradores.py
```

---

## 🛠️ Tecnologias

- **Python** — pandas, sqlite3
- **SQLite** — banco de dados local
- **Orange Data Mining** — exploração visual inicial
- **VS Code** — ambiente de desenvolvimento 