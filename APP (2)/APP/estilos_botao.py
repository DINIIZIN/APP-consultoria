import flet as ft

def estilo_botao():
    return ft.ButtonStyle(
        bgcolor=ft.Colors.WHITE30,
        color= ft.Colors.WHITE,
        overlay_color= ft.Colors.DEEP_ORANGE,
        shape = ft.RoundedRectangleBorder(radius=50),
        elevation = 30
    )