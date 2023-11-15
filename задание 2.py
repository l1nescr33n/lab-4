# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"  # переменная с названием входящего файла
OUTPUT_FILENAME = "output.json"  # переменная с названием файла вывода данных


def task() -> None:
    csv_data = []  # Создание списка с переменными
    with open(INPUT_FILENAME, "r") as file:  # Чтение из файла
        reader = csv.DictReader(file, delimiter=',', lineterminator='\n\n')  # Запись из файла в переменную
        for row in reader:
            csv_data.append(row)  # Вывод заглавных столбцов

    with open(OUTPUT_FILENAME, "w", newline='\n') as write_file:  # Запись в Json файл
        json.dump(csv_data, write_file, indent=4)  # Сериализация файла

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
