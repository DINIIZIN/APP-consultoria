import sqlite3
import bcrypt

class ConsultoriaDB:
    def __init__(self, nome_banco="Consultoria.db"):
        self.nome_banco = nome_banco
        self._criar_tabela()

    def _criar_tabela(self):
        """Cria a tabela de usuários se não existir (dados ficam permanentes em consultoria.db)."""
        con = sqlite3.connect(self.nome_banco)
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            telefone TEXT,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)
        con.commit()
        con.close() 

    def cadastrar_usuario(self, nome, email,  senha,  telefone):
        """Cadastra um novo usuário e salva permanentemente no banco."""
        con = sqlite3.connect(self.nome_banco)
        cur = con.cursor()
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        try:
            cur.execute("""
            INSERT INTO usuarios (nome, email, senha, telefone)
            VALUES (?, ?, ?, ?,)
            """, (nome, email,senha_hash.decode(), telefone))
            con.commit()
        except sqlite3.IntegrityError:
            print("⚠️ Erro: email já cadastrado.")
        finally:
            con.close()

    def listar_usuarios(self):
        """Retorna todos os usuários cadastrados."""
        con = sqlite3.connect(self.nome_banco)
        cur = con.cursor()
        cur.execute("SELECT id, nome, email, telefone, criado_em FROM usuarios")
        usuarios = cur.fetchall()
        con.close()
        return usuarios

    def verificar_login(self, email, senha):
        """Verifica se login e senha estão corretos."""
        con = sqlite3.connect(self.nome_banco)
        cur = con.cursor()
        cur.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
        resultado = cur.fetchone()
        con.close()

        if resultado:
            senha_hash = resultado[0]
            if bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8')):
                return True
            else:
                return False
        else:
            return False