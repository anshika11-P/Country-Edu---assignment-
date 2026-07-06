# Question 2- longest Increasing Subsequences

from bisect import bisect_left

# Function to find the length of LIS
def find_lis(numbers):

    if not numbers:
        return 0
    lis = []

    # Check each number in the list
    for num in numbers:
        position = bisect_left(lis, num)
        if position == len(lis):
            lis.append(num)
        else:
            lis[position] = num
    return len(lis)

# Take input from the user
data = input("Enter the list ")
if data == "[]":
    print("Length of LIS: 0")
else:
    data = data.strip("[]")
    numbers = list(map(int, data.split(",")))

#print output
    print("Length of LIS:", find_lis(numbers))