import heapq


def merge_k_lists(lists):
    # Використання купи для об'єднання списків
    min_heap = []

    # Додаємо початкові елементи кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)

    merged_list = []

    # Поки купа не порожня, видаляємо найменший елемент і додаємо наступний
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)

        # Додаємо наступний елемент із того ж списку до купи, якщо він існує
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)