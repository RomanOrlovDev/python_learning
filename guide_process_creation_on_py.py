# child process
# system fork
# multiprocessing
import os
import time
from multiprocessing import Process

pid = os.fork()

if pid == 0:
    # this is child process
    while True:
        print("child: ", os.getpid())
        time.sleep(5)
else:
    print("parent: ", os.getpid())
    os.wait()  # wait for the end of child process

# normally multiprocessing reached by the following code:


def f(name):
    print("Hello", name)


p = Process(target=f, args=("Bob",))
p.start()
p.join()