import logging
import ephem
from ephem import *
from datetime import *
import locale
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import csv
from collections import OrderedDict

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}
"""
Реализуйте в боте команду, которая отвечает на вопрос “Когда ближайшее полнолуние?” 
Например /next_full_moon 2019-01-01. 
Чтобы узнать, когда ближайшее полнолуние, используйте ephem.next_full_moon(ДАТА)
"""
def next_full_moon_from_today(bot,update):
  locale.setlocale(locale.LC_ALL, "russian")
  c = str(next_full_moon(date.today())).split()[0].split('/')
  c = datetime(int(c[0]),int(c[1]),int(c[2]))
  update.message.reply_text("Ближайшее полнолуние будет в "+c.strftime('%A %d %B %Y'))
"""
Реализуйте в боте команду /wordcount которая считает слова в присланной фразе. 
Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова. Не забудьте:
Добавить проверки на пустую строку
Как можно обмануть бота, какие еще проверки нужны?
"""

def wordcount(bot,update):
    txt = update.message.text
    l = len(txt.split()) - 1
    if not l:
      s = "Введена пустота"  
    elif  l == 1:
      s = " слово"
    elif l < 5:
      s = " слова"
    else:
      s = " слов"
    if l: 
      k = str(l)+s 
    else:
      k = s
    update.message.reply_text(k)

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def planet_talk(bot, update):
    # Вот здесь что-то
    
    pl = update.message.text.split()
    planet = pl[1]
    #
    
    time = date.today()
    if planet == 'Venus':
      stars=constellation(Venus(time))
    if planet == 'Mars':
      stars=constellation(Mars(time))
    if planet == 'Jupiter':
      stars=constellation(Jupiter(time))
    if planet == 'Saturn':
      stars=constellation(Saturn(time))
    if planet == 'Uranus':
      stars=constellation(Uranus(time))
    if planet == 'Neptune':
      stars=constellation(Neptune(time))
    if planet == 'Pluto':
      stars=constellation(Pluto(time))
    if planet == 'Sun':
      stars=constellation(Sun(time))
    if planet == 'Moon':
      stars=constellation(Moon(time))
    if planet == 'Mercury':
      stars=constellation(Mercury(time))
    
    update.message.reply_text(stars[1])

def towns_csv():
  lt = []
  with open('towns.csv', 'r', encoding='Windows-1251') as f:
    fields = ['town']
    reader = csv.reader(f, fields, delimiter=',')
    for i in reader:
      lt.append(i[0])
    return lt

def town_find(town,country):
    letter = ''
    for i in country:
      if i == town:
        if i.upper()[-1] not in ['Ь','Ъ','Ы']:
          letter = i.upper()[-1]
          country.remove(i)
        else:
          letter = i.upper()[-2]
          country.remove(i)  
    if not letter:  
        letter = "Нет такого города"
    return letter,country

def town_give(letter,country):
  town = ''
  for j in iter(country):
        if letter == j[0]:
          town = j
          country.remove(j)
          break
  return town, country

def input_word(bot,update):
  input_command = update.message.text.split()
  if len(input_command)  ==2 :
      word = input_command[1]
  else:
      word = input_command  
  #word = input("Город ")  #####################
  yield word
  
def towns_play(bot,update):
  lst = towns_csv()
  instr = ""
  tlst = lst[:]
  input_command = update.message.text.split()
  if len(input_command)  ==2 :
    instr = input_command[1]
  else:
    instr = input_command 
  while tlst and instr !="exit":                          
    print("update",update)                                #  - это гоняется по бесконечному кругу 
                                                          #  - 
    #instr = input_word(bot,update)                          - это обработка пользовательского текста (без параметра не работает)
    input_command = update.message.text.split()           #  - это я ее отдельно вынес чтоб лишний раз параметр не передавать
    if len(input_command)  ==2 :                          #  - очень хочется тормознуть цикл пока не будет введено значение, не совсем понятно как это сделать, если выйти из него, то снова зайти можно только вызовом команды /cities, которая обнуляет предыдущие результаты игры
      instr = input_command[1]
    else:
      instr = input_command 
    
    #print(instr)
    f_letter = town_find(instr,tlst)[0]                                  
    # print(town_give(f_letter,tlst)[0])
    if f_letter not in ["","Нет такого города"]:
      update.message.reply_text(town_give(f_letter,tlst)[0])
      # print("обычный ответ")
    elif f_letter=="":
      update.message.reply_text("Закончились города")
      print("ответ что города кончились")
    else:
      update.message.reply_text("Нет такого города")
    #  print("ответ что нет города") 
    instr = ""
    # break                                                 -  просто попробовал
  else:

    if instr == "exit":
      update.message.reply_text("Закончили")
    else: 
      update.message.reply_text("Города кончились")

