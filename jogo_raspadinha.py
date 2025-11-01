import random

def gerar_raspadinha(simbolos, derrotas_consecutivas, saldo):
    """
    Gera uma nova raspadinha.
    Recebe os simbolos, o contador de derrotas e o saldo atual.
    Retorna (numeros_sorteados, novo_contador_derrotas).
    """

    # MUDANÇA: Remove a linha 'global derrotas_consecutivas'
    # A função agora usa o valor que recebeu no argumento 'derrotas_consecutivas'
    
    # Esta lógica continua, mas usando o argumento 'derrotas_consecutivas'
    if derrotas_consecutivas >= 4:
        n = random.choice(["⭐", "🍀", "💎"]) 
        numeros = [n, n, n]
        derrotas_consecutivas = 0  # Zera a cópia local do contador
    else:
        # MUDANÇA: Usa a lista 'simbolos' que recebeu como argumento
        numeros = [random.choice(simbolos) for _ in range(3)]

    numero = random.randint(1, 100) 
    
    print()
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("[ ? ] [ ? ] [ ? ]")
    
    # MUDANÇA: Usa o 'saldo' que recebeu como argumento
    print(f"Créditos atuais: R$ {saldo:.2f}") 
    print("========================\n")

    # MUDANÇA: Retorna os números E o novo estado do contador de derrotas.
    # Se as derrotas foram zeradas, o main.py saberá disso.
    return numeros, derrotas_consecutivas

def calcular_premio(resultados):
    """
    Calcula o prêmio baseado nos resultados.
    Não controla mais as derrotas.
    Retorna apenas o valor do prêmio (0 se não ganhou).
    """
    
    # MUDANÇA: Remove a linha 'global derrotas_consecutivas'
    
    # Este dicionário pode ficar aqui, pois é específico desta função
    premios = {"🍀": 10, "⭐": 50, "💎": 80}

    if resultados[0] == resultados[1] == resultados[2]:
        # MUDANÇA: Remove 'derrotas_consecutivas = 0'
        # A função não tem mais a responsabilidade de resetar o contador.
        return premios[resultados[0]]

    # MUDANÇA: Remove 'derrotas_consecutivas += 1'
    # A função não deve incrementar as derrotas. O main.py fará isso.
    
    # Apenas retorna 0 se não houve combinação
    return 0