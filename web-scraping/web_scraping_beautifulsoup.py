# Python Web Scraping with BeautifulSoup

#import modules
import bs4 as bs
import urllib.request

#open the url and turn it into soup!
url = urllib.request.urlopen\
    ('http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012').read()
soup = bs.BeautifulSoup(url, 'lxml')

# search through the 'div' elements and get the title, genres, runtime and ratings
for div in soup.find_all('div', class_='lister-item-content'):
    title = div.find('a').contents[0]
    genres = div.find('span', class_='genre')
    genres = genres.text.split()
    runtime = div.find('span', class_='runtime').contents[0]
    rating = div.find('strong').contents[0]
    print(title, genres, runtime, rating, )