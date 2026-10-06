#3.1 list operations 
fivefoods = ["hotdog", "sushi", "pasta", "salad", "soup"]
print(fivefoods[1])
print(fivefoods[-1])
fivefoods.append("blackberry")
fivefoods.insert(0, "apple")
del fivefoods[2]
print(len(fivefoods))

for x in fivefoods:
    print(x.upper())

newlist = fivefoods[0:5:4]
#debugging 1: I wrote to jump 5 insted of 4 at first, so it was not printing the last item in the list.

if "potato" in fivefoods:
    print("A potato!")
else:
    print("No potato!")

#3.2 slicing and striding 
numbers1 = list(range(0,20))
#debugging #2: at first I did not define numbers as a list but just a range, which made all the functions not work. 
def get_first_15(numbers1):
    return numbers1[0:15]

def get_every_5th(lst):
    return lst[0:20:5]
#debugging 2: I forgot to put def before the function name, so the function was invalid.


def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers1)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

#3.3 nested lists
list_1 = [1, 2, 3]
list_2 =[4, 5, 6]
list_3 = [7, 8, 9]
numbers2 = [[1,2,3], [4,5,6], [7,8,9]]

#3.3.1
print(numbers2[2][0:3:1])
print(numbers2[1][1])
numbers2.append([10, 11, 12])

def sums_nested(lst):
    total = 0
    for sublist in lst:
        total += sum(sublist)
    return total

#3.4 create a 5x5 list
def create_5x5_list():
    numbers = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(i * 5 + j + 1)
        numbers.append(row)
    return numbers
numbers3 = create_5x5_list()
def multiples_of_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = "?"
    return lst
def sum_5x5(lst):
    total = 0
    for sublist in lst:
        for num in sublist:
            if num != "?":
                total += num
    return total
#4 dictionaries
ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Maria": 48}
print(ages["Katie"])
ages["Mira"] = 100
ages["Miana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(name, age)

#5 running your code 
print(create_5x5_list())