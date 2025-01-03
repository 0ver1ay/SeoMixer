import os

# Маппинг моделей на английские названия
model_mapping = {
    'Аркана': 'Arkana',
    'Мастер': 'Master',
    'Кангу': 'Kangoo',
    'Логан': 'Logan',
    'Дастер': 'Duster',
    'Колеос': 'Koleos',
    'Каптур': 'Captur',
    'Клио': 'Clio',
    'Лагуна': 'Laguna',
    'Меган': 'Megane',
    'Сандеро': 'Sandero',
    'Сценик': 'Scenic',
    'Симбол': 'Symbol',
    'Трафик': 'Trafic',
}

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []

    for line in lines:
        # Заменяем 'Рено' на 'Renault'
        modified_line = line.replace('Рено', 'Renault')

        for russian_model, english_model in model_mapping.items():
            modified_line = modified_line.replace(russian_model, english_model)

        modified_lines.append(modified_line)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write("\n")
        file.writelines(modified_lines)

def process_folder(folder_path):
    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path)

folder_path = 'E:/WORK/Python/SeoMixer/russian'

process_folder(folder_path)
