import sqlite3, uuid

class Usuarios:

    def __init__(self, nome: str, email: str, senha: str, cargo: str) -> None:
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

    def conectar(self) -> str:
        try:
            self.conexao = sqlite3.connect('banco.db')
            self.cursor = self.conexao.cursor()
            return 'Usuário conectado ao banco de dados com sucesso.'

        except sqlite3.Error as e:
            return f'Erro ao conectar o usuário criado com o banco de dados: {e}.'

    def cadastrar(self) -> str:
        try:
            self.cursor.execute('''INSERT INTO usuarios(id, nome, email, senha, cargo)
                                VALUES (?, ?, ?, ?, ?)''',
                                (self.id, self.nome, self.email, self.senha, self.cargo))
            self.conexao.commit()
            return "Usuário cadastrado com sucesso."
        
        except sqlite3.Error as e:
            return(f'Erro ao cadastrar o usuário: {e}')

    def visualizar(self) -> str:
        try:
            self.cursor.execute('''SELECT * FROM usuarios WHERE id=?''', (self.id,))
            usuario = self.cursor.fetchone()
            if usuario:
                return usuario
            else:
                return 'Usuário não encontrado.'
            
        except sqlite3.Error as e:
            return f'Erro ao visualizar o usuário: {e}'
        
    def alterar(self, nome: str, email: str, senha: str, cargo: str) -> str:
        try:
            self.cursor.execute('''UPDATE usuarios SET nome=?, email=?, senha=?, cargo=?
                                WHERE id=?''', (nome, email, senha, cargo, self.id,))
            self.conexao.commit()
            return 'Usuário alterado com sucesso.'
        except sqlite3.Error as e:
            return f'Erro ao alterar o usuário: {e}'

    def excluir(self) -> str:
        try:
            self.cursor.execute('''DELETE FROM usuarios WHERE id=?''', (self.id,))
            self.conexao.commit()
            return 'Usuário excluído com sucesso.'
        except sqlite3.Error as e: 
            return f'Erro ao excluir o usuário {e}'
        