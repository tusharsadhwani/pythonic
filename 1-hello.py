class Hello:
    def __init__(self, message='Hello world!'):
        self._message = message

    @property
    def message(self):
        return self._message

    def main(self):
        print(self.message)


Hello().main()
