from financas import insert_coin, descontar_valor
from jogo_raspadinha import gerar_raspadinha, calcular_premio

# As variáveis "mestras" do jogo vivem aqui
saldo = 0.0
derrotas_consecutivas = 0
# Você pode adicionar mais símbolos aqui (ex: "🍉", "🔔")
simbolos = ["⭐", "🍀", "💎"] 

def main():
    #'main' controla 'derrotas_consecutivas'
    global saldo, derrotas_consecutivas 
    
    saldo = 0.0  # saldo inicial do jogador
    valor_aposta = 10.0  # custo fixo da raspadinha
    
    # Pede um depósito inicial antes de começar o loop
    print("--- Bem-vindo ao Jogo da Raspadinha! ---")
    saldo = insert_coin(saldo)

    while True:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        
        escolha = input("Pressione ENTER para continuar ou digite 'q' para sair: ").strip().lower()
        if escolha == "q":
            print(f"👋 Obrigado por jogar! Seu saldo final: R$ {saldo:.2f}")
            break

        # Chama 'gerar_raspadinha' passando os argumentos necessários
        # Recebe 2 valores: os resultados e um contador (que vamos ignorar)
        # Usamos '_' para a variável que não vamos usar (o contador de derrotas)
        resultados, _ = gerar_raspadinha(simbolos, derrotas_consecutivas, saldo)
        
        while True:
            resposta = input("Quer raspar esta raspadinha? (s/n ou q para sair): ").strip().lower()
            if resposta in ('s', 'n', 'q'):
                break
            print("⚠ Digite uma resposta válida (s/n/q).")

        if resposta == 'q':
            print(f"👋 Jogo encerrado. Saldo final: R$ {saldo:.2f}")
            break

        if resposta == 's':
            # Chama 'descontar_valor' passando o saldo e a aposta
            # Recebe 2 valores: o novo saldo e um booleano 'pode_jogar'
            saldo, pode_jogar = descontar_valor(saldo, valor_aposta)
            
            # Verifica o booleano 'pode_jogar'
            if not pode_jogar:
                print("Voltando ao menu principal.")
                # 'continue' pula para a próxima iteração do loop 'while True'
                continue 

            # Se chegou aqui, o pagamento foi um sucesso
            print("🎉 Resultado da raspadinha:")
            print(f"[ {resultados[0]} ] [ {resultados[1]} ] [ {resultados[2]} ]")
            
            # Chama 'calcular_premio'
            ganho = calcular_premio(resultados)
            
            if ganho > 0:
                saldo += ganho
                print(f"➡ Você ganhou R${ganho:.2f}!")
                print(f"Saldo atual R${saldo:.2f}")
                
                # MAIN agora é responsável por zerar as derrotas
                derrotas_consecutivas = 0
            else:
                print("➡ Nada :(")
                
                # MAIN agora é responsável por incrementar as derrotas
                derrotas_consecutivas += 1
        else:
            print("Raspadinha não raspada.")
            
if __name__ == "__main__":
    main()