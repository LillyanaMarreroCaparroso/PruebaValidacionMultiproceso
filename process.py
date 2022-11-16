# -*- coding: utf-8 -*-

from datetime import datetime
from multiprocessing import Process
import os
from time import sleep 

def newProcess():
    pidProcess = os.getpid()
    date = datetime.now()
    time = date.time().strftime("%H:%M:%S")

    print('Iniciando el proceso: {} a las {}' .format(pidProcess, time))
    sleep(3)
    print('Terminado el proceso: {}' .format(pidProcess))
    

if __name__ == "__main__":
    processes = [] #lista para guardar los procesos

    for p in range(10): #10 procesos
        process = Process(target=newProcess) #asignamos la funcion a ejecutar
        processes.append(process)
    
    for p in processes:
        p.start()
        p.join()
        sleep(10)

        
    
        
   