def ar_eval(bot,update):
  """
  Научите бота выполнять основные арифметические действия с двумя числами: сложение, вычитание, умножение и деление. 
  Если боту дать команду /calc 2-3, он должен ответить “-1”.

Не забудьте обработать возможные ошибки во вводе: пробелы, отсутствие чисел, деление на ноль
Подумайте, как можно сделать поддержку действий с тремя и более числами
  """
  input_command = update.message.text.split()
  instr = input_command[1]
  res = eval(instr)
  update.message.reply_text(res)

# далее я попробовал напиисать собственный распил произвольной строки, однако столкнулся с трудностью при обработке подряд идущих однородных операторов
# строка для примера 2-1*3+4/2*3

  """  
  instr_al = instr.replace('+','!')    # заменяю все плюсы и минусы восклицательными знаками чтобы по ним разделить
  instr_al = instr_al.replace('-','!')    #  оно же
  print("off add and less",instr_al)
  mult = []                                # объявляю пустые списки
  rmult = []
  div = []
  rdiv = []
  instr_resmult=[]
  sp1 = instr_al.split('!')                 # делю на выражения умножения и деления чтобы вычислить их прежде
  z =''
  #print("sp1 = ",sp1)                                    
  for i in sp1:                            
    print("sp1 = ",sp1)
    print("i=",i)
    print("i index= ",sp1.index(i))               
    k = i.split('/')
    print("k =",k)
    for j in k:                               #разделяю то, что надо поделить между собой
      tmp = ''                             
      z = i
      if j.partition('*')[1]:                    # проверяю, есть ли в списке выражения умножения чтоб их вычислить
        
        print("j.partition('*')=",j.partition('*'))                          
        rmult.append(int(j.partition('*')[0])*int(j.partition('*')[2]))                 #записываю результаты умножения (потом понял что не за чем)
        mult.append(sp1.index(i))                                                     # записываю индекс члена списка с умножением
        print("k index = ",k.index(j))
        tmp=int(j.partition('*')[0])*int(j.partition('*')[2])                            # вычисляю 
        k[k.index(j)]=tmp                                                             # заменяю выражение результатом в списке
        print("tmp",tmp)
        print("j=",j)
        #print("mult=",mult)
        #print("rmult=",rmult)
        print("new k=",k)
        print("2k index = ",k.index(tmp))
      sp1[sp1.index(i)]=k                                                              # заменяю в списке более высокого уровня
      print("new sp1=",sp1)
      print("---------------")
    print("===============================")                                          
      
   # y = sp1.split('*')                                            # тут я начинал то же самое относительно умножения чтобы записать результвт деления - потом отказался (закомментарено)
    #for t in y:
      #if t.partition('/')[1]:
       # print(t.partition('/'))
    #    rdiv.append(int(t.partition('/')[0])/int(t.partition('/')[2]))
     #   div.append(sp1.index(i))
     #   print(div)
     #   print(rdiv)
   
   далее по идее нужно было бы схлопнуть суммы и разности, но не нашел времени побороть вычисление выражений типа 4/2*3
  
"""


def main():
    mybot = Updater("1007684944:AAHyQ5_tF2_qer8lWGyWytHILaAOf5uYT_8", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_talk))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon_from_today))
    dp.add_handler(CommandHandler("calc", ar_eval))
    dp.add_handler(CommandHandler("cities", towns_play))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
