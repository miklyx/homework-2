from datetime import *
from csv import *

def homework_times():
  # вчера
  print(date.today()-timedelta(days=1))

  # сегодня
  print(date.today())

  # месяц назад
  s = datetime.strftime(date.today(),'%Y-%m-%d')
  a = s.split('-')
  if int(a[1])>1 :
    if int(a[1]) < 10:
      a[1]='0'+str(int(a[1])-1)
    else:
      a[1]=str(int(a[1])-1)
  else:
    a[1]='12'
  a1=''
  for i in a:
    a1=a1+i
  t = datetime.strptime(a1,'%Y%m%d')
  print(t)

  # Превратите строку "01/01/17 12:10:03.234567" в объект datetime
  print(datetime.strptime('01/01/17 12:10:03.234567','%d/%m/%y %H:%M:%S.%f'))


"""
Скачайте файл по ссылке
Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
Подсчитайте количество слов в тексте
Замените точки в тексте на восклицательные знаки
Сохраните результат в файл referat2.txt
"""

def homework_files():
  with open('referat.txt', 'r', encoding = 'utf-8') as referat:
    text=referat.read()
    string_length = len(text)
  cnt=len(text.split())
  print(string_length)
  print(cnt)
  print(text.replace('.','!'))
  with open('referat2.txt','w',encoding = 'utf-8') as referat2:
    referat2.write(text)

"""
Создайте список словарей:
        [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
Запишите содержимое списка словарей в файл в формате csv
"""

def list_dict_2_csv():
  list_dict = [
         {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
         {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
         {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
      ]
  with open('list_dict.csv','w',encoding = 'utf-8') as csv_file:
    fields = ['name', 'age' , 'job']
    writer = DictWriter(csv_file,fields,delimiter = ',')
    writer.writeheader()
    for employer in list_dict:
        writer.writerow(employer)
