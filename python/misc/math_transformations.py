def reverse_number(number: int) -> int:
    print(f"Number {number}")
    reverse = 0
    while number > 0:
        last_digit = number % 10
        reverse = (reverse * 10) + last_digit
        number = number // 10
    print(f"Reversed number {reverse}")
    return reverse
