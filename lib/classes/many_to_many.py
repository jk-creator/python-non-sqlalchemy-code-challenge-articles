class Article:
    all = []
    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    
    def get_title(self):
        return self._title
    def set_title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 :
            self._title = title
    title = property(get_title, set_title)

    def get_author(self):
        return self._author
    def set_author(self, author):
        if isinstance(author, Author):
            self._author = author
    author = property(get_author, set_author)
    
    @property 
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        
class Author:
    def _init_(self, name = None):
        self.name = name
            
    def get_name(self):
        return self._name
    def set_name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name           
   
    name = property(get_name, set_name)
    def articles(self):
        return [article for article in Article.all if article.author == self]
    def add_articles(self, article):
        if isinstance(article, Article):
            self._articles.append(article)

    def magazines(self):
       return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    def topic_areas(self):
        return list(set({magazine.category for magazine in self.magazines()}))

class Magazine:
    def _init_(self, name, category):
        self.name = name
        self.category = category
        self.add_articles = []
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value       
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value   
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list({article.author for article in self.articles()})
    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles]
        unique_authors = set(authors)
        contributing_authors = [author for author in unique_authors if authors.count(author) > 2]
        return contributing_authors if contributing_authors else None