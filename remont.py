#Задача 3. Вводится ширина, длина и высота комнаты.
#Рулон обоев 10 метров при ширине 0.5
#Сколько рулонов надо купить?


height = input('Высота')
width = input('Ширина')
lenght = input('Длина')

heightRoom = int(height)
widthRoom = int (width)
lenghtRoom= int (lenght)

rulonOb = int(10)
widthOb = bool(0.5)

pl = bool(5.3)

rastshet = (widthRoom * heightRoom * 2) + (lenghtRoom * heightRoom * 2 / pl)

print('количество обоев ', rastshet)




    