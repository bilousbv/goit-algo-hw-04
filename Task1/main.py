import random
import timeit


# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Вбудований Timsort (через sorted)
def timsort(arr):
    return sorted(arr)


# Функція для порівняння алгоритмів
def compare_sorting_algorithms():
    sizes = [100, 1000, 5000]  # Різні розміри масивів для тестування
    results = {"size": [], "insertion_sort": [], "merge_sort": [], "timsort": []}

    for size in sizes:
        # Генерація випадкового масиву
        arr = [random.randint(0, 10000) for _ in range(size)]

        # Вимірювання часу для сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)

        # Вимірювання часу для сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)

        # Вимірювання часу для Timsort
        timsort_time = timeit.timeit(lambda: timsort(arr.copy()), number=1)

        # Збереження результатів
        results["size"].append(size)
        results["insertion_sort"].append(insertion_time)
        results["merge_sort"].append(merge_time)
        results["timsort"].append(timsort_time)

    # Виведення результатів
    for i in range(len(sizes)):
        print(f"Розмір масиву: {results['size'][i]}")
        print(f"Сортування вставками: {results['insertion_sort'][i]:.6f} секунд")
        print(f"Сортування злиттям: {results['merge_sort'][i]:.6f} секунд")
        print(f"Timsort: {results['timsort'][i]:.6f} секунд")
        print("-" * 40)


compare_sorting_algorithms()