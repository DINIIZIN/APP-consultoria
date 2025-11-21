import flet as ft
from estilos_botao import estilo_botao
import sqlite3
def perfil_view(page: ft.Page):#Função que define a tela de perfil do usuário
    #Campos de entrada para o perfil
    nome_input = ft.TextField(label = "Nome Completo", bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
    email_input = ft.TextField(label = "Email", bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
    telefone_input = ft.TextField(label = "Telefone", bgcolor=ft.Colors.WHITE,color=ft.Colors.BLACK)
    bio_input = ft.TextField(label = "Sobre você", bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
    

    page.padding = 0 
    def fechar_alerta(e):
        alerta_perfil.open = False
        page.update()

    alerta_perfil = ft.AlertDialog(
            modal=True,
            title=ft.Text(""),
            content=ft.Text(""),
            actions=[ft.TextButton("Fechar", on_click=lambda e: fechar_alerta(e))],
            open=False
    )

   
   
   
   
    #Função chamada ao ser clicado salvar alterações
    def salvar_perfil(e):
        #Cria um dialogo de informação com os dados preenchidos
        if not nome_input.value or not email_input.value  or not telefone_input.value:
            alerta_perfil.title = ft.Text("⚠️ Dados incompletos")
            alerta_perfil.content = ft.Text("Por favor, preencha nome, E-mail ou horário antes de confirmar.")

        else:
            conn =  sqlite3.connect("Consultoria.db")
            cursor = conn.cursor()
            cursor.execute(""" 
            UPDATE usuarios
            SET nome=?, email=?, telefone=?, bio=?
            WHERE id = 1""",(nome_input, email_input, telefone_input, bio_input))
            conn.commit()
            conn.close()
            
            alerta_perfil.title = ft.Text("✅ Perfil atualizado")
            alerta_perfil.content = ft.Text(f"Nome: {nome_input.value}\n"
                             f"E-mail: {email_input.value}\n"
                             f"Telefone: {telefone_input.value}"

            )
        alerta_perfil.open=True
        page.dialog = alerta_perfil
        page.update()#atualiza a interface para exibir o diálogo
        
        #Retorna a estrutura visual do perfil
    return ft.View(
        "/perfil",
        padding=0,
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1,-1),
                    end=ft.Alignment(1, 1),
                    colors=["#003366", "#0077cc", "#17279F"]
                
        
            ),
                  
                content=ft.Column(
                 
                 [
                 ft.Text("👤 Meu Perfil", size=30, weight="bold"),#Título do perfil
                 ft.Divider(),#Linha divisória visual
                 nome_input,#Campo do nome
                 email_input,#Campo do e-mail
                 telefone_input,#Campo do telefone
                 bio_input,#Campo da bio
                 ft.ElevatedButton("Salvar Alterações", on_click=salvar_perfil, style=estilo_botao()),#Botão para salvar o perfil
                 ft.Divider(),#linha divisória visual
                 ft.ElevatedButton("Voltar",on_click=lambda _: page.go("/home"), style=estilo_botao()),#Botão para voltar a tela inicial do aplicativo
                 alerta_perfil
                 ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

            )
        ]

)

