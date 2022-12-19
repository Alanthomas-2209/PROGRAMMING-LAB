class Publisher:
    def __init__(self, publisherName):
        self.publisherName = publisherName

    def display(self):
        pass


class Book(Publisher):
    def __init__(self, publisherName, title, author):
        Publisher.__init__(self, publisherName)
        self.title = title
        self.author = author

    def display(self):
        pass


class Python(Book):
    def __init__(self, publisherName, title, author, price, noOfPage):
        Book.__init__(self, publisherName, title, author)
        self.price = price
        self.noOfPage = noOfPage

    def display(self):
        print("Publisher :", self.publisherName)
        print("Title :", self.title)
        print("Author :", self.author)
        print("Price :", self.price)
        print("No. of pages :", self.noOfPage)


obj = Python("Dvir Publishing House Ltd", "Sapiens", "Yuval Noah Harari", 1200, 443)
obj.display()
