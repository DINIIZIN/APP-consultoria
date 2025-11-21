import flet as ft
import sqlite3
from estilos_botao import estilo_botao
import bcrypt
# Criando conexão e tabela (se não existir)
def criar_banco():
    conn = sqlite3.connect("Consultoria.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    
    

def cadastro_view(page: ft.Page):
    page.title = "Tela de Cadastro"
    page.window.width = 385
    page.window.height = 844
    page.scroll = "adaptive"
    
    
    criar_banco()  # garante que a tabela exista

    # Campos de cadastro
    campo_nome = ft.TextField(label="Nome", width=370, bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
    campo_email = ft.TextField(label="E-mail", width=370, bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
    campo_senha = ft.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        width=370,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
    )
    campo_telefone = ft.TextField(label="Telefone", width=370, bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)

    # Texto para exibir resultado
    resultado = ft.Text("")

    # Função do botão cadastrar
    def cadastrar(e):
        nome = campo_nome.value.strip()
        email = campo_email.value.strip()
        senha = campo_senha.value.strip()
        telefone = campo_telefone.value.strip()

        if nome and email and senha and telefone:
            try:
                conn = sqlite3.connect("Consultoria.db")
                cursor = conn.cursor()
               
                senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
               
                cursor.execute(
                    "INSERT INTO usuarios (nome, email, senha, telefone) VALUES (?, ?, ?, ?)",
                    (nome, email, senha_hash.decode(), telefone)
                )
                conn.commit()
                resultado.value = "✅ Cadastro realizado com sucesso!"
                page.go("/login")
                campo_nome.value = ""
                campo_email.value = ""
                campo_senha.value = ""
                campo_telefone.value = ""
            except sqlite3.IntegrityError:
                # ⚠️ Email duplicado
                resultado.value = "⚠️ Erro: e-mail já cadastrado."
            except Exception as ex:
                # ⚠️ Outro erro inesperado
                print("Erro inesperado:", ex)
                resultado.value = "⚠️ Erro inesperado ao cadastrar."
            finally:
                conn.close()
        else:
            resultado.value = "⚠️ Preencha todos os campos antes de cadastrar."

        page.update()

    # Botão de cadastro
    botao_cadastrar = ft.ElevatedButton(
        "Cadastrar",
        on_click=cadastrar,
        style=estilo_botao(),

    ) 
    

    # Adicionando elementos à tela
    return ft.View(
        padding=0,
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#003366", "#0077cc", "#17279F"]
                ),
                content=ft.Column(
                    expand=True,
                    controls =[
                        ft.Text("Cadastro de Usuário", size=20, weight="bold", ),
                        campo_nome,
                        campo_email,
                        campo_senha,
                        campo_telefone,
                        botao_cadastrar,
                        resultado,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )