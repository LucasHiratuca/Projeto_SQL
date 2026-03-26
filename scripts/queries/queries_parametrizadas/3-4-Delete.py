import sqlite3
import pandas as pd

def delete_vendas(conn, transaction_id: int) -> None:

    cur = conn.cursor()

    cur.execute("DELETE FROM vendas2 WHERE Transaction_ID = ?", (transaction_id,))

    conn.commit()
    print(f"✅ Transação {transaction_id} excluída com sucesso!")


if __name__ == "__main__":
    conn = sqlite3.connect("dados/processed/retail_sales_clean2.db")
    try:
        transaction_id = int(input("Digite o id da transação que deseja excluir: "))

        delete_vendas(conn, transaction_id)

    except ValueError as e:
        print(f"❌ Erro de valor — limite deve ser um número inteiro: {e}")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    finally:
        conn.close()