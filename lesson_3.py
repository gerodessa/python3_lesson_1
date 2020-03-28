
# импотрирую для работы со знаками припинания.
import string
# тут лежат регулярные выражения похоже на sql
import re
# для приведения слов к первой форме
import pymorphy2
text = open('texst_lesson_3.txt', 'r', encoding='UTF-8')  # Для винды обязательно писать кодировку иначе ошибка
text_1 = text.read()
'''проверка прочтения текста. '''
print(text_1)

print('1) методами строк очистить текст от знаков препинания;')

text_2 = text_1.translate(str.maketrans('', '', string.punctuation))
print(text_2)
# так эффективнее либо следать не эффективно но самой
text_3 = re.sub(r'[^\w\s]','',text_1)
print(text_2)

print('2 сформировать list со словами (split);')
# для удобства возьму исходный текст и буду формировать по предложениям (точки в виде разделителя)
arr_2 = text_1.split('.')
print(arr_2)

print('3) привести все слова к нижнему регистру (map);')
text_4 = list(map(lambda m: m.lower(), arr_2))
print(text_4)

print(' 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')
# получим снача лист из слов текста,для этого очищенный для знаков текст поделепим по пробелам
arr_3 = text_2.split()

# не знаю для питона слово с большой буквы и маленькой одинаковые или нет, поэтому в нагрузку уменьшу регистр
arr_3 = list(map(lambda m: m.lower(), arr_3))
print(arr_3)
# приведение слов к первой форме
arr_4 = []
morph = pymorphy2.MorphAnalyzer()
for arr_3 in arr_3:
    p = morph.parse(arr_3)[0]
    arr_4.append(p.normal_form)
print('приведение к 1 форме слова')
print(arr_4)

# заполняем словарь таким образом что бы посчитать количество слов в тексте.
dict = {a: arr_4.count(a) for a in arr_4}
print(dict)
# 5 наиболее встречающихся
sort_list = list(dict.items())
sort_list.sort(key=lambda i: i[1], reverse=True)
print('5 наиболее встречающихся')
print(sort_list[:5])
# Количество разных слов в тексте
text_set = set(arr_4)
print('Количество разных слов в тексте')
print(len(text_set))
