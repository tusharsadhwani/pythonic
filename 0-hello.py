class Hello:
    def __init__(self):
        self._message = 'Hello world!'

    def get_message(self):
        return self._message

    def main(self):
        message = self.get_message()
        print(message)


Hello().main()
