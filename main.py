from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from textblob import TextBlob

from productClass import Product

def main():
    baseUrl = "https://www.amazon.com.au"
    productObjectDataset = []

    ## interate over amazon pages
    for i in range(1, 2):
        urlToFetch = baseUrl+ "/s?k=Smartwatches&i=electronics&page=" + str(i)
        res = requests.get(urlToFetch)

        soup = BeautifulSoup(res.text, 'html.parser')
        title_cont = soup.find_all('a', class_='a-link-normal a-text-normal', href=True)
        for title in title_cont:
            productUrl = baseUrl + title.get('href')
            productTitle = title.text
            productObject = Product(productTitle, productUrl)

            productObjectDataset.append(productObject)
        #endfor
    #endfor

    for productObject in productObjectDataset:
        print(extract_title(productObject))
    #endfor
#enddef

def extract_title(productObject):
    return productObject.title
#enddef

def extract_url(productObject):
    return productObject.url
#enddef

def extract_review_list(productObject):
    return productObject.review_list
#enddef

if __name__ == "__main__":
    main()
#endif