
def quick_sort(arr):        # создаем функцию в параметры которой будем передавать массив arr
    if len(arr)<= 1:        # првоеряем если длина массива <= 1 ТУТ МЕСТО ГДЕ РЕКУРСИЯ БУДТ ЗАВЕРШАТЬ РАБОТУ
        return arr          # возвращаем массив
    else:                   # ИНАЧЕ
        pivot = arr[0]      # создали переменную в которую будем сохранять 1й элемент
# создадим 2 массива: в 1й запишем все значения которые < arr[0] т.е. первого элемента - pivot во второй массив > переменной pivot
    less = [i for i in arr[1:] if i <= pivot]                   # с помощью генератора списка кладем значения i, 1й элемент брать не надо т.к. он нам уже известен т.е. берем все элементы после 1го [1:] т.е. <= переменной pivot
    greater = [i for i in arr[1:] if i > pivot]   
    return quick_sort(less) + [pivot] + quick_sort(greater)     # т.к. элементы неотсортированны вызываем функцию НЕЛЬЗЯ СКЛАДЫВАТЬ СПИСОК С КАКИМ ТО ЧИСЛОМ ПО ЭТОМУ PIVOT НАДО ПРЕОБРАЗОВАТЬ В СПИСОК 
print(quick_sort([14,45,76,34,87,3,6,83,12,3]))
