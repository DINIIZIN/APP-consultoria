import google.generativeai  as genai# Importa a biblioteca da openai para se comunicar com a Ia do gemini
import flet as ft
import httpx
import asyncio
import threading
from estilos_botao import estilo_botao
#Define a chave de acesso da api do Gemini
genai.configure(api_key="AIzaSyA0pPyA2dZBXvY9UqHzyuLALT1O1yzt25w")

model = genai.GenerativeModel("models/gemini-2.5-pro")#define qual o modelo do google que vamos usar que é o gemini

mensagens = ft.ListView(expand=True, spacing=10, auto_scroll=True)


async def buscar_google(pergunta):
    chave_api = "AIzaSyA0pPyA2dZBXvY9UqHzyuLALT1O1yzt25w"
    cx = "a5311e24a29ca41cd"
    url = "https://www.googleapis.com/customsearch/v1"

    parametros = {
        "key":chave_api,
         "cx": cx,
         "q": pergunta
    }
    
    
    async with httpx.AsyncClient() as client:

        resposta = await client.get(url, params=parametros)
        resultados = resposta.json()
    
    
    if "items" in resultados:
        resumo = ""
        for item in resultados["items"][:5]:
            titulo = item.get("title", "")
            link = item.get("link", "")
            snippet = item.get("snippet", "")
            print(f"🔗 {titulo} \n`{link}\n{snippet}\n")
            resumo += snippet + " "
            return resumo.strip()   
    return ""



async def responder_chatbot(pergunta):
    resumo_web = await buscar_google(pergunta)
    resposta =  await asyncio.to_thread(model.generate_content,f"Com base nisso {resumo_web}, responda: {pergunta}")
    return resposta.text #retorna a resposta no terminal
    
def chatbot_view(page: ft.Page):
    pergunta_input = ft.TextField(label="Digite sua pergunta",
    color=ft.Colors.BLACK
    )
    
    page.padding = 0
    async def perguntar(e):   
        pergunta = pergunta_input.value
        mensagens.controls.append(ft.Text(f"{pergunta}", color=ft.Colors.WHITE))
        
        mensagens.controls.append(ft.Text(f"🤖 Dini AI está pensando...", color=ft.Colors.BLACK))
        page.update()  
        
        resposta = await responder_chatbot(pergunta)
       
        mensagens.controls.pop()
        mensagens.controls.append(ft.Text(f"{resposta}", color=ft.Colors.CYAN_100))
        
        
        pergunta_input.value = ""
        pergunta_input.focus()
        page.update()
    pergunta_input =ft.TextField(label = "Digite sua Pergunta",
                               on_submit=lambda e: threading.Thread(target=lambda: asyncio.run(perguntar(e))).start(), 
                                 bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK  )#ativa a função ao pressionar 
                                
    return ft.View(
    "/chatbot",
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
                expand = True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Dini AI", size=30, weight="bold", color=ft.Colors.WHITE),

                    ft.Container(
                        expand=True,
                        content=mensagens,
                        padding=20,
                        alignment=ft.alignment.center
                    ),

                    ft.Row(
                        controls=[pergunta_input],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/home"), style=estilo_botao())
                ]
            )
        )
    ]
)

    