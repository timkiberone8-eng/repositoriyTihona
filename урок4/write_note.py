with open("example.txt","w",encoding="utf-8") as file:
     file.write("сегодня мы учились работать с файлами\n")


with open("note.txt","a",encoding="utf-8") as file:
     file.write("а это вторая строка.\n")


note=input("введите свою заметку")
with open("note.txt","a",encoding="utf-8") as file:
    file.write(note+"\n")

print("---что теперь в файле note.txt---")

with open("note.txt","r",encoding="utf-8") as file:
    print(file.read())