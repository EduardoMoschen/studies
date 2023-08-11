def main():
    cpf = input("Digite um CPF: ")
    novo_cpf = cpf[:-2]  # Elimina os dois últimos dígitos do número do CPF
    reverso = 10  # Contador reverso
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
    #  Evita sequência como 11111111111, 00000000000, ...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print("CPF válido!")
    else:
        print("CPF inválido!")


if __name__ == "__main__":
    main()
    