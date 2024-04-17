def verify_card_number(card_number):
    # Function to verify if a credit card number is valid
    # Função para verificar se um número de cartão de crédito é válido
    sum_of_odd_digits = 0
    # Reverse the card number to simplify the calculation
    # Inverte o número do cartão para simplificar o cálculo
    card_number_reversed = card_number[::-1]
    # Extract odd-positioned digits
    # Extrai os dígitos em posições ímpares
    odd_digits = card_number_reversed[::2]

    # Sum the odd-positioned digits
    # Soma os dígitos em posições ímpares
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Extract even-positioned digits
    # Extrai os dígitos em posições pares
    even_digits = card_number_reversed[1::2]
    # Double the even-positioned digits and sum them up
    # Dobra os dígitos em posições pares e soma-os
    for digit in even_digits:
        number = int(digit) * 2
        # If the result is two digits, sum them up individually
        # Se o resultado tiver dois dígitos, soma-os individualmente
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    # Check if the total sum is divisible by 10
    # Verifica se a soma total é divisível por 10
    return total % 10 == 0


def is_valid_credit_card_number(card_number):
    # Function to check if a credit card number is valid
    # Função para verificar se um número de cartão de crédito é válido
    card_number = card_number.replace(' ', '').replace('-', '')

    # Check if the card number contains only digits and has a length of 16
    # Verifica se o número do cartão contém apenas dígitos e tem um comprimento de 16 caracteres
    if not card_number.isdigit() or len(card_number) != 16:
        return False

    return verify_card_number(card_number)


def main():
    # Main function
    # Função principal
    card_number = input('PLEASE ENTER YOUR CARD NUMBER: ')

    if is_valid_credit_card_number(card_number):
        print('THE CREDIT CARD IS VALID!')
    else:
        print('SORRY, THE CREDIT CARD IS INVALID.')


if __name__ == "__main__":
    main()
