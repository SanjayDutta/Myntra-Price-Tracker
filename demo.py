'''
from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")'''
import threading
import time


def print_work_a():
    print('Starting of thread :', threading.currentThread().name)
    time.sleep(2)
    print('Finishing of thread :', threading.currentThread().name)


def print_work_b():
    print('Starting of thread :', threading.currentThread().name)
    print('Finishing of thread :', threading.currentThread().name)

a = threading.Thread(target=print_work_a, name='Thread-a', daemon=True)
b = threading.Thread(target=print_work_b, name='Thread-b')

a.start()
b.start()