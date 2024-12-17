# Определяем пути к входному файлу и файлам для каждой модели
input_file_path = 'E:/WORK/Python/SeoMixer/texts/out.txt'  # Файл, в котором ищем строки
model_replacement = {
    'Сандеро': 'Sandero',
    'Трафик': 'Trafic',
    'Сценик': 'Scenic',
    'Симбол': 'Symbol',
    'Меган': 'Megane',
    'Мастер': 'Master',
    'Логан': 'Logan',
    'Лагуна': 'Laguna',
    'Колеос': 'Koleos',
    'Клио': 'Clio',
    'Каптур': 'Captur',
    'Кангу': 'Kangoo',
    'Дастер': 'Duster',
    'Аркана': 'Arkana',
}

# Функция для записи строк в файл по модели
def write_model_lines(model):
    model_file_name = model_replacement[model].lower() + '.txt'  # имя выходного файла
    model_file_path = f'E:/WORK/Python/SeoMixer/texts/models/{model_file_name}'

    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
         open(model_file_path, 'w', encoding='utf-8') as model_file:

        for line in input_file:
            if model in line:  # Проверяем, содержит ли строка модель
                model_file.write(line)

    print(f"Строки для модели '{model}' записаны в файл: {model_file_path}")

# Перебор всех моделей в словаре
for model in model_replacement.keys():
    write_model_lines(model)
