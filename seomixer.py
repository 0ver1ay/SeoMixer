
input_file_path = 'E:/WORK/Python/SeoMixer/texts/marker.txt'
output_file_path = 'E:/WORK/Python/SeoMixer/texts/out.txt'

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


def process_line(line):
    parts = line.split(' ')
    category = ' '.join(parts[:-2])  # категория запчастей
    brand = parts[-2]  # марка автомобиля
    model = parts[-1]  # модель автомобиля

    new_lines = []

    new_lines.append(line)

    # Заменяем модель на английскую, если она есть в словаре
    if model in model_replacement:
        # Добавляем строку с замененным брендом и моделью
        new_lines.append(f"{category} Renault {model_replacement[model]}")

    # Добавляем только модель на русском
    new_lines.append(f"{category} {model}")

    # Если модель есть в словаре, добавляем строку с моделью на английском
    if model in model_replacement:
        new_lines.append(f"{category} {model_replacement[model]}")

    # Добавляем дополнительные строки для Сандеро
    if model == 'Сандеро':
        new_lines.append(f"{category} Рено Степвей")
        new_lines.append(f"{category} Renault Stepway")
        new_lines.append(f"{category} Степвей")
        new_lines.append(f"{category} Stepway")

    # Добавляем дополнительные строки для Кангу/Кенго
    if model == 'Кангу':
        new_lines.append(f"{category} Рено Кенго")

    return new_lines


with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
    seen_lines = set()
    for line in input_file:
        line = line.strip()
        if line:  # пропускаем пустые строки
            processed_lines = process_line(line)
            for new_line in processed_lines:
                if new_line not in seen_lines:
                    seen_lines.add(new_line)
                    output_file.write(new_line + '\n')

print("Обработка завершена. Результаты записаны в:", output_file_path)
