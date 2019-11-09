integer_roman = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),
]


def convert_integer_to_roman(n):
    roman_numeral = []
    for (integer, roman) in integer_roman:
        (quotient, n) = divmod(n, integer)
        roman_numeral.append(roman * quotient)
        if n == 0:
            break
    return "".join(roman_numeral)

print convert_integer_to_roman(1993)
