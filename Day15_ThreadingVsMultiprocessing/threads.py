from threading import Thread
import time

def square():
    for i in range(100):
        i*i
        time.sleep(0.1)
        
if __name__ == '__main__':
    threads = []
    num_threads = 11

    #create thread
    for i in range(num_threads):
        t = Thread(target=square)
        threads.append(t)

    #start each thread
    for t in threads:
        t.start()

    #join thread
    for t in threads:
        t.join()

    #end of the thread:
    print("Ended Process")