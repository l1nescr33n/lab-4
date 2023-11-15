# TODO решите задачу
import json

INPUT_FILE = "input.json"  # Создаём переменную с названием файла


def task() -> float:
    with open(INPUT_FILE, "r") as input_file:  # Чтение файла
        summary = 0  # Создание переменной, в которой будет высчитываться сумма значений словарей
        json_file = json.load(input_file)  # Десериализация данных Json
        for i in range(0, len(json_file)):  # Перебор словарей в списке
            json_result = json_file[i]["score"] * json_file[i]["weight"]  # Перемножение значений словарей
            summary += json_result  # Суммирование перемноженных значений
        return round(summary, 3)


print(task())
