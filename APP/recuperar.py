from bancodedados import ConsultoriaDB
import flet as ft
from estilos_botao import estilo_botao
def recuperacao_senha_view(page: ft.Page):
    resultado = ft.Text("")
    db = ConsultoriaDB()
    
    page.padding = 0    
    
    def limpar_resultado(e):
         resultado.value = ""
         page.update()
        



    campo_email = ft.TextField(
        label="Email Cadastrado",
        on_change=limpar_resultado,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK

    )
    

    def validar_email_para_redefinir(e):
            email = campo_email.value.strip()
            if not email:
                resultado.value = "⚠️ Insira seu e-mail antes de continuar."
            else:
                page.session.set("email_recuperacao", email)  # 🔑 salva o e-mail na sessão
                page.go("/nova_senha")  # vai para a tela de nova senha
    page.update()
    


    def verificar_email(e):
            email = campo_email.value.strip()
            if email:
                usuarios = db.listar_usuarios()

                if any(u[2] == email for u in usuarios):
                    resultado.value = "✅ Email encontrado! Clique abaixo para redefinir a senha."
                    page.update()
                else:
                    resultado.value = "⚠️ Email não cadastrado."
            else:
                resultado.value = "⚠️ Preencha o campo de email."
            page.update()

           

    return ft.View(
            "/recuperar",
                padding=0,
                 controls=[
                    ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, -1),
                        end=ft.Alignment(1, 1),
                        colors=["#003366", "#0077cc", "#17279F"]
                    ),
                    content = ft.Column(
                    
                        expand=True,
                    controls=[ 
                        ft.Text("Recuperar senha", size = 25),
                        campo_email,
                        ft.ElevatedButton("Verificar", on_click=verificar_email, style=estilo_botao()),
                        resultado,
                        ft.TextButton("Redefinir Senha", on_click=validar_email_para_redefinir, 
                        style=estilo_botao(), 
                    ),
                        ft.ElevatedButton("Voltar ao login", on_click=lambda _: page.go("/login"),
                                         style = estilo_botao()),
                        ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        
                        )
                    )

            ]
                            
                        
        )