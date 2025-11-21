import flet as ft
import bcrypt
import sqlite3
from estilos_botao import estilo_botao
def nova_senha_view(page:ft.Page):
    email = page.session.get("email_recuperacao")
    campo_nova_senha = ft.TextField(label="Nova Senha", password=True,can_reveal_password=True,bgcolor=ft.Colors.WHITE, width=370, color=ft.Colors.BLACK)
    campo_confirmar_senha = ft.TextField(label="Confirmar senha", password= True, can_reveal_password=True, bgcolor=ft.Colors.WHITE, width=370,color=ft.Colors.BLACK)
    resultado = ft.Text("")
    
    page.padding = 0
    
    
    def redefinir_senha(e):
        ##usa o e-mail que vai na tela anterior email = campo_email.value.strip()
        nova_senha = campo_nova_senha.value.strip()
        confirmar_senha = campo_confirmar_senha.value.strip()
        
        if not email or not nova_senha or not confirmar_senha:
            resultado.value = "⚠️ Preencha todos os campos."
            page.update()
        elif nova_senha != confirmar_senha:
             resultado.value = "⚠️ As senhas não coincidem."
             page.update()
        
       
       
        try:
            conn  = sqlite3.connect("Consultoria.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
            if cursor.fetchone():
                senha_hash = bcrypt.hashpw(nova_senha.encode("utf-8"), bcrypt.gensalt())
                cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (senha_hash.decode(), email,))
                conn.commit()
                resultado.value = "✅ Senha redefinida com sucesso!"
                page.update()
            else: 
                resultado.value = "⚠️ E-mail não encontrado."
            page.update()
       
        finally:
            conn.close()
    
    
    return ft.View(
    "/nova_senha",
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
               
               expand = True,
                controls=[   # ✅ aqui é controls, com colchetes
                    campo_nova_senha,
                    campo_confirmar_senha,
                    ft.ElevatedButton("Confirmar", on_click=redefinir_senha, style=estilo_botao()),
                    resultado,
                    ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/login"), style=estilo_botao())
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    ],
    vertical_alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)    


    
    
    