import random
import time

def exibir_baloes(baloes, escondido):
    print("\nBalões na festa junina:")
    for i, balao in enumerate(baloes, 1):
        if i == escondido:
            print(f"{i}: 🎈 (escondido!)")
        else:
            print(f"{i}: 🎈")
    print()

def jogar_festa_junina():
    pontos = 0
    rodadas = 5

    print("Bem-vindo ao jogo de Estourar Balões - Festa Junina!\n")
    time.sleep(1)

    for rodada in range(1, rodadas + 1):
        print(f"Rodada {rodada} de {rodadas}")
        baloes = [1, 2, 3, 4, 5]
        balao_escondido = random.choice(baloes)

        exibir_baloes(baloes, escondido=None)
        time.sleep(1)
        print("Um balão vai ser escondido... fique atento!")
        time.sleep(2)

        exibir_baloes(baloes, escondido=balao_escondido)

        try:
            chute = int(input("Digite o número do balão que você quer estourar (1-5): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if chute == balao_escondido:
            print("Parabéns! Você estourou o balão certo! 🎉\n")
            pontos += 1
        else:
            print(f"Errou! O balão escondido era o número {balao_escondido}.\n")

        time.sleep(1)

    print(f"Fim do jogo! Você fez {pontos} ponto(s). Obrigado por jogar a Festa Junina!")

if __name__ == "__main__":
    jogar_festa_junina()
4
