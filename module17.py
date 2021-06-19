def ranging(list_sequence):
    for i in range(len(list_sequence)):
         for j in range(len(list_sequence) - i - 1):
            if list_sequence[j] > list_sequence[j + 1]:
                list_sequence[j], list_sequence[j + 1] = list_sequence[j + 1], list_sequence[j]


def binary_search(list_sequence, element, left, right):
  print("left: ", left, ", right: ", right)
  if left > right:  # если левая граница превысила правую,
    return right  # значит элемент отсутствует
  middle = (right + left) // 2  # находимо середину
  print("middle: ", middle)
  if list_sequence[middle] == element:  # если элемент в середине,
    return middle - 1  # возвращаем этот индекс
  elif element < list_sequence[middle]:  # если элемент меньше элемента в середине
    # рекурсивно ищем в левой половине
    return binary_search(list_sequence, element, left, middle - 1)
  else:  # иначе в правой
    return binary_search(list_sequence, element, middle + 1, right)


sequence = input("Ввести последовательность целых чисел через пробел")
element = int(input("Введите число"))
list_sequence = list(map(int,(sequence).split()))
print(list_sequence)
ranging(list_sequence)
print(list_sequence)
print(list_sequence[len(list_sequence)-1])
if element <= list_sequence[0] or element > list_sequence[len(list_sequence)-1]:
  print("Нужно вводить целое число в пределах последовательности и не равное первому элементу последовательности")
  exit()

print("отсортированная последовательность", list_sequence)
print("элемент, который ищем", element)
print("запускаем поиск")
print(binary_search(list_sequence, element, 0, len(list_sequence)-1))
print("поиск завершен")