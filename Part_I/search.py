from models import Author, Quote

def search_quotes(query):
    if query.startswith('tags:'):
        tags = query.replace('tags:', '').split(',')
        quotes = Quote.objects(tags__in=tags)
    elif query.startswith('author:'):
        author_name = query.replace('author:', '').strip()
        author = Author.objects(fullname=author_name).first()
        quotes = Quote.objects(author=author)
    else:
        quotes = Quote.objects(quote__icontains=query)

    if bool(quotes) == False:
        print('Brak w bazie danych')
    else:
        for quote in quotes:
            print(f'Author: {quote.author.fullname}')
            print(f'Quote: {quote.quote}')
            print(f'Tags: {quote.tags}')
            print()