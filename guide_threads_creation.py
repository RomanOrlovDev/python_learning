from threading import Thread


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
