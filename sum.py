def sum_list(elements):
    total = 0
    for num in elements:
        total += num
    return total

# Example usage
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print("Sum of list:", sum_list(numbers))
