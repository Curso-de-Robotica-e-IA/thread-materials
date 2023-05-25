from threading import Thread
import time

value = 7

def incremento():
    global value
    while True:
        time.sleep(0.1)
        value +=1


def decremento():
    global value
    while True:
        if( value > 7):
            time.sleep(0.1)
            value -=1



thread1 = Thread(target=incremento)
thread2 = Thread(target=decremento)
thread2.start()
thread1.start()

while True:
    time.sleep(0.1)
    print(value)
