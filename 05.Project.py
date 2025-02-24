def count_digits(n):
    count = 0
    tmp = n
    while tmp > 0:
        tmp = tmp // 10
        count = count + 1
    return count

def is_special_number(n):
    digits = count_digits(n)
    tmp = n
    total = 0
    while tmp > 0:
        digit = tmp % 10
        total = total + (digit ** digits)
        tmp = tmp // 10
        if total > n:  # If total exceeds n, skip the rest of the loop
            return False  # Skip checking further if the sum is already too large
    return total == n

def find_special_numbers(start, end):
    print("Special Numbers between", start, "and", end)
    for num in range(start, end + 1):
        if not is_special_number(num):  # Skip numbers that are not special
            continue
        print(num)
    print("Finished checking numbers!")

start_range = int(input("Enter Start of Range: "))
end_range = int(input("Enter End of Range: "))
find_special_numbers(start_range, end_range)
