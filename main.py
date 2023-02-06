'''
Практическая работа  №1
Написать программу на Python, которая:

* Подсчитывает общее количество символов в файле
* Подсчитывает общее количесто символов без пробелов
* Подсчитывает количество символов без знаков препинания
* Подсчитывает количество слов в файле
* Подсчитывает количество предложений
* Результат подсчета должен быть выведен в консоль

**Вход программы:**
Файл `aristotle.txt`

**Выход программы:**
Информация о количестве символов, слов и предложений
'''
import re

#открытие файла на чтение
f_in = open('aristotle.txt', 'r', encoding="utf-8-sig")

# считываем данные файла в строку
str_in = str(f_in.read())


str_len = len(str_in) # общее количество символов в файле
space_count = str_in.count(' ') # количество символов пробела в файле

# массив знаков препинанния
punctuation_marks = '''.,?!'"-:;()'''
pm_count = 0 # количество символов знаков препинания в файле
for m in punctuation_marks:
    pm_count += str_in.count(m)


word_list = re.split(' |\n|\r|\f|\t', str_in)
word_count = len(word_list)


print(f'Общее колическтво символов в фале: == >\t{str_len}')
print(f'Общее колическтво символов без пробелов: == >\t{str_len - space_count}')
print(f'Количество символов без знаков препинания: == >\t{str_len - pm_count}')
print(f'Количество слов в файле: == >\t{word_count}')

f_in.close()