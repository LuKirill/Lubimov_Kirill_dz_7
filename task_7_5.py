# 5. *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>]), например:
# {
# 100: (15, ['txt']),
# 1000: (3, ['py', 'txt']),
# 10000: (7, ['html', 'css']),
# 100000: (2, ['png', 'jpg'])
# }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
# скрипт.

#######################################################################################################################

import os, json

size_dict = {}
for root, dirs, files in os.walk('my_project'):
    for file in files:
        key_dict = os.stat(os.path.join(root, file)).st_size // 10 * 10 * 10
        f_ext = file.split('.')[-1]
        if key_dict in size_dict:
            size_dict[key_dict][1].append(f_ext)
            size_dict[key_dict] = (size_dict[key_dict][0] + 1, list(set(size_dict[key_dict][1])))
        else:
            size_dict.setdefault(key_dict, (1, [f_ext]))

res_d = {k: size_dict[k] for k in sorted(size_dict.keys())}
print(res_d)
with open('result.json', 'w') as f:
    json.dump(res_d, f)

with open('result.json', 'r') as f:
    print(json.load(f))