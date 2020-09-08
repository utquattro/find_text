import codecs
import re

# Открываем txt документы.
file1 = codecs.open('word.txt', 'r', 'utf-8')
file2 = codecs.open('text.txt', 'r', 'utf-8')
file3 = open('result.txt', 'w')

text = file2.read() # Текст для поиска слова.
word = file1.read() # Слово которое ищем.

match = re.findall(word,text) # Найденные совпадения.
frequency = str(len(match)) # Перевод list в string. Считаем частоту встречаемости слова.
file3.write(frequency) # Запись в документ result.txt частоту встречаемости слова.

# Закрываем  txt документы.
file1.close() 
file2.close()
file3.close()
