conn = sqlite3.connect("banco.db")
cur = conn.cursor()

email = "ana@email.com"
cur.execute("SELECT * FROM usuarios WHERE email = ?", (email,))

linha = cur.fetchone()   # retorna uma linha
linhas = cur.fetchall() # retorna todas

print(linha)