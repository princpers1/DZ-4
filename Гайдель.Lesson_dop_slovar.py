# Дополнительно по словарям:
# Создайте словарь из строки пользователя следующим образом: в качестве ключей возьмите символы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данного символа в строку.
slov='topliderrrr'
dict = {i: slov.count(i) for i in slov}
print(dict)