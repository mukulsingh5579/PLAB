#The "Smart" Web Scraper (Newspaper3k)
from newspaper import Article

url = 'https://www.nature.com/articles/d41586-024-00123-x' # Example article
article = Article(url)

article.download()
article.parse()
article.nlp() # Performs natural language processing

print(f"Title: {article.title}")
print(f"Summary: {article.summary[:150]}...")
print(f"Keywords: {article.keywords}")