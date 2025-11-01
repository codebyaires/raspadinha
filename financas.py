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