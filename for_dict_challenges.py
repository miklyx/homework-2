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

mlst=[]
dlst=[]
for i in school:
  # print(i.get('class'))
  for j in i.get('students'):
    if is_male.get(j.get('first_name')):
      mlst.append(j.get('first_name'))
    else:
      dlst.append(j.get('first_name'))
  print("В классе "+i.get('class')+" "+str(len(dlst))+" девочки и "+str(len(mlst))+" мальчика")
  mlst = []
  dlst = []
  
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
"""

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
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

mlst=[]
dlst=[]
resl = []
m=0
mc = ""
d=0
md =""
for i in school:
  for j in i.get('students'):
    if is_male.get(j.get('first_name')):
      mlst.append(j.get('first_name'))
    else:
      dlst.append(j.get('first_name'))
  i['M']=len(mlst)
  i['D']=len(dlst)
  resd=dict(classs=i.get('class'),M = i.get('M'),D =i.get('D'))
  resl.append(resd)
  mlst = []
  dlst = []
  resd = dict()
for i in resl:
  if i.get('M') > m:
    m = i.get('M')
    mc = i.get('classs')
  if i.get('D') > d:
    d = i.get('D')
    dc = i.get('classs')
print("Больше всего мальчиков в классе "+mc)
print("Больше всего девочек в классе "+dc)
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
