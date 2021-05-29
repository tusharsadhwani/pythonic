class Hello:
    def __init__(self, msg='Hello world!'):
        self._message = msg

    @property
    def message(self):
        return self._message

    def main(self):
        print(self.message)


Hello().main()
