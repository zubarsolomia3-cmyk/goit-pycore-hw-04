def total_salary(path):

    
    try:
        total = 0
        count = 0
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()  
                if not line:  
                    continue
                name, salary = line.split(",")  
                total += int(salary)
                count += 1

        if count > 0:
            average = total / count
        else:
            average = 0
        return total, average

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
