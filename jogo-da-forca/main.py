from os import name, system


def main():
    palavra_secreta = input("Digite uma palavra: ")
    letras_digitadas = []
    numero_de_tentativas = 3

    if name == "nt":
        system("cls")   # Comando interpretado por SO Windows.
    else:
        system("clear")  # Comando interpretado por SO Linux/Mac.

    while True:
        if numero_de_tentativas <= 0:
            print("Você perdeu!")
            break

        letra = input("Digite uma letra: ")

        if len(letra) > 1:
            print("Por favor, digite apenas uma letra por vez.")
            continue

        # Insere as letras digitadas dentro da lista.
        letras_digitadas.append(letra)

        if letra in palavra_secreta:  # Verifica se a letra está na palavra.
            print(f"A letra {letra} existe na palavra!")
        else:
            print(f"A {letra} não existe na palavra!")
            letras_digitadas.pop()  # Remove a letra que foi inserida na lista.

        # Uma variável temporária para ir guardando as letras que acertar.
        palavra_secreta_temporaria = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_digitadas:
                palavra_secreta_temporaria += letra_secreta
            else:
                palavra_secreta_temporaria += "*"

        if palavra_secreta_temporaria == palavra_secreta:
            print(f"Você ganhou! A palavra é {palavra_secreta_temporaria}.")
            break
        else:
            print(
                f"A palavra secreta está assim: {palavra_secreta_temporaria}")

        if letra not in palavra_secreta:
            numero_de_tentativas -= 1

        print(f"Você ainda tem {numero_de_tentativas}")
        print()


if __name__ == "__main__":
    main()
