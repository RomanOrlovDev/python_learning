# context managers allow you to allocate and release resources precisely when you want to.
# the most widely example is the "with" statement


class open_file:
    def __init__(self, file_name, mode):
        self.f_resource = open(file_name, mode)

    def __enter__(self):
        return self.f_resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f_resource.close()


with open_file('some_file.txt', 'r') as f:
    print(f.read())
