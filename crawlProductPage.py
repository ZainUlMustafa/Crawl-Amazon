from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from textblob import TextBlob

def main():
    baseUrl = "https://www.amazon.com.au"
    
    needToReplace = "/product-reviews/"
    for i in range(1, 1000000):
        urlToFetch = baseUrl + "/Xiaomi-Mi-Watch-Lite-Smartwatch/dp/B08Q3DQXH6".replace("/dp/", needToReplace) + "?pageNumber=" + str(i)

        res = requests.get(urlToFetch)

        soup = BeautifulSoup(res.text, 'html.parser')
        content = soup.find_all('span', class_='a-size-base review-text review-text-content')

        if (len(content) == 0):
            break
        #endif

        for title in content:
            print(title.text.strip())
        #endfor
    #endfor

#enddef

if __name__ == "__main__":
    main()
#endif