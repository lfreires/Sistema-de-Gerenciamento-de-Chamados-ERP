import sqlite3

try:
    conexao = sqlite3.connect('banco.db')
except sqlite3.Error as e:
    print(f'Erro ao criar o banco - {e}')

cursor = conexao.cursor()
#id, self.nome, self.email, self.senha, self.cargo
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id VARCHAR(255) PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255),
                senha VARCHAR(255),
                cargo VARCHAR(255)
);''')
conexao.close()