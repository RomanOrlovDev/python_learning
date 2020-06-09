from queue import Queue
from threading import Thread
import time


def worker(n, m):
    while True:
        item = n.get()
        if item is None:
            break
        print("Processed item: ", item, m)

my_queue = Queue(3)
t1 = Thread(target=worker, args=(my_queue, 1))
t2 = Thread(target=worker, args=(my_queue, 2))
t1.start()
t2.start()

for i in range(10):
    # time.sleep(1)
    my_queue.put(i)

my_queue.put(None)
my_queue.put(None)
t1.join()
t1.join()