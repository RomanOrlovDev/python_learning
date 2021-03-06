class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''
