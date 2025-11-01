import random

def gerar_raspadinha(simbolos, derrotas_consecutivas, saldo):
   
    if derrotas_consecutivas >= 5:
        n = random.choice(["⭐", "🍀", "💎"]) 
        numeros = [n, n, n]
        derrotas_consecutivas = 0  # Zera a cópia local do contador
    else:
        # Usa a lista 'simbolos' que recebeu como argumento
        numeros = [random.choice(simbolos) for _ in range(3)]

    numero = random.randint(1, 100) # Número aleatório para a raspadinha
    
    print()
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("[ ? ] [ ? ] [ ? ]")
    
    # Usa o 'saldo' que recebeu como argumento
    print(f"Créditos atuais: R$ {saldo:.2f}") 
    print("========================\n")

    return numeros, derrotas_consecutivas

def calcular_premio(resultados):
    # Calcula o prêmio baseado nos resultados
    # Retorna apenas o valor do prêmio (0 se não ganhou)

    # Dicionário de prêmios
    premios = {"🍀": 10, "⭐": 50, "💎": 80}

    # Verifica se os três símbolos são iguais
    if resultados[0] == resultados[1] == resultados[2]:

        return premios[resultados[0]]

    return 0