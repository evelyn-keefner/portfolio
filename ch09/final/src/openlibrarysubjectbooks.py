import requests

class OpenLibrarySubjectBooks:
    def __init__(self, query):
        self.url = 'https://openlibrary.org/subjects/' # {subject}.json
        self.query = query
        self.content = []

    def get(self):
        try:
            r = requests.get(f'{self.url}{self.query}.json', timeout=5)
            print(f'url: {self.url}{self.query}.json')
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
