import random
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    unique_numbers = set()
    
    while len(unique_numbers) < quantity:
        number = random.randint(min, max)
        unique_numbers.add(number)
    
    return sorted(unique_numbers)

def main():
    print("Привіт!"
    "\nЦя програма допоможе тобі перемогти в лотереї.")

    try:
        min_num = int(input("Введіть мінімальне число (не менше 1): "))
        max_num = int(input("Введіть максимальне число (не більше 1000): "))
        quantity = int(input("Введіть кількість чисел для вибору: "))

    except ValueError:
        print("Будь ласка, введіть коректні цілі числа.")
        return
    
    result = get_numbers_ticket(min_num, max_num, quantity)

    if not result:
        print("Параметри не відповідають обмеженням або помилка при введенні.")
    else:
        print("Ваші лотерейні числа: ", result)

if __name__ == "__main__":
    main()