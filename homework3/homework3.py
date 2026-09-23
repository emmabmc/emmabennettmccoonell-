def say_goodbye(message):
    print(message)
say_goodbye("goodbye")

def area_of_circle(radius):
    area = 3.14 * radius ** 2
    return area
print(area_of_circle(5))

def subtract(a, b):
    return a - b
print(subtract(10, 5))

def multiply(a, b):
    return a * b
print(multiply(4, 3))

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
print(divide(10, 2))

def what_to_wear(temperatures):
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return(min_temp, max_temp)
print(what_to_wear([30, 40, 50, 60, 70]))

def week_or_end(day):
    if day <= 5:
        return "Weekday"
    else:
        return "Weekend"
print(week_or_end(3))

def fuel_efficiency(miles, gallons):
    if gallons == 0:
        return "Error: Gallons cannot be zero"
    return miles / gallons
print(fuel_efficiency(100, 10))

def secret_code(int):
    y = str(int % 10)
    z = str(int // 10)
    return (y + z)
print(secret_code(12345))

def oski(x, y):
    z = 1
    for i in range(y):
        z = z * x
    return (z)
print(oski(2, 3))

def for_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num
print(for_min([5, 3, 8, 1, 4]))

def for_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
print(for_max([5, 3, 8, 1, 4]))

def while_min(nums):
    min_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_num:
            min_num = nums[i]
        i += 1
    return min_num
print(while_min([5, 3, 8, 1, 4]))

def while_max(nums):
    max_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_num:
            max_num = nums[i]
        i += 1
    return max_num
print(while_max([5, 3, 8, 1, 4]))

def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum([5, 3, 8, 1, 4]))

t= fuel_efficiency(100, 10)
print("The fuel efficiency of your ride is:", t)
