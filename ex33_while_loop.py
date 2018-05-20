numbers = []

def while_function(count):
    i = 0
    while i < count:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


while_function(3)

print("The numbers: ")
for num in numbers:
    print(num)