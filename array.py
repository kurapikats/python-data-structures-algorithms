numbers = [10, 20, 300, 40, 50]

# random indexing --> O(1) get items if we know the index !!!
print(numbers[4])

# it can store different data types
# numbers[1] = "Adam"

# iteration methods

# for i in range(len(numbers)):
#     print(numbers[i])

# for num in numbers:
#     print(num)

# remove last two items
print(numbers[:-2])

# show only first 2 items
print(numbers[0:2])

# show 3rd item onwards
print(numbers[2:])

# get the highest number in the array
# O(n) linear time complexity
# this type of search is slow on large array
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)
