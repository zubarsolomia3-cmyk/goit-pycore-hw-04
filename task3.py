import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)

def print_directory_structure(directory, indent=0):
    
    
    """
    Рекурсивно виводить структуру директорії з кольорами
    """
    for item in directory.iterdir():
        if item.is_dir():
            print(" " * indent + Fore.BLUE + f"[{item.name}]")  
            print_directory_structure(item, indent + 4)
        else:
            
            print(" " * indent + Fore.GREEN + item.name)  # зелений — файли

def main():
    
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: вкажіть шлях до директорії.")
        return

    path = Path(sys.argv[1])

   
    if not path.exists():
        print(Fore.RED + "Помилка: вказаний шлях не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + "Помилка: шлях не є директорією.")
        return

    print(Fore.YELLOW + f"Структура директорії: {path}\n")
    print_directory_structure(path)



if __name__ == "__main__":
    main()
