from abc import ABC, abstractmethod


class Publication(ABC):  # Inherit from ABC to make it an abstract base class
    def __init__(self, title, price):
        self.title = title
        self.price = price

    @abstractmethod
    def get_description(self):  # Define an abstract method
        pass


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
    
        self.period = period
        self.publisher = publisher

    def parent_method(self):
        print('this is the parent method')

    def get_description(self):  # Implement the abstract method
        return f"{self.title} ({self.period} - {self.publisher})"

class Book(Publication): 

    ''' this is a book class'''
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

    def get_description(self):  # Implement the abstract method
        return f"{self.title} by {self.author}"
    

    def __str__(self):
        return "this is a book call"


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price,period, publisher)

    def child_method(self):
        print('this is the child method')
    
    def get_description(self):  # Implement the abstract method
        return f"{self.title} {self.period} - {self.publisher}"

    # def parent_method(self):
    #     # print('this is NOT the parent method')
    #     # super().parent_method()


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price,period, publisher)

def get_description(self):  # Implement the abstract method
    return f"{self.title} ({self.period} - {self.publisher})"


b1 = Book("One fish two fish", "Dr Seuse", 24, 29.0)
n1 = Newspaper("The West", "Seven West Media", 2.5, "Daily")
m1 = Magazine("Wired", "Condé Nast", 14.4, "Monthly")

# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)


# Magazine is the Child, Peridocal is the Parent
# m1.parent_method()


# acces the get description method
print(m1.get_description())
