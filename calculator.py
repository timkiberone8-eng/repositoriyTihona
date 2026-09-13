a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
result=0
x= input("Введите операцию (сложение, вычитание, умножение, деление): ").lower().strip()
if x=="сложение":
    result=a+b
    print(result)

if x=="вычитание":
    result=a-b
    print(result)

if x=="умножение":
    result=a*b
    print(result)


if x=="деление":
    result=a/b
    print(result)
