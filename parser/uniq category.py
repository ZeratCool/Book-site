import csv

# Открываем CSV файл для чтения с указанием кодировки UTF-8
with open('books_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    # Пропускаем заголовок, если он есть
    next(reader, None)

    # Создаем пустой список для хранения значений третьей колонки
    column_3 = []

    # Итерируемся по строкам CSV файла и добавляем значения третьей колонки в список
    for row in reader:
        column_3.append(row[2])

# Выводим список значений третьей колонки
unique_values = list(set(column_3))
print(unique_values)