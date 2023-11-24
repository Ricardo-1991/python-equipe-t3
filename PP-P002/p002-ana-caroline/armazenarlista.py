# Função para carregar as tarefas do arquivo
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.strip().split("|")
                descricao = partes[0]
                concluida = True if partes[1] == "True" else False
                tarefas.append({"descricao": descricao, "concluida": concluida})
    except FileNotFoundError:
        # Se o arquivo não existir, começa com uma lista vazia de tarefas
        pass

# Função para salvar as tarefas no arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['descricao']}|{tarefa['concluida']}\n")

# Antes de usar as tarefas, carregue-as do arquivo
tarefas = []
carregar_tarefas()

# Restante do código (funções existentes) permanece igual...

# Exemplo de uso:
registrar_tarefa("Preparar a marmita")
registrar_tarefa("Arrumar a mochila")
registrar_tarefa("Fechar as janelas")
listar_tarefas()
marcar_tarefa_realizada(1)
listar_tarefas()
editar_tarefa(2, "Arrumar o quarto")
listar_tarefas()

# Ao finalizar o programa ou sempre que houver uma modificação nas tarefas, salve-as no arquivo
salvar_tarefas()
