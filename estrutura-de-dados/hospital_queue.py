# [EXIGÊNCIA DE CÓDIGO 1 de 7]
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

    def __str__(self):
        return f"[{self.cor},{self.numero}]"

class FilaDeAtendimento:
    def __init__(self):
        self.head = None
        self.contador_v = 1
        self.contador_a = 201

    def inserirSemPrioridade(self, novo_nodo):
        # [EXIGÊNCIA DE CÓDIGO 2 de 7]
        if not self.head:
            self.head = novo_nodo
            return

        ponteiro_atual = self.head
        while ponteiro_atual.proximo:
            ponteiro_atual = ponteiro_atual.proximo
        ponteiro_atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        # [EXIGÊNCIA DE CÓDIGO 3 de 7]
        if not self.head or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
            return

        ponteiro_atual = self.head
        while ponteiro_atual.proximo and ponteiro_atual.proximo.cor == 'A':
            ponteiro_atual = ponteiro_atual.proximo

        novo_nodo.proximo = ponteiro_atual.proximo
        ponteiro_atual.proximo = novo_nodo

    def inserir(self):
        # [EXIGÊNCIA DE CÓDIGO 4 de 7]
        while True:
            cor = input("Digite a cor do cartão (A,V): ").upper()
            if cor in ['A', 'V']:
                break
            else:
                print("Opção inválida. Por favor, digite 'A' ou 'V'.")

        if cor == 'A':
            numero = self.contador_a
            self.contador_a += 1
        else:
            numero = self.contador_v
            self.contador_v += 1
            
        novo_nodo = Nodo(numero, cor)

        if not self.head:
            self.head = novo_nodo
        elif novo_nodo.cor == 'A':
            self.inserirComPrioridade(novo_nodo)
        else:
            self.inserirSemPrioridade(novo_nodo)
            
        print(f"Paciente com cartão {novo_nodo.cor}{novo_nodo.numero} adicionado à fila.")

    def imprimirListaEspera(self):
        # [EXIGÊNCIA DE CÓDIGO 5 de 7]
        if not self.head:
            print("\nA fila de espera está vazia.\n")
            return

        elementos = []
        ponteiro_atual = self.head
        while ponteiro_atual:
            elementos.append(str(ponteiro_atual))
            ponteiro_atual = ponteiro_atual.proximo
        
        print("\nFila de Espera: " + " ".join(elementos) + "\n")

    def atenderPaciente(self):
        # [EXIGÊNCIA DE CÓDIGO 6 de 7]
        if not self.head:
            print("\nNão há pacientes na fila para atender.\n")
            return

        paciente_chamado = self.head
        self.head = self.head.proximo
        print(f"\n>>> Chamando paciente - Cartão {paciente_chamado.cor}{paciente_chamado.numero} - para atendimento! <<<\n")

class SistemaHospitalar:
    # [EXIGÊNCIA DE CÓDIGO 7 de 7]
    def __init__(self):
        self.fila = FilaDeAtendimento()

    def executar(self):
        while True:
            print("\n--- Sistema de Triagem Hospitalar ---")
            print("1 – Adicionar paciente à fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar paciente")
            print("4 – Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.fila.inserir()
            elif opcao == '2':
                self.fila.imprimirListaEspera()
            elif opcao == '3':
                self.fila.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o sistema. Obrigado!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

sistema = SistemaHospitalar()
sistema.executar()
