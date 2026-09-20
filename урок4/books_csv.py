import csv
with open("books.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["название","автор","год"])
    writer.writerow(["гарри поттер","джоан роулинг",1997])
    writer.writerow(["1984","джордж оруэл",1949])

with open("books.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("тоже самое но по человечевки")
with open("books.csv","r",encoding="utf-8") as file:
    reader=csv.reader(file)
    next(reader)
    for title,author,year in reader:
        print(f"{title}-{author}-{year}год")