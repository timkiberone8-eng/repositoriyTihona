from calculator_modules.arithmetic import add, subtract, multiply, divide;
from advanced import power, square_root;

class NegativeNumberError(Exception):
            """исключение если отрицательное число"""
            pass

def main():
    try:
        x=int(input())
        y=int(input())

        result=0
        a = input("введите операцию (сложение,вычитание,умножение,деление,стпень,корень-только первое число,второе-любое)").lower().strip()
        if a=="сложение":
            result=add(x,y)
            print(result)

        if a=="вычитание":
            result=subtract(x,y)
            print(result)

        if a=="умножение":
            result=multiply(x,y)
            print(result)


        if a=="деление":
            result=divide(x,y)
            print(result)

        if a=="степень":
            result=power(x,y)
            print(result)


        def sqrt_with_check(x):
            """корень с проверкой.Для отрицательного числа выбрасывает свое исключение"""
            if x<0:
                raise NegativeNumberError("ошибка:корень из отрицательного числа не определен")
            return x**0.5

        if a=="корень":
            result=sqrt_with_check(x)
            print(result)


    # except ZeroDivisionError:
    #     print("нельзя делить на ноль")





    except ValueError:
        print("введите правильный тип данных")


    except NegativeNumberError as e:
        print(e)

    finally:
        print("завершено")


if __name__ == "__main__":
    main()