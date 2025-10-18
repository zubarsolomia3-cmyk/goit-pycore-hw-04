def get_cats_info(path):

    cats = []


    try:

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:


                    continue  
                cat_id, name, age = line.split(",")
                cat_dict = {"id": cat_id, "name": name, "age": age}
                cats.append(cat_dict)
        return cats

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return []

        
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []



cats_info = get_cats_info("cats_file.txt")
print(cats_info)
