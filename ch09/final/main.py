import sys
import requests
from src import openlibrarysubjectsearch
from src import openlibrarysubjectbooks
from src import freemoviedatabase

def main():
    subject = ''
    subject_results = {}
    subject_list = []
    num_found_subject = 0

    print("Welcome to the book / movie matcher!")
    print("Please enter a book subject to begin. (e.g. Love, Winter, Fantasy)")

    while num_found_subject == 0:
        subject = input(': ')
        subjects = openlibrarysubjectsearch.OpenLibrarySubjectSearch(subject)
        subject_results = subjects.get()
        subject_list = subject_results['docs']

        num_found_subject = subject_results['numFound']
        if num_found_subject == 0:
            print("Please try again.")
        else:
            print(f'Total results: {num_found_subject} (Can show a maximum of 99)')

    user_subject_selection = None
    current_index_subject = 0
    search_index_subject = 0
    while (type(user_subject_selection) is not int):
        print('Enter number to select choice, enter "n" to see next 10 results, enter "b" to see previous 10 results, or "q" to quit.')
        if current_index_subject + 10 <= num_found_subject:
            search_index_subject = current_index_subject + 10
        else:
            search_index_subject = len(subject_list)

        for i in range(current_index_subject, search_index_subject):
            print(f'{i}: {subject_list[i]['name']}')

        user_subject_selection = input(': ')

        if user_subject_selection == 'q':
            sys.exit()
        elif user_subject_selection == 'n':
            if current_index_subject + 10 >= 100 or current_index_subject + 10 >= num_found_subject:
                print('You are on the last page.')
            else:
                current_index_subject += 10
        elif user_subject_selection == 'b':
            if current_index_subject - 10 < 0:
                print('You are on the first page.')
            else:
                current_index_subject -= 10
        elif user_subject_selection.isdigit() and int(user_subject_selection) < len(subject_list):
            user_subject_selection = int(user_subject_selection)
        else:
            print('Please enter a valid choice.')

    subject_choice = subject_list[user_subject_selection]['name'].lower()
    print('Your choice: ', subject_choice)

    num_found_subject = 0

    books = openlibrarysubjectbooks.OpenLibrarySubjectBooks(subject_choice)
    book_results = books.get()
    num_count_books = book_results['work_count']
    book_list = book_results['works']

    user_book_selection = None
    current_index_book = 0
    search_index_book = 0
    while (type(user_book_selection) is not int):
        print('Enter number to select choice, enter "n" to see next 10 results, enter "b" to see previous 10 results, or "q" to quit.')
        if current_index_book + 10 <= num_found_subject:
            search_index_book = current_index_book + 10
        else:
            search_index_book = len(book_list)

        for i in range(current_index_book, search_index_book):
            title = book_list[i]['title']
            author_data = book_list[i]['authors']
            authors = []
            for author in author_data:
                authors.append(author['name'])
            print(f'{i}: {book_list[i]['title']}')
            print(f'    Author(s):{"".join([f'[{author}] ' for author in authors])}')

        user_book_selection = input(': ').lower()

        if user_book_selection == 'q':
            sys.exit()
        elif user_book_selection == 'n':
            if current_index_book + 10 >= 12 or current_index_book + 10 >= num_count_books:
                print('You are on the last page.')
            else:
                current_index_book += 10
        elif user_book_selection == 'b':
            if current_index_book - 10 < 0:
                print('You are on the first page.')
            else:
                current_index_book -= 10
        elif user_book_selection.isdigit() and int(user_book_selection) <= 11:
            user_book_selection = int(user_book_selection)
        else:
            print('Please enter a valid choice.')

    book_title = book_list[i]['title']
    book_author_data = book_list[i]['authors']
    book_authors = []
    for book_author in book_author_data:
        book_authors.append(book_author['name'])
    book_choice = book_list[user_book_selection]['title']

    print('Your book: ', book_choice)
    print(f'    Author(s):{"".join([f'[{book_author}] ' for book_author in book_authors])}')

    movie_search_user_query = ''
    movie_search_query_selection = ''
    print("Press 1 to search for a movie using your book title as a query.")
    print("Press 2 to search for a movie using your subject as a query.")
    print("Press q to quit.")
    while movie_search_user_query != 'q':
        movie_search_user_query = input(': ').lower()
        if movie_search_user_query == '1':
            movie_search_query_selection = book_title
            break
        elif movie_search_user_query == '2':
            movie_search_query_selection = subject_choice
            break
        elif movie_search_user_query == 'q':
            sys.exit()
        else:
            print("Please enter a valid choice.")

    free_movie_api = freemoviedatabase.FreeMovieDatabaseSearch(movie_search_query_selection)
    movies = free_movie_api.get()
    movies = movies['description']

    if movies:
        if len(movies) < 10:
            for movie in movies:
                movie_title = movie.get('#TITLE')
                movie_year = movie.get('#YEAR')
                imdb_link = movie.get('#IMDB_URL')
                print(f'Title: {movie_title}')
                print(f'    Year Released: {movie_year}')
                print(f'    IMDB Link: {imdb_link}')
        else:
            for i in range(10):
                movie_title = movies[i].get('#TITLE')
                movie_year = movies[i].get('#YEAR')
                imdb_link = movies[i].get('#IMDB_URL')
                print(f'Title: {movie_title}')
                print(f'    Year Released: {movie_year}')
                print(f'    IMDB Link: {imdb_link}')
    else:
        print("No movies found for your search query!")

if __name__ == '__main__':
    main()
