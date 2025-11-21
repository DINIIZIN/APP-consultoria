import flet as ft
import datetime
from estilos_botao import estilo_botao
def agendamento_view(page: ft.Page):  #Função principal que define a tela de agendamento
    
    page.theme_mode = ft.ThemeMode.DARK 
    page.bgcolor = "#003366"
    page.window.bgcolor = "#003366"
    page.window.width = 390
    page.window.height = 844
    page.window.resizable = False
    page.padding = 0


    alerta_dialogo = ft.AlertDialog(modal=True,
                                    title=ft.Text("✅ Agendamento Confirmado!", text_align="center", weight="bold"),
                                    content=ft.Text("Seu horáro foi reservado com sucesso!", text_align="center"),
                                    actions=[(ft.TextButton("Fechar", on_click=lambda e: fechar_alerta()))],
                                    open=False

                                    )
    def fechar_alerta():
        alerta_dialogo.open = False
        page.update()
    
    servico_dropdown = ft.Dropdown(#Permite ao usuário escolher qual serviço deseja agendar.
        label = "Serviços", 
        bgcolor=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        border_color=ft.Colors.WHITE,
        focused_border_color=ft.Colors.WHITE,
        text_style= ft.TextStyle(color=ft.Colors.BLACK),
        options=[   
            ft.dropdown.Option("Mentoria de carreira", text_style = ft.TextStyle(color=ft.Colors.BLACK)),
            ft.dropdown.Option("Preparação pra Processo Seletivo",text_style = ft.TextStyle(color=ft.Colors.BLACK)),
            ft.dropdown.Option("Coaching", text_style = ft.TextStyle(color=ft.Colors.BLACK)),
            ft.dropdown.Option("Mapeamento de Perfil", text_style = ft.TextStyle(color=ft.Colors.BLACK)),

        ]

    )
    objetivo_text = ft.Text("",color=ft.Colors.WHITE)
    preco_text = ft.Text("", color=ft.Colors.WHITE)
    texto_data = ft.Text("", color=ft.Colors.WHITE)#vai ser preenchido com base no serviço e na instruçao de data e preço




    horario_dropdown = ft.Dropdown(
        label = "Horário",
        width= 300,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        bgcolor=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        focused_border_color=ft.Colors.BLACK,
        text_style=ft.TextStyle(color=ft.Colors.BLACK),  
        options = [ft.dropdown.Option(f"{h}:00") for h in range(14,21)]
    )
    #cria um componente de calendario (datepicker) para o usuario definir uma data
    date_picker = ft.DatePicker(
        on_change=lambda e: print("Data Escolhida:", e.data), #mostra no terminal a data escolhida
        first_date=datetime.date.today(),#Define a data mínima como hoje
        last_date=datetime.date.today() + datetime.timedelta(days=60)#define a data maixma como 60 dias à frente
    )
    page.overlay.append(date_picker) #adiciona o calendario a sobreposição da página(fica invisivel até ser aberto)

    #Função que abre o calendário na tela
    def abrir_calendario(e):
        date_picker.open = True #abre o calendário
        page.update()#atualiza a página(interface)

    def confirmar_agendamento(e):
        data = date_picker.value
        horario = horario_dropdown.value
        servico = servico_dropdown.value       
        
        if not servico or not horario or not data:
            
            
                alerta_dialogo.title = ft.Text("⚠️ Dados incompletos")
                alerta_dialogo.content= ft.Text("Por favor, selecione serviço, data ou horário antes de confirmar.")
                
        else:
            alerta_dialogo.title=ft.Text("✅ Agendamento Confirmado!")
            alerta_dialogo.content=ft.Text(f"{servico} marcado para {data} às {horario}")#mostra a data escolhida
             #abre o diálogo
            
    
        
        alerta_dialogo.open = True
        page.update()
    page.update()#atualiza interface
    #formulário quando o usuário clicar em agendar mentoria
    formulario = ft.Column(
    visible=False,
    horizontal_alignment=ft.CrossAxisAlignment.START,
    controls=[
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Selecione uma data",
                        on_click=lambda e: abrir_calendario(e),
                        style=estilo_botao()
                    ),
                    ft.ElevatedButton(
                        "Confirmar Agendamento",
                        on_click=confirmar_agendamento,
                        style=estilo_botao()
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER  # centraliza os dois
            ),
              # empurra o conjunto pra direita
        )
    ]
)



    textos = {
    "Mentoria de carreira": {
        "objetivo": "Um processo de desenvolvimento profundo, com provocações estratégicas, exercícios e " \
            "acompanhamento contínuo. A mentoria amplia visão de carreira, fortalece competências e direciona escolhas consistentes.",
        "preco": "Preço: R$700,00"
    },
    "Preparação pra Processo Seletivo": {
        "objetivo": "Trabalho focado em entrevistas, cases e dinâmicas, onde ajudo o cliente a estruturar sua narrativa, " \
            "destacar pontos fortes e responder com segurança. Aplico a técnica de role play, simulando situações reais, com prática intensa, feedback imediato e ajustes na hora.",
        "preco": "Preço: R$750,00"
    },
    "Coaching": {
        "objetivo": "Voltado para metas e performance. Utilizo técnicas estruturadas para apoiar o cliente a definir objetivos claros, " \
             "construir plano de ação e alcançar resultados mensuráveis no prazo definido.",
        "preco": "Preço: R$700,00"
    },
    "Mapeamento de Perfil": {
        "objetivo":"Ferramenta de autoconhecimento que revela pontos fortes, desafios e estilo de comportamento. Utilizo técnicas como a Janela de Johari, " \
           "que evidencia aspectos visíveis para si e para os outros — e também os pontos cegos que precisam ser revelados. A partir dessa leitura, ajudo o cliente a enxergar padrões, ganhar clareza e traçar estratégias de desenvolvimento.",
        "preco": "Preço: R$700,00"
    }
}
    #função que torna o formulário visível
    def mostrar_formulario(e):
        servico = servico_dropdown.value
 
  
        if servico in textos:
            objetivo_text.value = textos[servico]["objetivo"]
            preco_text.value = textos[servico]["preco"]
            texto_data.value = f"Escolha uma data para{servico.lower()}:"
            formulario.visible = True
        else:
            objetivo_text.value = ""
            preco_text.value = ""
            texto_data.value = ""
            formulario.visible = True

      
        page.update()#atualizaçãõ da interface


    return ft.View(
        "/agendar", #Rota da tela
        padding=0,
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1,-1),
                    end=ft.Alignment(1, 1),
                    colors=["#003366", "#0077cc", "#17279F"]
            ),

        
            content = ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand = True,

                 controls = [ft.Text("📅 Agendar Consultoria", size=24, weight="bold", color= ft.Colors.WHITE),#titulo
                 servico_dropdown,
                 objetivo_text,
                 preco_text,
                 horario_dropdown,
                 # Botão que apenas mostra o formulário
                 ft.ElevatedButton("Mostrar Agenda",on_click=mostrar_formulario,style=estilo_botao()),
                 formulario,
                 ft.Divider(),
                 ft.ElevatedButton("Voltar", on_click=lambda _: page.go("/home"), style=estilo_botao()),
                 alerta_dialogo  
            
                ],

            ),

        
     )
    

        ]
    )
