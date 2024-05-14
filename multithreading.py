import threading
import time, datetime

def afficher_tik():
    for i in range(4):
        time.sleep(2)
        print('tik')

def afficher_tok():
    for i in range(4):
        time.sleep(2)
        print('tok')

t1 = threading.Thread(target=afficher_tik)
t2 = threading.Thread(target=afficher_tok)

t1.start()
time.sleep(1)
t2.start()
