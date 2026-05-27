nums = "11 1234 11 1234 4567 67 56781"

numbers = nums.split()

print("Reverse List:", numbers[::-1])

unique = sorted(set(numbers), key=int)

print("Second Minimum:", unique[1])

print("Second Maximum:", unique[-2])