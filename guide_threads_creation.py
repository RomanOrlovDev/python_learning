from threading import Thread
from concurrent.futures import ThreadPoolExecutor, as_completed


def f(name):
    print("Hello", name)


t = Thread(target=f, args=["Bob"])
t.start()
t.join()

# also classes are available for using

class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print("Hello", self.name)


mt = PrintThread("Ben")

mt.start()
mt.join()

# new technology is introduced in Python 3 - ThreadPoolExecutor
def f(a):
    return a * a


with ThreadPoolExecutor(max_workers=3) as pool:
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
