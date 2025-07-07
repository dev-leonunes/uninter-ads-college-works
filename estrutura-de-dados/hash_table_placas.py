class NodoEstado:
    # [EXIGÊNCIA DE CÓDIGO 2 de 7]
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

    def __str__(self):
        return f"[{self.sigla}]"

class TabelaHashEstados:
    def __init__(self, tamanho=10):
        # [EXIGÊNCIA DE CÓDIGO 1 de 7]
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho

    # [EXIGÊNCIA DE CÓDIGO 5 de 7]
    def funcao_hash(self, sigla):
        if sigla.upper() == 'DF':
            return 7
        
        if len(sigla) >= 2:
            char1_ascii = ord(sigla[0].upper())
            char2_ascii = ord(sigla[1].upper())
            return (char1_ascii + char2_ascii) % self.tamanho
        return 0

    # [EXIGÊNCIA DE CÓDIGO 3 de 7]
    def inserir(self, sigla, nome_estado):
        posicao = self.funcao_hash(sigla)
        novo_nodo = NodoEstado(sigla, nome_estado)
        
        if self.tabela[posicao] is not None:
            novo_nodo.proximo = self.tabela[posicao]
        
        self.tabela[posicao] = novo_nodo

    # [EXIGÊNCIA DE CÓDIGO 4 de 7]
    def imprimir_tabela(self):
        for i in range(self.tamanho):
            print(f"Posição {i}: ", end="")
            ponteiro_atual = self.tabela[i]
            
            if not ponteiro_atual:
                print("None")
            else:
                elementos_da_linha = []
                while ponteiro_atual:
                    elementos_da_linha.append(str(ponteiro_atual))
                    ponteiro_atual = ponteiro_atual.proximo
                print(" -> ".join(elementos_da_linha) + " -> None")
        print("-" * 30)

def executar():
    tabela_hash = TabelaHashEstados()

    print("\n--- Tabela Hash Inicial (Vazia) ---")
    tabela_hash.imprimir_tabela()

    # [EXIGÊNCIA DE CÓDIGO 6 de 7]
    estados_brasil = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    
    for sigla, nome in estados_brasil:
        tabela_hash.inserir(sigla, nome)

    print("\n--- Tabela Hash Após Inserção dos 27 Estados e DF ---")
    tabela_hash.imprimir_tabela()

    # [EXIGÊNCIA DE CÓDIGO 7 de 7]
    tabela_hash.inserir('LN', 'Leonardo Nunes')

    print("\n--- Tabela Hash Final (com Estado Fictício) ---")
    tabela_hash.imprimir_tabela()

executar()
