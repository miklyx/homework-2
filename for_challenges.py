"""
# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for i in names:
  print(i)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for i in names:
  print(i+' '+str(len(i)))


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for i in names:
    if is_male.get(i) :
        g = "M"
    else:
        g = 'W'
    print(i+ ' ' + g)


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
print("Всего "+str(len(groups))+" группы")
for i in groups:
  print("В группе "+ str(len(i))+ " ученика")


# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша
"""
groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
for i in range(len(groups)):
   print(",".join(groups[i]))
#print(','.join(groups[0]))
#for i in groups:
#    for j in i:
#      print(j, end = ' ')
#    print()

    # ПРО join() УЗНАТЬ