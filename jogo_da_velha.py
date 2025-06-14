import random
import time

def criar_tabuleiro(tamanho=4):
    # Criar pares de letras (exemplo: A, B, C, ...)
    letras = [chr(i) for i in range(65, 65 + (tamanho * tamanho) // 2)]
    cartas = letras * 2
    random.shuffle(cartas)

    # Monta o tabuleiro como matriz
    tabuleiro = []
    for i in range(tamanho):
        linha = cartas[i * tamanho:(i + 1) * tamanho]
        tabuleiro.append(linha)
    return tabuleiro

def exibir_tabuleiro(tabuleiro, revelados):
    tamanho = len(tabuleiro)
    print("\n   " + "  ".join(str(i) for i in range(tamanho)))
    print("  " + "---" * tamanho)
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if (i, j) in revelados:
                linha.append(tabuleiro[i][j])
            else:
                linha.append("*")
        print(f"{i} | " + "  ".join(linha))
    print()

def jogo_da_memoria():
    tamanho = 4
    tabuleiro = criar_tabuleiro(tamanho)
    revelados = set()
    tentativas = 0

    while len(revelados) < tamanho * tamanho:
        exibir_tabuleiro(tabuleiro, revelados)

        try:
            print("Escolha a primeira carta para virar:")
            l1 = int(input("Linha: "))
            c1 = int(input("Coluna: "))
            if (l1, c1) in revelados or not (0 <= l1 < tamanho and 0 <= c1 < tamanho):
                print("Posição inválida ou já revelada, tente novamente.")
                continue

            print("Escolha a segunda carta para virar:")
            l2 = int(input("Linha: "))
            c2 = int(input("Coluna: "))
            if (l2, c2) in revelados or not (0 <= l2 < tamanho and 0 <= c2 < tamanho) or (l1 == l2 and c1 == c2):
                print("Posição inválida ou já revelada, tente novamente.")
                continue

        except ValueError:
            print("Por favor, digite números válidos.")
            continue

        # Mostrar as cartas escolhidas
        exibir_tabuleiro(tabuleiro, revelados | {(l1, c1), (l2, c2)})

        if tabuleiro[l1][c1] == tabuleiro[l2][c2]:
            print("Par encontrado!")
            revelados.add((l1, c1))
            revelados.add((l2, c2))
        else:
            print("Não é um par. Tente novamente.")
            time.sleep(2)  # pausa para o jogador memorizar
        tentativas += 1

    print(f"Parabéns! Você encontrou todos os pares em {tentativas} tentativas.")

if __name__ == "__main__":
    jogo_da_memoria()
2

