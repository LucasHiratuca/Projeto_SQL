# 📊 Scripts de Integração de Dados - Retail

Este repositório contém scripts para download e processamento de dados de varejo, integrando com a API do Kaggle e gerenciamento de banco de dados SQLite.

---

## 📁 Scripts Disponíveis

### 1️⃣ `download_conn_retail1.py`
**Download de dados da API do Kaggle para SQLite**

Este script baixa um dataset diretamente da API do Kaggle e cria uma tabela no banco SQLite com os dados obtidos.

### 2️⃣ `conn_retail2.py`
**Importação de dados processados no Orange para SQLite**

Este script carrega dados que foram tratados e exportados do Orange e os transfere para uma tabela no banco SQLite.

---

## 🚀 Como usar

```bash
# Download dos dados da API
python scripts/download_conn_retail1.py

# Importação dos dados do Orange
python scripts/conn_retail2.py