#Задача 2.
#Вводится количество минут до урока
#и расстояние в километрах.
#Какая должна быть средняя скорость,
#чтобы успеть на урок?


minute_urok = input('минут до урока')
rasstoyanie = input('Расстояние km')
minute = int(minute_urok) 
ras = int(rasstoyanie) /1000
speed = ras / minute
print(speed,'km/h')


    


