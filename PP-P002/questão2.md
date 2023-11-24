## Persistência de dados:

Em Python, você pode usar a manipulação de arquivos para armazenar e recuperar dados persistentes, como a lista de tarefas em um aplicativo. Vou apresentar um exemplo básico de como você poderia modificar o aplicativo para utilizar um arquivo para armazenar a lista de tarefas.

```python
    import random

def adicionar_tarefa(tarefa, arquivo):
    with open(arquivo, 'a') as f:
        f.write(tarefa + '\n')

def mostrar_tarefas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            tarefas = f.readlines()
            if not tarefas:
                print("Nenhuma tarefa encontrada.")
            else:
                print("Lista de tarefas:")
                for i, tarefa in enumerate(tarefas, start=1):
                    print(f"{i}. {tarefa.strip()}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo.")

def gerar_numero_aleatorio():
    return random.randint(1, 100)

def main():
    arquivo_tarefas = 'tarefas.txt'

    # Adicionar tarefa
    nova_tarefa = f"Tarefa {gerar_numero_aleatorio()}"
    adicionar_tarefa(nova_tarefa, arquivo_tarefas)

    # Mostrar tarefas
    mostrar_tarefas(arquivo_tarefas)

if __name__ == "__main__":
    main()






```