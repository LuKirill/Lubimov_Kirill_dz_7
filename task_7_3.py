# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# | |--mainapp
# | | |--base.html
# | | |--index.html
# | |--authapp
# | |--base.html
# | |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации; это реальная задача, которая решена, например, во
# фреймворке django.

import os, shutil

path_templates = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7'
templates_folder = os.path.join(path_templates, "templates")
try:
    os.mkdir(templates_folder)
except FileExistsError as e:
    print(f'{e}')
else:
    print(f'Папка успешно создана: {path_templates}')

root_src_dir = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\my_project'
root_dst_dir = r'C:\Users\kiril\PycharmProjects\Lubimov_Kirill_dz_7\templates'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_dir):
            os.remove(dst_file)
        shutil.copy(src_file, dst_dir)