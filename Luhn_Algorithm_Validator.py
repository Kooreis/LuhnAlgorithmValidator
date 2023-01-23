def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    card_number_digits = digits_of(card_number)
    odd_digits = card_number_digits[-1::-2]
    even_digits = card_number_digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_algorithm(card_number) == 0

while True:
    card_number = input("Enter a card number to validate or 'q' to quit: ")
    if card_number == 'q':
        break
    if is_luhn_valid(card_number):
        print("This is a valid card number.")
    else:
        print("This is not a valid card number.")