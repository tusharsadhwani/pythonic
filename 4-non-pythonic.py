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

class CLI:
    def __init__(self) -> None:
        self.api = UserAPI()
        self.user_cache = []

    def print_user_names(self, num_users):
        timer = time.time()

        if len(self.user_cache) >= num_users:
            users = self.user_cache[:num_users]
        else:
            users = self.api.get_users(num_users)
            self.user_cache = users

        for i in range(len(users)):
            user = users[i]
            print(i+1, '-', user['name']['first'])

        duration = time.time() - timer
        print('-- took %.2f seconds' % duration)
        print()


def main():
    cli = CLI()
    while True:
        print('Enter number of users to fetch')
        num = int(input('> '))
        cli.print_user_names(num)


if __name__ == '__main__':
    main()
