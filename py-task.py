def number(user_input):
    # Проверка на ошибки
    try:
        numbers = list(map(int, user_input.split(', ')))
    except ValueError:
        print("Ошибка! Вводите только числа в формате '1, 2, 3'. Попробуйте снова.")
        return

    # Обработка строки и преобразование в список
    numbers = list(map(int, user_input.split(', ')))
    
    # Поиск и вывод только четных чисел
    even_numbers = [x for x in numbers if x % 2 == 0]
    print(f'Четные числа: {even_numbers}')

    # Поиск и вывод максимального и минимального чисел из списка
    print(f'Максимальное число: {max(numbers)}')
    print(f'Минимальное число: {min(numbers)}')
    
    # Сортировка списка в порядке возрастания
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_numbers[j] > sorted_numbers[j+1]:
                sorted_numbers[j], sorted_numbers[j+1] = sorted_numbers[j+1], sorted_numbers[j]
    print("Отсортированный список:", sorted_numbers)

    
if __name__ == "__main__":
    user_input = input("Введите числа через запятую и пробел (например, '1, 2, 3'): ")
    number(user_input)

