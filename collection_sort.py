"""Сортировка списка v2."""
array = [3, 5, 2, 11, 10, 8, 2, 2, 3]
print(array)

for n in range(len(array)):
    min_value_index = n

    for i in range(n, len(array)):
        if array[min_value_index] > array[i]:
            min_value_index = i

    array[n], array[min_value_index] = array[min_value_index], array[n]

print(array)
