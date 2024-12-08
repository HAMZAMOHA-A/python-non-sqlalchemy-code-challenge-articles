class Article:
    # Class variable to store all Article instances
    all = []

    def __init__(self, author, magazine, title):
        # Initialize the article with an author, magazine, and title
        self.author = author  # This will trigger the setter for 'author'
        self.magazine = magazine  # This will trigger the setter for 'magazine'
        self.title = title  # This will trigger the setter for 'title'
        # Add the newly created article instance to the class-level 'all' list
        type(self).all.append(self)

    @property
    def title(self):
        # Returns the title of the article
        return self._title
    
    @title.setter
    def title(self, title):
        # Validates and sets the title only if it meets the conditions
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title

    @property
    def author(self):
        # Returns the author of the article
        return self._author
    
    @author.setter
    def author(self, author):
        # Validates and sets the author if it is an instance of the Author class
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        # Returns the magazine in which the article was published
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        # Validates and sets the magazine if it is an instance of the Magazine class
        if isinstance(magazine, Magazine):
            self._magazine = magazine


class Author:
    # Class variable to store all Author instances
    all = []

    def __init__(self, name):
        # Initialize the author with a name
        self.name = name  # This will trigger the setter for 'name'
        # Add the newly created author instance to the class-level 'all' list
        type(self).all.append(self)

    @property
    def name(self):
        # Returns the author's name
        return self._name
    
    @name.setter
    def name(self, name):
        # Validates and sets the name only if it is a non-empty string
        if isinstance(name, str) and len(name) >= 1 and not hasattr(self, '_name'):
            self._name = name

    def articles(self):
        # Returns a list of all articles written by this author
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        # Returns a unique list of magazines the author has contributed to
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        # Adds a new article to the author's list of articles for a given magazine and title
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns a list of unique categories of the magazines the author has written for
        if self.articles():
            return list({article.magazine.category for article in self.articles()})
        return None


class Magazine:
    # Class variable to store all Magazine instances
    all = []

    def __init__(self, name, category):
        # Initialize the magazine with a name and category
        self.name = name  # This will trigger the setter for 'name'
        self.category = category  # This will trigger the setter for 'category'
        # Add the newly created magazine instance to the class-level 'all' list
        type(self).all.append(self)

    @property
    def name(self):
        # Returns the magazine's name
        return self._name
    
    @name.setter
    def name(self, name):
        # Validates and sets the name if it is a string between 2 and 16 characters
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        # Returns the magazine's category
        return self._category
    
    @category.setter
    def category(self, category):
        # Validates and sets the category if it is a non-empty string
        if isinstance(category, str) and len(category) >= 1:
            self._category = category

    def articles(self):
        # Returns a list of all articles published by this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Returns a unique list of authors who have contributed to this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Returns a list of all article titles published in the magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Returns a list of authors who have written more than 2 articles for the magazine
        author_count = {}
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        # Filter authors who have contributed 2 or more articles
        return [author for author, count in author_count.items() if count >= 2] or None
