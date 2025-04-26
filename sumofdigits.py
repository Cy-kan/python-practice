def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total

# Example usage
if __name__ == "__main__":
    num = 1234
    print("Sum of digits:", sum_of_digits(num))
