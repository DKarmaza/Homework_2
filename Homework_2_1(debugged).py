def total_salary(path):
    total_salary = 0
    number_of_developers = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    salary = int(line.split(',')[1])
                    total_salary += salary
                    number_of_developers += 1
                except (ValueError, IndexError):
                    print(f" У рядку '{line.strip()}' вказані не коректні дані.")

        if number_of_developers == 0:
            return 0, 0
    
        average_salary = total_salary / number_of_developers
        return total_salary, average_salary
    except FileNotFoundError:
        print("Файл зa цим шляхом не було знайдено.")
        return 0, 0
    
total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")