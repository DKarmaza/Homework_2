def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat = line.strip().split(',')
                cat_dict = { 
                    "id": cat[0],
                    "name": cat[1],
                    "age": cat[2]
                }
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл зa цим шляхом не було знайдено")

    return cats_info

cats_info = get_cats_info("cats_list.txt")
print(cats_info)
