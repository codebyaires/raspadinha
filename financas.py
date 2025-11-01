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