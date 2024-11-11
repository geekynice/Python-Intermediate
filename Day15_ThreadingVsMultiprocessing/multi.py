from multiprocessing import Process
import os
import time
def square():
    for i in range(100):
        i*i
        time.sleep(0.1)
        
if __name__ == '__main__':
    processes = []
    cpu_count = os.cpu_count()

    #create process
    for i in range(cpu_count):
        p = Process(target=square)
        processes.append(p)

    #start process
    for p in processes:
        p.start()

    #join process
    for p in processes:
        p.join()

    #end of the process:
    print("Ended Process")