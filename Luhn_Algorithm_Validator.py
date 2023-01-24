def luhn_algorithm(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    card_number_digits = digits_of(card_number)