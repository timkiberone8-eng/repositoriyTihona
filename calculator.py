a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
result=0
x= input("Введите операцию (сложение, вычитание, умножение, деление): ").lower().strip()
if x=="сложение":
    result=a+b
elif x=="вычитание":
    result=a-b
elif x=="умножение":
    result=a*b
elif x=="деление":
    result=a/b
else:
    result="Неизвестная операция"

print(result)
