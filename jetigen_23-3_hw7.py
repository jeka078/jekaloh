ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
squares = list(map(lambda x: x**2, evens))
print(squares)
def print_element_by_index(index, lst=ten):
    try:
        element = lst[index]
        print(element)
    except IndexError:
        print("Неверно указан индекс. Индекс должен быть от 0 до", len(lst) - 1)
while True:
    index = input("Введите индекс для получения элемента списка (или 'q' для выхода): ")
    if index == 'q':
        break
    try:
        index = int(index)
        print_element_by_index(index)
    except ValueError:
        print("Индекс должен быть целым числом.")
