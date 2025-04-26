def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
if __name__ == "__main__":
    num = 7
    print(f"{num} is", check_even_odd(num))
