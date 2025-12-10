import requests

class FreeMovieDatabaseSearch:
    def __init__(self, query):
        self.url = 'https://imdb.iamidiotareyoutoo.com/search'
        self.params = {
            'q': query
        }
        self.content = []

    def get(self):
        try:
            r = requests.get(self.url, params=self.params, timeout=5)
            r.raise_for_status()
            response = r.json()
            self.content = response
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def change_query(self, query):
        self.params = {
            'q': query
        }

    def __string__(self):
        return str(self.content)

def main():
    print('Wrong file.')

if __name__ == '__main__':
    main()
