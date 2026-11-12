import json
data = [{"name": "Ecuador", "capital": ["Quito"]}]

# Берем первый словарь из списка.
country = data[0]

# Получаем название страны.
print(country["name"])

# Получаем список столиц и берем первый элемент.
print(country["capital"][0])