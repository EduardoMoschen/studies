from random import randint


def main():
    numero_cpf = str(randint(100000000, 999999999))
    novo_cpf = numero_cpf
    reverso = 10
    total = 0

    for indice in range(19):
        if indice > 8:  # Primeiro índice vai de 0 a 9
            indice -= 9  # São os 9 primeiros dígitos do CPF
        total += int(novo_cpf[indice]) * reverso
        reverso -= 1  # Decrementa o contador reverso

        if reverso < 2:
            reverso = 11
            digito = 11 - (total % 11)

            if digito > 9:
                digito = 0

            total = 0
            novo_cpf += str(digito)  # Concatena o dígito gerado no novo CPF

    print(novo_cpf)


if __name__ == "__main__":
    main()