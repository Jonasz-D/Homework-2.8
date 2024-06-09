from models import Author, Quote
import connect, json, datetime

def load_data_to_db():
    Author.drop_collection()
    Quote.drop_collection()
    with open('authors.json', 'r', encoding='utf-8') as f:
        authors_data = json.load(f)

    with open('quotes.json', 'r', encoding='utf-8') as f:
        quotes_data = json.load(f)

    for author_data in authors_data:
        author = Author(fullname = author_data['fullname'],
            born_date = datetime.datetime.strptime(author_data['born_date'], '%B %d, %Y'),
            born_location = author_data['born_location'],
            description = author_data['description'])
        author.save()

    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        quote = Quote(
            tags=quote_data['tags'],
            author=author,
            quote=quote_data['quote']
        )
        quote.save()




