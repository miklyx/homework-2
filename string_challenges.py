
# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(len((word.lower()).split('а'))-1)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???

print(sum(word.lower().count(v) for v in 'уеыаоэиюё'))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for i in sentence.split():
    print(i[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???

s=[]
k = 0
for i in sentence.split():
  k += len(i)
print(k/len(sentence.split()))