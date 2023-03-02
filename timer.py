from threading import *  #подключаем библиотеку многопоточности
from time import time, sleep


def my_timer(num, text):  #функция-таймер
    print(f'Запускаем таймер на {num} секунд\n', end='')
    sleep(num) #ждем, пока отработает
    print(f'Таймер на {num} секунд закончил работу\n', end='')
    print(f'Напоминаю: {text}')


while True:
    local_time = float(input('Через сколько минут?\n'))
    text = str(input("О чём вам напомнить?\n"))
    local_time *= 60

    t = Thread(target=my_timer, args=(local_time,text)) #объявляем таймер в новый поток
    t.start() #запускаем объявленный поток
