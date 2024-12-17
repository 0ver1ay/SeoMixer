def remove_duplicates(file_path):
    # Читаем содержимое файла
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Удаляем дубликаты, сохраняя порядок
    unique_lines = list(dict.fromkeys(lines))

    # Перезаписываем файл без дубликатов
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)

file_path = 'E:/WORK/Python/SeoMixer/russian/stepway.txt'
remove_duplicates(file_path)
