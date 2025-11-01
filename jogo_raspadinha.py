def gerar_raspadinha():
    global derrotas_consecutivas

    #Se perdeu 4 vezes seguidas, a próxima é vitória garantida
    if derrotas_consecutivas >= 4:
        n = random.choice(["⭐", "🍀", "💎"])   #escolhe qual símbolo vai dar vitória
        numeros = [n, n, n]
        derrotas_consecutivas = 0
    else:
        numeros = [random.choice(simbolos) for _ in range(3)]

    numero = random.randint(1, 100) 
    
    print()
    print(" Raspadinha ".center(40, "-"))
    print(f"Número da Raspadinha: {numero}")
    print("[ ? ] [ ? ] [ ? ]")
    print(f"Créditos atuais: R$ {saldo:.2f}")
    print("========================\n")

    return numeros