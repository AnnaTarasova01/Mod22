try:
    array = list(map(int, input("Введите числа в произвольном порядке через пробел:").split()))
    element = int(input("Введите одно произвольное число:"))

except ValueError:
        print("Только цифры!!")

 #сортировка
else:
    def sort_list(array):
         m = len(array)
         for i in range(m):
             for j in range(i+1, m):
                 if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
         is_sort = True
         return array

#поиск числа
    def binary_search(array, element, left, right):
        if left > right:  # если левая граница превысила правую,
             return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] >= element and array[middle - 1] < element:   # если элемент в середине,
            return middle -1  # возвращаем этот индекс
        elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)

    print ('Отсортированный список:', sort_list(array))
    left = min(array)
    right = max(array)
    if element < left or element > right:
        print("Число не входит в диапазон")
    else:
        print("Число входит в диапазон")



