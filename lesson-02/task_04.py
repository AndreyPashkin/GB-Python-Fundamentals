# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input('Введите несколько слов разделённых пробелами: ')

words_list = words.split(' ')
words_amount = len(words_list)
clear_words_list = []

# очистка списка на случай, если пользователь сделал несколько пробелов подряд
for word in words_list:
    if word != '':
        clear_words_list.append(word)

# выводим очищенный список, нумеруя строки
for index, word in enumerate(clear_words_list):
    print(f'{index + 1}: {word[:10:]}')
