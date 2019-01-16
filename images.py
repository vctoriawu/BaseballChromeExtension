import urllib
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

my_url = "https://www.gettyimages.ca/photos/major-league-baseball?sort=mostpopular&mediatype=photography&phrase=major%20league%20baseball"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")

container = page_soup.find('section', {"assets editorial simplify-search gi-bricks"})
img = container.find('a')

#counter to index the images correctly
counter = 1
for i in container.findAll('img', src = True):
    #Retrieve image URL
    imgUrl = i.get('src')
    print(imgUrl)

    r = requests.get(imgUrl) # create HTTP response object 
  
    # send a HTTP request to the server and save 
    # the HTTP response in a response object called r 
    with open("baseballimg"+ str(counter) +".png",'wb') as f: 
  
    # Saving received content as a png file in binary format 
    # write the contents of the response (r.content) to a new file in binary mode. 
        f.write(r.content) 

    counter += 1    
