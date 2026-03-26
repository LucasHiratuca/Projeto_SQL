import sqlite3

def atualizar_transacao(conn, transacao_id: int, data: str, customer_id: str, 
                      genero: str, idade: int, categoria: str, 
                      quantidade: int, preco_unidade: int) -> None:
    
    total = quantidade * preco_unidade
    cur = conn.cursor()

    cur.execute("UPDATE vendas2 SET Date=?, Customer_ID=?, Gender=?, Age=?, Product_Category=?, Quantity=?, Price_per_Unit=?, Total_Amount=? WHERE Transaction_ID=?",
    (data, customer_id, genero, idade, categoria, quantidade, preco_unidade, total, transacao_id))

    conn.commit()
    print(f"✅ Transação {transacao_id} atualizada com sucesso!")


if __name__ == "__main__":
    conn = sqlite3.connect("dados/processed/retail_sales_clean2.db")

    try:
        transacao_id  = int(input("Digite o id da transação que deseja atualizar: "))
        data          = input("Informe a data (formato YYYY-MM-DD): ")
        customer_id   = input("Digite o ID do cliente (ex: CUST001): ")
        genero        = input("Digite o gênero (Male/Female): ")
        idade         = int(input("Digite a idade: "))
        categoria     = input("Digite a categoria (Beauty/Clothing/Electronics): ")
        quantidade    = int(input("Digite a quantidade: "))
        preco_unidade = int(input("Digite o preço por unidade: "))

        atualizar_transacao(conn, transacao_id, data, customer_id, 
                          genero, idade, categoria, quantidade, preco_unidade)

    except ValueError as e:
        print(f"❌ Erro de valor — verifique se idade, quantidade e preço são números inteiros: {e}")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

    finally:
        conn.close()

