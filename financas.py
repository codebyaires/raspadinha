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
                    saldo += coins  # Adiciona ao 'saldo' que a função recebeu
                    print(f"💰 Crédito adicionado! Novo saldo: R$ {saldo:.2f}")
                    return saldo  # Retorna o novo saldo para o main.py
                else:
                    print("Operação Cancelada")
                    # MUDANÇA: Se o usuário cancelar, a função deve parar e
                    # retornar o saldo original, sem alterações.
                    return saldo 
            else:
                print("⚠️ Opção inválida, tente novamente.")

        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números, de 1 a 5.")
            
def descontar_valor(saldo_atual, valor_aposta):
    """
    Tenta descontar a aposta do saldo. 
    Retorna (novo_saldo, True) se conseguir.
    Retorna (saldo_original, False) se não conseguir.
    """
    
    # MUDANÇA: A função agora usa 'saldo_atual' que recebeu como argumento
    # em vez de 'global saldo'.
    
    if saldo_atual >= valor_aposta:
        saldo_atual -= valor_aposta
        print(f"R$ {valor_aposta:.2f} descontado da aposta.")
        # MUDANÇA: Retorna o saldo atualizado e True (sucesso)
        return saldo_atual, True
    else:
        print(f"Saldo insuficiente para apostar. Valor da aposta R$ {valor_aposta:.2f}!")
        
        # MUDANÇA: Pergunta se o usuário quer adicionar crédito
        quer_adicionar = input("Deseja adicionar mais créditos? (s/n): ").strip().lower()
        
        if quer_adicionar == 's':
            # MUDANÇA: Chama insert_coin, passando o saldo atual
            saldo_apos_inserir = insert_coin(saldo_atual)
            
            # MUDANÇA: Verifica se o usuário realmente adicionou crédito
            if saldo_apos_inserir > saldo_atual:
                # Se adicionou, tenta descontar novamente
                # O 'return' passa o resultado da nova tentativa para cima
                return descontar_valor(saldo_apos_inserir, valor_aposta)
            else:
                # Usuário cancelou a inserção de crédito
                print("Operação cancelada. Aposta não realizada.")
                # MUDANÇA: Retorna o saldo original e False (falha)
                return saldo_atual, False 
        else:
            # Usuário não quis adicionar créditos
            print("Aposta não realizada.")
            # MUDANÇA: Retorna o saldo original e False (falha)
            return saldo_atual, False