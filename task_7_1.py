# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
# |--settings
# |--mainapp
# |--adminapp
# |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
# лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?

#######################################################################################################################

import os

project_path = 'my_project'
paths = ['setting', 'mainapp', 'adminapp', 'authapp']
for d in paths:
    os.makedirs(os.path.join(os.curdir, project_path, d), exist_ok=True)

#######################################################################################################################

# import os
#
# path1 = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7'
# folder = 'my_project'
# if not os.path.exists(folder):
#     os.mkdir(folder)
#
# path2 = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project'
# folders = "settings", "mainapp", "adminapp", "authapp"
# for i in folders:
#     new_path = os.path.join(path2, i)
#     try:
#         os.makedirs(new_path)
#     except FileExistsError as e:
#         print(f'{e}')
#     else:
#         print(f'Папка успешно создана: {path2}')
#
#
# with open("starter.txt", "a", encoding="utf-8") as f,\
#     open("starter.txt", "a", encoding="utf-8") as file:
#     for t in os.listdir(path2):
#         f.write(t + '\n')
#     file.write(folder + '\n')