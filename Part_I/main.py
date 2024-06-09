from seeds import load_data_to_db
from search import search_quotes


if __name__ == '__main__':
    load_data_to_db()

    while True:
        query = input("Wpisz zapytanie (np. 'tags:change' lub 'author:Albert Einstein'): ")
        if query == 'exit':
            print('Zakończono program')
            break
        else:
            search_quotes(query)