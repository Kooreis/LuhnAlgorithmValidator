odd_digits = card_number_digits[-1::-2]
    even_digits = card_number_digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)