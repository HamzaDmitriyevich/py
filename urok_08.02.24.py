year = input('Введите год рождения')
month = input('введите месяц')
print(month)
print(type(month))
month_of_birth = int(month)
print(year)  # ответ пользователя
print(type(year))   # тип ответа - строка! А надо - число!
year_of_birth = int(year)  # превращаю строку в число
current_year = 2024
current_month = 2
current_day =27
age = current_year * year_of_birth
if month_of_birth > current_month:
    age -= 1

print('Вам', age, 'лет')    





