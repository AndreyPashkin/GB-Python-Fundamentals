# 6. Реализовать функцию int_func(),
# принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(word):
    if len(word):  # проверка для удаления влияния лишних пробелов в строке
        return word[0].upper() + word[1::]
    else:
        return ''


# вариант через join
def int_func_multi_1(string):
    string_list = string.split(' ')
    new_string_list = []
    for word in string_list:
        word = int_func(word)
        new_string_list.append(word)
    new_string = ' '.join(new_string_list)
    return new_string


# вариант через конкатенацию строк
def int_func_multi_2(string):
    string_list = string.split(' ')
    new_string = ''
    for word in string_list:
        new_string += int_func(word) + ' '
    new_string = new_string[:-1]  # удаление лишнего пробела в конце строки для сохранения длины начальной строки
    return new_string


text = input('Введите текст: ')

print(int_func_multi_1(text))  # вывод новой строки по способу 1
print(int_func_multi_2(text))  # вывод новой строки по способу 2
