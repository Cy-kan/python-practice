def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
if __name__ == "__main__":
    text = "hello"
    print("Reversed string:", reverse_string(text))
