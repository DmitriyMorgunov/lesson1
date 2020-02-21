
# I. Практика. Вывод сообщений
print('Привет программист!')
print(2+2)
print(10/3)


# II. Практика: Числа
v = input('Введите число от 1 до 10: ')
print(int(v) + 10)


# III. Практика: Строки
name = input('Введите ваше имя: ')
print('Привет, ', name, '. Как дела?', sep=' ')


# IV. Практика: Приведение типов
print(float('1'))
# print(int('2.5')) # Здесь будет ошибка, так как нельзя передавать в функцию int строковое представление вещественного числа.
print(bool(1))
print(bool(''))
print(bool(0))


# V. Практика: Переменные
name = 'Дмитрий'
print(name)

user_info = {
    "first_name": 'Дмитрий',
    "last_name": 'Моргунов'
}
print(user_info['first_name'])


# VI. Практика: Списки
# Создайте список из чисел 3, 5, 7, 9 и 10.5
newList = [3, 5, 7, 9, 10.5]
# Выведите содержимое списка на экран
print(newList)
# Добавьте в конец списка строку "Python"
newList.append('Python')
# Выведите длину списка на экран
print(len(newList))
# Выведите на экран начальный элемент списка
print(newList[0])
# Выведите на экран последний элемент списка
print(newList[-1])
# Напечатайте элементы списка со второго по четвертый включительно
print(newList[1:4])
# Удалите из списка строку "Python"
newList.remove('Python')


# VII. Практика: Словари
# Создайте словарь
newDictionaries = {
    "city": "Москва",
    "temperature": "20"
}
# Выведите на экран значение ключа city
print(newDictionaries['city'])
# Уменьшите значение "temperature" на 5
newDictionaries['temperature'] = int(newDictionaries['temperature']) - 5
# Выведите на экран весь словарь
print(newDictionaries)
# Проверьте, есть ли в словаре ключ country
print('country' in newDictionaries)
# Выведите значение по-умолчанию "Россия" для ключа country
newDictionaries.get('country', "Россия")
# Добавьте в словарь элемент date со значением "27.05.2019"
newDictionaries["date"] = "27.05.2019"
# Выведите на экран длину словаря
print(len(newDictionaries))


# VIII. 
# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, приводит их к строке и отдает 
#   объединенными через разделитель delimiter
def get_summ(one, two, delimiter='&'):
    newString = f'{one}{delimiter}{two}'
    print(newString)
    return newString

# Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в переменную и выведите ее значение на экран
newString = get_summ("Learn", "python")
print(newString)

# Сделайте так, чтобы результирующая строка выводилась заглавными буквами
print(newString.upper())

# Создайте функцию format_price, которая принимает один аргумент price
# Приведите price к целому числу (тип int)
# Верните строку "Цена: ЧИСЛО руб."
def format_price(price):
    formatPrice = int(price)
    return f'Цена: {formatPrice} руб.'
# Вызовите функцию, передав на вход 56.24 и положите результат в переменную
formatPrice = format_price(56.24)
# Выведите значение переменной с результатом на экран
print(formatPrice)


"""
Сделайте git init в папке lesson1
Создайте файл .gitignore и добавьте туда строку *.pyc
Добавьте все файлы в коммит (git add .)
Сделайте коммит (git commit -m "First commit")
Создайте репозиторий lesson1 на github.com
Добавьте удаленный репозиторий к локальному lesson1
Сделайте git push -u origin master
"""
