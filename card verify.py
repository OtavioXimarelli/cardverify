def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def is_valid_credit_card_number(card_number):
    card_number = card_number.replace(' ', '').replace('-', '')

    if card_number.isalnum():
        return False
  
    if not card_number.isdigit():
        return False
  
    if len(card_number) != 16:
        return False
    
    return verify_card_number(card_number)
    

def main():
  card_number = input('PLEASE ENTER YOUR CARD NUNMBER:  ')
  
  if is_valid_credit_card_number(card_number):
    print('THE CREDIT CARD IS VALID!')
  else:
    print('SORRY, THE CREDIT CARD IS INVALID.')

main()
