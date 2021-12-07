class Product:
    def __init__(self, title, url, review_list = []):
        self.title = title
        self.url = url
        self.review_list = review_list
    #enddef

    def add_reviews(self, review_list):
        self.review_list = review_list
    #enddef
#endclass