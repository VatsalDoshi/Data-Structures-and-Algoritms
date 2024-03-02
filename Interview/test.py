def intToRoman(num):
    result = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]
    return result


# Test Cases:
print(intToRoman(3))  # Output: "III"
print(intToRoman(58))  # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"
