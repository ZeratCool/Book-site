import csv
from googletrans import Translator

def translate_csv(input_file, output_file):
    translator = Translator()

    with open(input_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

        translated_rows = []
        for row in rows:
            translated_row = []
            for item in row:
                translated_item = translator.translate(item, src='ru', dest='en').text
                translated_row.append(translated_item)
            translated_rows.append(translated_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(translated_rows)

if __name__ == "__main__":
    input_filename = input("Введите имя входного CSV файла: ")
    output_filename = input("Введите имя выходного CSV файла: ")
    translate_csv(input_filename, output_filename)
    print("Перевод завершен. Новый файл сохранен как", output_filename)
