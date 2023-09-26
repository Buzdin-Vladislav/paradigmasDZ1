import random


def search_imp(target, array):
    for num in array:
        if num == target:
            return True
    return False


array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print(array)

print(search_imp(5, array))