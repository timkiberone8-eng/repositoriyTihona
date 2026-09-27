import csv
FILENAME= "task.csv"

def load_task(filename):
    """ "читатет задач из файла.нет файла-начинаем с пустго списка"""
    tasks=[]
    with open(filename,"r",encoding="utf-8") as file:
      reader = csv.reader(file)
      for row in reader:
         tasks.append(row[0])

    return tasks

def save_tasks(filename,tasks):
   """перезаписывает файл текущим списком задач"""
   with open(filename,"w",newline="",encoding="utf-8")as file:
      writer = csv.writer(file)
      for task in tasks:
         writer.writerow([task])

def add_task(tasks,task):
   tasks.append(task)


def show_tasks(tasks):
   if not tasks:
      print("список пуст")

   else:
      print("ваши задачи")
      for i, task in enumerate(tasks,1):
         print(f"{i}.{task}")

def main():
   tasks = load_task(FILENAME)

   while True:
      print("\n1.показать задачаи")
      print("2.добавить адачаи")
      print("3.сохранить и выйти")
      choice=input("выбеите действие").strip()

      if choice=="1":
         show_tasks(tasks)

      elif choice =="2":
            task=input("введите новую заадчу")
            add_task(tasks.task)

      elif choice=="3":
        save_tasks(FILENAME,tasks)
        print("задачаи сохранены , досвидание")
        break
      else:
         print("неверный выбор попробуйе ввести 1,2 или 3")

if __name__== "__main__":
    main()
   