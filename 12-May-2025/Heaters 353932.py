# Problem: Heaters - https://leetcode.com/problems/heaters/

def stringToIntHelper(str, index):
    if index == len(str):
        return 0

    # Convert current character to digit
    digit = int(str[index])

    # Recursively compute the rest of the number
    return digit * (10 ** (len(str) - index - 1)) + stringToIntHelper(str, index + 1)

# Wrapper function
def stringToInt(str):
    return stringToIntHelper(str, 0)