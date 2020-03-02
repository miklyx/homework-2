from collections import Counter

"""
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

lst=[]
for i in students:
  lst.append(i.get('first_name'))
c = Counter(lst)
for k,v in c.items():
  print(k+': '+str(v))
  

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
  {'first_name': 'Оля'},
]
# ???
lst=[]
for i in students:
  lst.append(i.get('first_name'))
c = Counter(lst)
print("Самое частое имя среди учеников:",c.most_common(1)[0][0])


# Пример вывода:
# Самое частое имя среди учеников: Маша



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

lst=[]
k = 1
for i in school_students:
  #print(i)
  for j in i:
   # print(j)
    lst.append(j.get('first_name'))
  c = Counter(lst)
  print("Самое частое имя в классе ",k, ":",c.most_common(1)[0][0])
  k += 1
  lst =[]


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
"""
def computeMaleFemale(school, is_male):
  if not school:
    school = [
      {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
      {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
      ]
  if not is_male:
    is_male = {
      'Маша': False,
      'Оля': False,
      'Олег': True,
      'Миша': True,
     }
  mlst=[]
  dlst=[]
  dlstr=[]
  mlstr=[]
  classes = {}
  classes['female'] = ''
  classes['male'] = ''
  for i in school:
    for j in i.get('students'):
      if is_male.get(j.get('first_name')):
        mlst.append(j.get('first_name'))
      else:
        dlst.append(j.get('first_name'))
    #print("В классе "+i.get('class')+" "+str(len(dlst))+" девочки и "+str(len(mlst))+" мальчика")
    mlstr.append({i.get('class'):len(mlst)})
    dlstr.append({i.get('class'):len(dlst)})
    mlst = []
    dlst = []
  classes['female']=dlstr
  classes['male'] = mlstr
  return classes  
  
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
def main():
  school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  ]
  is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
  }
  m = 0
  mc = 0
  d = 0
  dc = 0
 
  for i in computeMaleFemale(school,is_male)['male']:
    if list(i.values())[0] > m:
      m = list(i.values())[0]
      mc = list(i.keys())[0]
  for i in computeMaleFemale(school,is_male)['female']:
    if list(i.values())[0] > d:
      d = list(i.values())[0]
      dc = list(i.keys())[0]
  print("Больше всего мальчиков в классе "+mc)
  print("Больше всего девочек в классе "+dc)


  # почему бы не обернуть предыдущее задание в функцию по подсчет девочек и мальчиков в классе?
  # пусть функция computeMaleFemale возвращает {'female': [{'2a': 2}, {'3c': 0}], 'male':[...]}
  # далее ты бы вызывал только computeMaleFemale(dict)
  # и производил сравнения поверх выходного словаря
  # пожалуйста реализуй с такой декомпозицией 
  # ???

if __name__ == "__main__":
    main()
