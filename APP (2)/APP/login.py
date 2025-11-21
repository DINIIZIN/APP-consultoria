import flet as ft
from bancodedados import ConsultoriaDB
from estilos_botao import estilo_botao
    
 
banco_dados_usuarios = {}
resultado = ft.Text("")
def login_view(page: ft.Page):
    page.title = "Sistema de Login (Flet)"
    resultado = ft.Text("")
    db = ConsultoriaDB()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#003366"
    page.window.bgcolor = "#003366"
    page.window.width = 385 
    page.window.height = 844
    page.window.resizable = False



    def fazer_login(e):
        email = campo_email.value.strip()
        senha = campo_senha.value.strip()
        if email and senha:
            if db.verificar_login(email,senha):
                resultado.value = "✅ Login realizado com sucesso!"
                page.go("/home")
            else:
                resultado.value = "⚠️ Login ou senha incorretos."
        else:
                resultado.value = "⚠️ Preencha todos os campos."
                
        page.update()

    campo_email = ft.TextField(label="Login", width=350, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
    campo_senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=350,bgcolor=ft.Colors.WHITE, on_submit=fazer_login, color=ft.Colors.BLACK)


    
        
    return ft.View(
        "/login",
        padding=0,
        controls=[
            ft.Container(
                expand=True,
                bgcolor = ft.Colors.WHITE,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#003366", "#0077cc", "#17279F"],
                    
                ),
             content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                    expand = True,
                    controls=[
                        ft.Image(
                            src="logo_dini_company.png",
                           
                            fit=ft.ImageFit.COVER
                        ),
            ft.Text("Login", size=25, color = ft.Colors.WHITE),
            campo_email,
            campo_senha,
            ft.ElevatedButton("Entrar", color=ft.Colors.WHITE,on_click=fazer_login, style = estilo_botao()),           
            resultado,
            ft.TextButton("Esqueci minha senha.", 
            on_click=lambda _: page.go("/recuperar"),
            style = ft.ButtonStyle(
            color = ft.Colors.WHITE)
            ),
            ft.TextButton("Cadastrar", on_click=lambda _: page.go("/cadastro"),
            style = ft.ButtonStyle(
            color = ft.Colors.WHITE)
            ),             
        ]
            
            
    )
            )
        ]
    )

