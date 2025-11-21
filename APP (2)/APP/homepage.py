import flet as ft
from estilos_botao import estilo_botao



def home_view(page: ft.Page):
   
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#003366"
    page.window_bgcolor = "#003366"
    page.window.width = 385
    page.window.height = 844
    page.window.resizable = False
    page.padding = 0
   
    return ft.View(
        "/home",
        padding = 0,
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#003366", "#0077cc", "#17279F"]
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand = True,
                    spacing=20,
                    controls=[
                        ft.Image(
                            src="logo_Dini_company.png",
                           
                            fit=ft.ImageFit.COVER
                        ),
                        ft.Text(
                            "👋Bem-vindo à Dini Company!",
                            size=18,
                            weight="bold",
                            text_align="center",
                            color=ft.Colors.WHITE
                        ),
                        ft.Column(
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton("Agendar Sessão", on_click=lambda _: page.go("/agendar"), style=estilo_botao()),
                                ft.ElevatedButton("Meu Perfil", on_click=lambda _: page.go("/perfil"), style=estilo_botao()),
                                ft.ElevatedButton("Abrir Chatbot", on_click=lambda _: page.go("/chatbot"),  style=estilo_botao()),
                                ft.ElevatedButton("Encerrar Sessão", on_click=lambda _: page.go("/login"), style=estilo_botao()),
                            ]
                        )
                    ]
                )
            )
        ]
    )

