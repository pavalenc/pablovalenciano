# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:04:16 2022

@author: pavmb
"""

import time
import random
from multiprocessing import Process
def f(value):
 for i in range(3):
     print (f"hola soy {value} vuelta {i}")
     time.sleep(random.random()/3)
def g():
 print ("adios")
if __name__ == "__main__":
 N = 10
 lp = []
 for i in range(N):
     lp.append(Process(target=f,args=(f"ana {i}",)))
 for p in lp:
     p.start()
 q = Process(target=g)
 q.start()
 print ("fin")