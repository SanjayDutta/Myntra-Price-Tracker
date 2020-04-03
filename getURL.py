import requests
import json
from bs4 import BeautifulSoup


class DataFetcher():

    def __init__(self, UserUrl):
        self.UserUrl = UserUrl

    def getPrice(self):
        try:
            #page = Page(self.UserUrl)
            src = requests.get(self.UserUrl).content
            soup = BeautifulSoup(src, 'lxml')
            #print(soup)
            PriceClassTag = soup.find_all("script", {"type": "application/ld+json"})
            #print(PriceClassTag)
            self.ProductName = json.loads(PriceClassTag[1].text)['description']
            self.ProductPrice = json.loads(PriceClassTag[1].text)['offers']['price']
            #print(json.loads(PriceClassTag[1].text))'''
            return 1,self.ProductName, self.ProductPrice

        except Exception:
            return 0,"Not Available","0"

'''
obj = DataFetcher("https://www.myntra.com/shirts/highlander/highlander-men-blue--white-slim-fit-checked-casual-shirt/2006852/buy")
ProductName, ProductPrice = obj.getPrice()
print("Product: " + ProductName + "\nPrice: " + ProductPrice)'''
