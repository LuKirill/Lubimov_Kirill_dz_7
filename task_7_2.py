# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
# |--settings
# | |--__init__.py
# | |--dev.py
# | |--prod.py
# |--mainapp
# | |--__init__.py
# | |--models.py
# | |--views.py
# | |--templates
# | |--mainapp
# | |--base.html
# | |--index.html
# |--authapp
# | |--__init__.py
# | |--models.py
# | |--views.py
# | |--templates
# | |--authapp
# | |--base.html
# | |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
# ситуации, библиотеки использовать нельзя.

#######################################################################################################################
import os

settings = {}
with open('config.yaml') as f:
    lines = dict(map(str.split, f.readlines()))

basedir = lines.pop('base')
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    print(f'Создан каталог: {k}')
    for i in v.split(','):
        with open(os.path.join(os.curdir, basedir, k, i), 'w') as f:
            print(f'Создан файл: {i} в каталоге {k}')

#######################################################################################################################

#import os
#
# with open("config.yaml", "w", encoding="utf-8") as f:
#     try:
#         f.write()
#     except TypeError:
#         print("Создаем пустой файл config.yaml") структуру создал вручную

# with open("config.yaml", "r", encoding="utf-8") as f:
#     a = f.readlines()
#     for i in a:
#         my_project_folder = a[0].strip()
#         subfolders = a[1].split(" ")[0], a[2].split(" ")[0], a[5].split("\\")[0]
#     my_project_path = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7'
#     new_path = os.path.join(my_project_path, my_project_folder)
#     try:
#         os.mkdir(new_path)
#     except FileExistsError as e:
#         print(f'{e}')
#     else:
#         print(f'Папка успешно создана: {my_project_path}')
#
#     subfolders_path = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project'
#     settings_path = os.path.join(subfolders_path, a[1].split(" ")[0])
#     try:
#         os.mkdir(settings_path)
#     except FileExistsError as e:
#         print(f'{e}')
#     else:
#         print(f'Папка успешно создана: {subfolders_path}')
#
#     mainapp_path = os.path.join(subfolders_path, a[2].split(" ")[0], a[3].split("\\")[0], a[3].split("\\")[1], a[3].split("\\")[2].split(" ")[0].strip())
#     try:
#         os.makedirs(mainapp_path)
#     except FileExistsError as e:
#         print(f'{e}')
#     else:
#         print(f'Папка успешно создана: {subfolders_path}')
#
#     authapp_path = os.path.join(subfolders_path, a[5].split("\\")[0], a[5].split("\\")[1], a[5].split("\\")[2].split(" ")[0].strip())
#     try:
#         os.makedirs(authapp_path)
#     except FileExistsError as e:
#         print(f'{e}')
#     else:
#         print(f'Папка успешно создана: {subfolders_path}')
#
#     settings_path = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project\settings'
#     settings_file_init = os.path.join(settings_path, a[1].split(" ")[1].split(",")[0])
#     settings_file_dev = os.path.join(settings_path, a[1].split(" ")[2].split(",")[0])
#     settings_file_prod = os.path.join(settings_path, a[1].split(" ")[3].split(",")[0].strip())
#     with open(settings_file_init, "w", encoding="utf-8") as fo,\
#         open(settings_file_dev, "w", encoding="utf-8") as fx,\
#             open(settings_file_prod, "w", encoding="utf-8") as fj:
#                 fo.write(settings_path)
#                 fx.write(settings_path)
#                 fj.write(settings_path)
#
#     mainapp_path = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project\mainapp'
#     mainapp_file_init = os.path.join(mainapp_path, a[2].split(" ")[1].split(",")[0])
#     mainapp_file_models = os.path.join(mainapp_path, a[2].split(" ")[2].split(",")[0])
#     mainapp_file_views = os.path.join(mainapp_path, a[2].split(" ")[3].split(",")[0].strip())
#     with open(mainapp_file_init, "w", encoding="utf-8") as fi,\
#         open(mainapp_file_models, "w", encoding="utf-8") as fm,\
#             open(mainapp_file_views, "w", encoding="utf-8") as fv:
#                 fi.write(mainapp_path)
#                 fm.write(mainapp_path)
#                 fv.write(mainapp_path)
#
#     authapp_path = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project\authapp'
#     authapp_file_init = os.path.join(authapp_path, a[4].split(" ")[1].split(",")[0])
#     authapp_file_models = os.path.join(authapp_path, a[4].split(" ")[2].split(",")[0])
#     authapp_file_views = os.path.join(authapp_path, a[4].split(" ")[3].split(",")[0].strip())
#     with open(authapp_file_init, "w", encoding="utf-8") as fi,\
#         open(authapp_file_models, "w", encoding="utf-8") as fm,\
#             open(authapp_file_views, "w", encoding="utf-8") as fv:
#                 fi.write(authapp_path)
#                 fm.write(authapp_path)
#                 fv.write(authapp_path)
#     authapp_subfolder = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project\authapp\templates\authapp'
#     subauthapp_file_base = os.path.join(authapp_subfolder, a[5].split(" ")[1].split(",")[0])
#     subauthapp_file_views = os.path.join(authapp_subfolder, a[5].split(" ")[2].strip())
#     with open(subauthapp_file_base, "w", encoding="utf-8") as fsab,\
#         open(subauthapp_file_views, "w", encoding="utf-8") as fsav:
#             fsab.write(authapp_subfolder)
#             fsav.write(authapp_subfolder)