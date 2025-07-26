def digitSum(s): # function to return all digits in string

    total = 0
    for ch in s: # loop through each character in string s
        if ch.isdigit(): # check if character is a digit and add it to total if true
            total += int(ch)
    return total


def maxDigitSum(strings): # function to return highest digit from strings

    maxSum = 0
    for s in strings: # loop through all strings in list
        currentSum = digitSum(s)
        if currentSum > maxSum: # if sum is higher that current, change it
            maxSum = currentSum
    return maxSum



input1 = ["dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw"]
result = maxDigitSum(input1)
print(f"Maximum digit sum is: {result}")