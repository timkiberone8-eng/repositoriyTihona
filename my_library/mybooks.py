import csv
FILENAME="my_books.csv"
def add_book(title,author,year):
    """дописывае одну книгу в кнце файла"""
    with open(FILENAME,"a",newline="",encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title,author,year])

def show_books():
    """печатат все книги из файла"""
    try:
        with open(FILENAME,"r",encoding="utf-8") as file:
            reader = csv.reader(file)
            books = list(reader)
    except FileNotFoundError:
        print("файл не найден пока что нет книг")
        return

    if not books:
        print("книг пока нет")
        return

    print("ваши книги:")
    for i,book in enumerate(books,1):
        title,author,year=book
        print(f"{i}.{title}-{author},{year}")

def main():
    while True:
        print("\n1.добавить книгу")
        print("2.показать все книги")
        print("3.выход")
        choice=input("выберите пункт:").strip()

        if choice=="1":
            title=input("название:")
            author=input("автор:")
            year=input("год:")
            add_book(title,author,year)
            print("книга добавлена")
        elif choice=="2":
            show_books()
        elif choice=="3":
            print("до свидания")
            break
        else:
            print("нет такого пункта, введите 1,2 или 3")


if __name__=="__main__":
    main()
