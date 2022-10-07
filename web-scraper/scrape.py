import requests
from bs4 import BeautifulSoup




class Start(object):
    
    def __init__(self):
        self.get_page()

    def get_page(self):

        url = input("search term : ")
        response = requests.get(f'https://www.flipkart.com/search?q={url}')
        response_content = response.content
        soup = BeautifulSoup(response_content, "html.parser")
        print(soup.prettify())



