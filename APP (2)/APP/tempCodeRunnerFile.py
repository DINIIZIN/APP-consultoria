import flet as ft
from homepage import home_view
from agendamento import agendamento_view
from perfil import perfil_view
#from depoimento import depoimento_view
from chatbot import chatbot_view

async def main(page: ft.Page):
    page.title = "Dini Company - Consultoria de Carreiras"
    page.theme_mode = ft.ThemeMode.LIGHT

    

    
    
    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.views.append(home_view(page)) #tela principal
    
        elif page.route == "/agendar":
            page.views.append(agendamento_view(page)) #tela de agendamento 

        elif page.route == "/perfil":
            page.views.append(perfil_view(page)) #tela de perfil
        
        #elif page.route == "/depoimento":
           # page.views.append(depoimento_view(page)) #tela do historico
        
        elif page.route == "/chatbot": 
            page.views.append(chatbot_view(page)) #tela do chatbot
        page.update() #atualiza interface com nova tela

    page.on_route_change = route_change # Toda vez que o usuário mudar de tela (rota), execute a função route_change.
    page.go("/home") # quando o app abrir a primeira tela é o home

ft.app(target=main)