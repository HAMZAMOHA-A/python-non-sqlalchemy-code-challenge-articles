class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title  
        self.__class__.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title  

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        self._title = value

class Magazine:
    all = []

    def __init__(self, name, category):
        self.set_name(name)
        self.set_category(category)
        self._articles = []
        self.__class__.all.append(self)

    def set_name(self, name):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string.")
        if not value:
            raise ValueError("Category cannot be empty.")
        self._category = value

    def set_category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = category  

    def articles(self):
        return self._articles

    def contributors(self):
        contributors = {article.author for article in self.articles()}
        return list(contributors)

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        contributing_authors = [author for author in self.contributors() if len([a for a in self.articles() if a.author == author]) > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        top_magazine = max(cls.all, key=lambda mag: len(mag.articles()))
        return top_magazine if len(top_magazine.articles()) > 0 else None

    def add_article(self, author, title):
        """Creates and returns a new article given an author and title."""
        article = Article(author, self, title)
        self._articles.append(article)
        return article

class Author:
    def __init__(self, name):
        self.set_name(name)
        self._articles = []

    def set_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name  

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        """Creates and returns a new article given a magazine and title."""
        article = Article(self, magazine, title)
        return article

    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    def topic_areas(self):
        topics = {article.magazine.category for article in self.articles()}
        return list(topics) if topics else None

     