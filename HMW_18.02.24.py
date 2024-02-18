import math



distance = float(input('Дистанция до цели'))
speed_bulet = int(input('Скорось пули'))
w = 10^-5
y = 7.2921
angular_velocity = y * w
width = math.pi / 4
width_of = math.sin(width)
t_bullet = distance/speed_bulet

S = (2 * speed_bulet) * t_bullet * angular_velocity * width_of 
print(S)