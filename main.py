from calculator_modules.arithmetic import add, subtract, multiply, divide;

x=int(input())
y=int(input())
result=0
a = input("введите операцию (сложение,вычитание,умножение,деление)").lower().strip()
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


# if __name__ == "__main__":
#     main()