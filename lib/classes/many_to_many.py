class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string with 5 to 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        
    
    def get_title(self):
        return self._title
    def set_title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 :
            self._title = title
    title = property(get_title, set_title)

    def get_author(self):
        return self._author
    def set_author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = value
    author = property(get_author, set_author)
    
    @property 
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        
class Author:
    def __init__(self, name):
        self._articles = []
        if type(name) == str and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Author name must be a non-empty string.")


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        return self._name
    def articles(self):
        return [article for article in Article.all if article.author == self]


    def magazines(self):
       return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    def topic_areas(self):
        first_list = [article.magazine for article in Article.all if article.author is self]
        if len(first_list) > 0:
            return list(set([magazine.category for magazine in first_list]))
        else:
            return None

class Magazine:
    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Magazine name must be a non-empty string with a length between 2 and 16 characters.")

        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Magazine category must be a non-empty string.")
        self._articles = []
        
        
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
        # return self._articles
    
    def contributors(self):
        return list({article.author for article in self.articles()})
    def article_titles(self):
        list_o_titles = [article.title for article in Article.all if article.magazine is self]
        if len(list_o_titles) > 0:
            return list_o_titles
        else:
            return None

    def contributing_authors(self):
        all_contributors = [article.author for article in Article.all if article.magazine is self]
        for element in all_contributors:
            if all_contributors.count(element) >= 2:
                return [element for element in all_contributors]
            else: 
                return None

# author_1 = Author("Carry Bradshaw")
# # author_2 = Author("Nathaniel Hawthorne")
# magazine_1 = Magazine("Vogue", "Fashion")
# # Article(author_1, magazine, "How to wear a tutu with style")
# # Article(author_2, magazine, "Dating life in NYC")
# article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
# print((article_1))