def int_to_roman(num):
    # Validate that the input is an integer
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    # Validate that the input is within the valid range (1 to 3999)
    if not 1 <= num <= 3999:
        raise ValueError("Input must be an integer between 1 and 3999 (inclusive)")

    romans = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000]
    ]

    res = ""

    for sym, val in reversed(romans):
        if num // val:
            count = num // val
            res += (sym * count) 
            num = num % val
    return res



def run_test_cases():
    test_cases = [
        (3, "III"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (3999, "MMMCMXCIX"),
        (16, "XVI"),
        (789, "DCCLXXXIX"),
        (150, "CL"),
        (246, "CCXLVI"),
        (3000, "MMM"),
        (1, "I"),
        (390, "CCCXC")
    ]

    for num, expected_result in test_cases:
        try:
            result = int_to_roman(num)
            assert result == expected_result
            print(f"Test passed for input {num}: {result}")
        except AssertionError:
            print(f"Test failed for input {num}. Expected: {expected_result}, Actual: {result}")
        except ValueError as ve:
            print(f"Test failed for input {num}. Error: {ve}")

# Run the test cases
print(run_test_cases())

