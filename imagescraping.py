import requests
from bs4 import BeautifulSoup

url = "https://www.tvguide.com/movies/marvels-the-avengers/cast/2000102154/"

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

images= soup.find_all('img')

for image in images:
    name = image['alt']
    link = image['src']
    with open(name.replace(' ', '_').replace('/','') + '.jpg', 'wb') as f:
        ima = requests.get(link)
        f.write(ima.content)
