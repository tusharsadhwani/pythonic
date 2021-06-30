import json
import time
import urllib.request


class UserAPI:
    endpoint = 'https://api.randomuser.me?seed=Pythonic'

    def __init__(self) -> None:
        self.request = urllib.request.Request(self.endpoint)
        self.request.add_header('api-key', '123456')

    def get_users(self, count=1):
        self.request.full_url = f'{self.endpoint}&results={count}'

        with urllib.request.urlopen(self.request) as response:
            data = json.load(response)

        return data['results']


################################################################################

def time_it(func):
    """Prints how long it took to run a function, after it runs"""
    def new_func(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()

        duration = after - before
        print(f'-- took {duration:.2f} seconds')
        print()

    return new_func


class CLI:
    def __init__(self) -> None:
        self.api = UserAPI()
        self.user_cache = []

    @time_it
    def print_user_names(self, num_users):
        if len(self.user_cache) >= num_users:
            users = self.user_cache[:num_users]
        else:
            users = self.api.get_users(num_users)
            self.user_cache = users

        for index, user in enumerate(users, start=1):
            print(index, '-', user['name']['first'])


def main():
    cli = CLI()
    while True:
        print('Enter number of users to fetch')
        num = int(input('> '))
        cli.print_user_names(num)


if __name__ == '__main__':
    main()
