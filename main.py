from models import Calculator

calc = Calculator()

while True:
    print("\n" + "=" * 40)
    print("КАЛКУЛАТОР на МЦЦ")
    print("=" * 40)
    print("1. Събиране")
    print("2. Изваждане")
    print("3. Умножение")
    print("4. Деление")
    print("5. Степен")
    print("6. Квадратен корен")
    print("7. Остатък (%)")
    print("8. Целочислено деление (//)")
    print("9. Абсолютна стойност")
    print("10. Процент")
    print("11. Факториел")
    print("12. Изход")

    choice = input("\nИзберете операция: ")

    if choice == "12":
        print("Довиждане!")
        break

    try:
        if choice in ["1", "2", "3", "4", "5", "7", "8", "10"]:
            a = float(input("Първо число: "))
            b = float(input("Второ число: "))

            if choice == "1":
                print(calc.add(a, b))

            elif choice == "2":
                print(calc.subtract(a, b))

            elif choice == "3":
                print(calc.multiply(a, b))

            elif choice == "4":
                print(calc.divide(a, b))

            elif choice == "5":
                print(calc.power(a, b))

            elif choice == "7":
                print(calc.modulo(a, b))

            elif choice == "8":
                print(calc.floor_divide(a, b))

            elif choice == "10":
                print(calc.percentage(a, b))

        elif choice in ["6", "9", "11"]:
            a = float(input("Въведете число: "))

            if choice == "6":
                print(calc.square_root(a))

            elif choice == "9":
                print(calc.absolute(a))

            elif choice == "11":
                print(calc.factorial(a))

        else:
            print("Невалиден избор!")

    except ValueError:
        print("Грешка: въведете валидно число!")