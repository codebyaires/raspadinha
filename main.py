import random
saldo = 0.0
derrotas_consecutivas = 0
simbolos = ["⭐", "🍀", "💎"]

def insert_coin(saldo): 
    while True:
        try:
            print("Escolha uma opção de crédito:")
            print("1- 2,00", "2- 5,00", "3- 10,00", "4- 15,00", "5- 50,00", sep="\n")
            opcao = int(input("Digite o número da opção desejada: "))

            valores = {1: 2, 2: 5, 3: 10, 4: 15, 5: 50}
            if opcao in valores:
                coins = valores[opcao]
                confirmar = input(f"Confirmar R${coins:.2f}? (S/N): ").strip().upper()
                if confirmar == "S":
                    saldo += coins
                    print(f"💰 Crédito adicionado! Novo saldo: R$ {saldo:.2f}")
                    return saldo
                else:
                    print("Operação Cancelada")
            else:
                print("⚠️ Opção inválida, tente novamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números, de 1 a 5.")

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

def descontar_valor(valor_aposta):
    global saldo
    if saldo >= valor_aposta:
        saldo -= valor_aposta
        print(f"R$ {valor_aposta:.2f} descontado da aposta.")
        return True
    else:
        print(f"Saldo insuficiente para apostar. Valor da aposta R$ {valor_aposta:.2f}!")
        saldo_novo = insert_coin(saldo)
        if saldo_novo > saldo:  #só atualiza se realmente entrou crédito
            saldo = saldo_novo
            return descontar_valor(valor_aposta)  #tenta novamente após inserir
        return False

def calcular_premio(resultados):
    global derrotas_consecutivas
    premios = {"🍀": 10, "⭐": 50, "💎": 80}

    if resultados[0] == resultados[1] == resultados[2]:
        derrotas_consecutivas = 0  #ganhou → reseta
        return premios[resultados[0]]

    #perdeu → incrementa
    derrotas_consecutivas += 1
    return 0

def main():
    global saldo
    saldo = 0.0  #saldo inicial do jogador
    valor_aposta = 10.0  #custo fixo da raspadinha

    while True:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
        #opção de saída antes de gerar
        escolha = input("Pressione ENTER para continuar ou digite 'q' para sair: ").strip().lower()
        if escolha == "q":
            print("👋 Obrigado por jogar! Até a próxima.")
            break

        resultados = gerar_raspadinha()
        
        #loop para garantir resposta válida (s, n ou q)
        while True:
            resposta = input("Quer raspar esta raspadinha? (s/n ou q para sair): ").strip().lower()
            if resposta in ('s', 'n', 'q'):
                break
            print("⚠ Digite uma resposta válida (s/n/q).")

        #se o jogador quiser sair no meio da rodada
        if resposta == 'q':
            print("👋 Jogo encerrado pelo jogador.")
            break

        if resposta == 's':
            if not descontar_valor(valor_aposta):
                break

            print("🎉 Resultado da raspadinha:")
            print(f"[ {resultados[0]} ] [ {resultados[1]} ] [ {resultados[2]} ]")
            ganho = calcular_premio(resultados)
            if ganho > 0:
                saldo += ganho
                print(f"➡ Você ganhou R${ganho:.2f}!")
                print(f"Saldo atual R${saldo:.2f}")
            else:
                print("➡ Nada :(")
        else:
            print("Raspadinha não raspada.")
                
if __name__ == "__main__":
    main()
