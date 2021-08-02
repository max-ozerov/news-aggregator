import feedparser

"""
url = 'https://finance.yahoo.com/rss/'
"""
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://thehill.com/rss/syndicator/19110'
feed = feedparser.parse(url)


print("The Hill — Most Popular\n")

for entry in feed.entries:

    article_title = entry.title
    content = entry.summary
    print(article_title + ": " + content + "\n")
