a=int(input())
b=int(input())
result=0
x= input("введите операцию (сложение,вычитание,умножение,деление)").lower().strip()
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
