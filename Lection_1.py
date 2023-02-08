# Найти самый часто встречающийся символ в строке (Кодировка: UTF-8)
s = input()
print(s)
print(max(map(lambda x: (s.replace(' ', '').count(x), x), s)))