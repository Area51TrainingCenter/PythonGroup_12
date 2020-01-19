import os
import time
import threading
import multiprocessing

NUM_WORKERS = 4

def only_sleep():
    print("Proceso: %s, Nombre del Proceso: %s, Nombre del Hilo %s" %(os.getpid(), multiprocessing.current_process(), threading.current_thread().name))


def crunch_number():
    print("Proceso: %s, Nombre del Proceso: %s, Nombre del Hilo %s"% (os.getpid(), multiprocessing.current_process(),threading.current_thread().name))
    x = 0
    while x < 10000000:
        x += 1

start_time = time.time()
for _ in range(NUM_WORKERS):
    only_sleep()
end_time = time.time()

print("Tiempo en serie", end_time-start_time)

start_time = time.time()
threads = [threading.Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_time = time.time()
print("Tiempo de Hilo", end_time-start_time)

# start_time = time.time()
processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()
print("Tiempo de Hilo", end_time-start_time)
