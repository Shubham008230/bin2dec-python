def bin_to_dec(text):
    """Returns the decimal value of a binary string, or None if invalid."""
    total = 0
    length = len(text)
    for index, char in enumerate(text):   # loop over the string directly, no array
        if char not in '01':
            return None         # invalid character found
        if char == "1":
            position = length - 1 - index    # rightmost digit is position 0
            total += 2 ** position           # the single math operation: power of 2
    return total


def main():
    while True:
        text = input("Enter up to 8 bits of binary (or 'q' to quit): ").strip()
        if text.lower() == 'q':
            break
        if not text or len(text) > 8:
            print("Please enter between 1 and 8 digits.")
            continue
        result = bin_to_dec(text)
        if result is None:
            print("Error: only 0s and 1s are allowed.")
        else:
            print(f"Decimal value: {result}")


if __name__ == "__main__":
    main()

