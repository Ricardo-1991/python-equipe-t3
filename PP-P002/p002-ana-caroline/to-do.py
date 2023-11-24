# Lista de tarefas
tarefas = []

# Função para listar as tarefas
def listar_tarefas():
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(f"{i}. {tarefa['descricao']} {status}")

# Função para registrar uma nova tarefa
def registrar_tarefa(descricao):
    if descricao[0].islower():
        descricao = descricao.capitalize()
    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa registrada!!!")

# Função para marcar uma tarefa como realizada
def marcar_tarefa_realizada(identificador):
    if 1 <= identificador <= len(tarefas):
        tarefa = tarefas.pop(identificador - 1)
        tarefa["concluida"] = True
        tarefas.insert(0, tarefa)
        print("Tarefa marcada como realizada!!!")
    else:
        print("Tarefa não encontrada ou já realizada.")

# Função para editar uma tarefa
def editar_tarefa(identificador, nova_descricao):
    if 1 <= identificador <= len(tarefas):
        tarefa = tarefas[identificador - 1]
        tarefa["descricao"] = nova_descricao
        print("Tarefa editada com sucesso!!!")
    else:
        print("Tarefa não encontrada.")

# Exemplo de uso:
registrar_tarefa("Preparar a marmita")
registrar_tarefa("Arrumar a mochila")
registrar_tarefa("Fechar as janelas")
listar_tarefas()
marcar_tarefa_realizada(1)
listar_tarefas()
editar_tarefa(2, "Arrumar o quarto")
listar_tarefas()
