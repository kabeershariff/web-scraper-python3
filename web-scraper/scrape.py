import requests
from bs4 import BeautifulSoup




class Start(object):
    

    def get_page(self, url):
        
        response = requests.get(f'https://www.flipkart.com/search?q={url}')
        response_content = response.content
        soup = BeautifulSoup(response_content, "html.parser")
        response_prices = soup.find_all('div', class_="_30jeq3")

        for i in response_prices:
            price = i.text
            print(price)





