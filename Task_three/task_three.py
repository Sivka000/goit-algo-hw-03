import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())

    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+380'):
            return cleaned_number
        else:
            return cleaned_number
    else:
        if cleaned_number.startswith('380'):
            return '+' + cleaned_number
        else:
            return '+38' + cleaned_number

def main():
    input_file = "phones.txt" #Текстовий файл з номерами
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            raw_numbers = file.readlines()
    except FileNotFoundError:
        print(f"Файл '{input_file}' Помилка файлу")
        return
    
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки: ", sanitized_numbers)

if __name__ == "__main__":
    main()

