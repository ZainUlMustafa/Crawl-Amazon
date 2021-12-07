from bs4 import BeautifulSoup
import jsonpickle
import requests
from datetime import datetime, timedelta
from textblob import TextBlob
from productClass import Product


def main():
    baseUrl = "https://www.amazon.com.au"
    mainCategory = "electronics"
    productCategory = "Smartwatches"
    pagesToFetch = 4
    productObjectDataset = []

    print("Processing...")
    ## interate over amazon pages where upper limit is a big number as we donts know how many pages there can be
    for i in range(1, pagesToFetch + 1):
        urlToFetch = baseUrl + "/s?k=" + productCategory + "&i=" + mainCategory
        if (i > 1):
            urlToFetch += "&page=" + str(i)
        #endif

        res = requests.get(urlToFetch)

        soup = BeautifulSoup(res.text, 'html.parser')
        title_cont = soup.find_all('a',
                                   class_='a-link-normal a-text-normal',
                                   href=True)

        print("Fetching: " + urlToFetch)

        # breaking the loop if page not found
        if (len(title_cont) == 0):
            print("Nothing found in: " + str(i))
            break
        #endif

        for title in title_cont:
            productUrl = baseUrl + title.get('href')
            productTitle = title.text
            productObject = Product(productTitle, productUrl)

            productObjectDataset.append(productObject)
        #endfor
    #endfor

    for productObject in productObjectDataset:
        reviews = []
        needToReplace = "/product-reviews/"
        for i in range(1, 1000000):
            urlToFetch = extract_url(productObject).replace(
                "/dp/", needToReplace) + "?pageNumber=" + str(i)
            res = requests.get(urlToFetch)
            soup = BeautifulSoup(res.text, 'html.parser')
            title_cont = soup.find_all(
                'span', class_='a-size-base review-text review-text-content')
            if (len(title_cont) == 0):
                break
            #endif

            for title in title_cont:
                reviews.append(title.text.strip())
            #endfor
        #endfor
        productObject.add_reviews(reviews)
        print(
            extract_url(productObject) +
            ": status completed!, review found :" + str(len(reviews)))
    #endfor

    print(len(productObjectDataset))
    jsonProductObjectDataset = jsonpickle.encode(productObjectDataset)
    output_file = open('filepath.json', 'w')
    output_file.write(jsonProductObjectDataset)
    output_file.close()
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