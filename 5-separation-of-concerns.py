import json
import time
import urllib.request


class UserAPI:
    endpoint = 'https://api.randomuser.me?seed=Pythonic'

    def __init__(self) -> None:
        self.request = urllib.request.Request(self.endpoint)
        self.request.add_header('api-key', '123456')

    def get_users(self, count=1):
        self.request.full_url = self.endpoint + '&results=%d' % count
        response = urllib.request.urlopen(self.request)
        data = json.load(response)
        response.close()
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

    def fetch_users(self, count):
        if len(self.user_cache) >= count:
            users = self.user_cache[:count]
        else:
            users = self.api.get_users(count)
            self.user_cache = users
        return users

    @time_it
    def print_user_names(self, num_users):
        users = self.fetch_users(num_users)

        for i in range(len(users)):
            user = users[i]
            print(i+1, '-', user['name']['first'])


def main():
    cli = CLI()
    while True:
        print('Enter number of users to fetch')
        num = int(input('> '))
        cli.print_user_names(num)


if __name__ == '__main__':
    main()
