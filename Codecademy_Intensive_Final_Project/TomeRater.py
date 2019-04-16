class User(object):
    """User utilizing Tome Rater Application"""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        
    def __repr__(self):
        return "\nUser: {user}, Email: {email}, Books Read: {books}.\n".format(user=self.name, 
                                                                             email=self.email, 
                                                                             books=len(self.books.keys()))
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email    

    def get_email(self):
        """Returns email address of current user"""
        return self.email

    def change_email(self, email):
        """Updates email address of current user"""
        self.email = email
        print("\n{name}'s Email has been successfully updated.\n".format(name=self.name))
        
    
    def read_book(self, book, rating=None):
        """Adds book to users list of read books"""
        return self.books.update({book: rating})
    
    def get_average_rating(self):
        """Gets the average rating for all books rated by user"""
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books.keys())


class Book(object):
    """Book object for Tome Rater Application"""
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
    
    def get_title(self):
        """Returns the title of current book"""
        return self.title
    
    def get_isbn(self):
        """Returns the ISBN of current book"""
        return self.isbn
    
    def set_isbn(self, isbn):
        """Sets the ISBN of current book"""
        self.isbn = isbn
        print("\nThe following ISBN, {isbn}, for {book} has been successfully updated.\n".format(book=self.title, 
                                                                                               isbn=isbn))
    def add_rating(self, rating):
        """Adds the determined rating to the current book"""
        self.ratings = []
        if (0 <= rating) and (rating <= 4):
            self.ratings.append(rating)
        else:
            print("\nInvalid Rating\n")
        
    def get_average_rating(self):
        """Returns average rating for the current book"""
        if len(self.ratings) == 0:
            return None
        else:
            return sum([value for value in self.ratings if value is not None]) / len(self.ratings)
    
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}".format(title=self.title)
    
        
class Fiction(Book):
    """Fiction Book for Tome Rater Application"""
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self, author):
        """Returns author of current Fiction book"""
        return self.author
    
    def __repr__(self):
        return "\n{title} by {author}.\n".format(title=self.title, 
                                                 author=self.author)
    

class NonFiction(Book):
    """Non-Fiction Book for Tome Rater Application"""
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self, subject):
        """Returns subject for the non-fiction book"""
        return self.subject

    def get_level(self, level):
        """Returns level for the non-fiction book"""
        return self.level
    
    def __repr__(self):
        return "\n{title}, a {level} manual on {subject}.\n".format(title=self.title, 
                                                                  level=self.level, 
                                                                  subject=self.subject)
        
class TomeRater(object):
    """TomeRater Application"""
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        """Creates a book with the values specified"""
        new_book = Book(title, isbn)
        print("\n{book} has been successfully created with the following ISBN:\n{isbn}.\n".format(book=title, isbn=isbn))
        return new_book
    
    def create_novel(self, title, author, isbn):
        """Creates a novel with the values specified"""
        new_fiction = Fiction(title, author, isbn)
        print("\n{novel} has been successfully created with the following attributes:\nAuthor: {author}, ISBN: {isbn}.\n".format(novel=title, 
                                                                                                                               author=author,
                                                                                                                               isbn=isbn))
        return new_fiction
    
    def create_non_fiction(self, title, subject, level, isbn):
        """Creats a non-fiction with the values specified"""
        new_non_fiction = NonFiction(title, subject, level, isbn)
        print("\n{book} has been successfully created with the following attributes:\nSubject: {subject}, Level: {level}.\n".format(book=title, 
                                                                                                                                  subject=subject, 
                                                                                                                                  level=level))
        return new_non_fiction
    
    def add_book_to_user(self, book, email, rating=None):
        """Adds specified book to an existing user"""
        if email not in self.users.keys():
            print("\nNo user exists with email {email}!.\n".format(email=email))
        else:
            user = self.users.get(email)
            user.read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)
            self.books.update({book:self.books.get(book, 0) + 1}) 
            print("\n{book} has been successfully added to {user} with email at {email}.\n".format(book=book, 
                                                                                                 email=email, 
                                                                                                 user=user))
                
                
        
    def add_user(self, name, email, user_books=None):
        """Creates and adds new user to TomeRater with values specified"""
        if email in self.users.keys():
            print("\nUser with email {email} already exists!\n".format(email=email))
            return
        new_user = User(name, email)
        self.users.update({email: new_user})
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
        print("\nUser {name} at {email} was successfully added.\n".format(name=name, 
                                                                        email=email))
                
    def print_catalog(self):
        """Prints TomeRater Catalog"""
        for book in self.books.keys():
            print(book)
        
    def print_users(self):
        """Prints TomeRater Users"""
        for user in self.users.keys():
            print(user)
       
    
    def most_read_book(self):
        """Returns the book that has been read the most""" 
        if len(self.books) == 0:
            return None
        else:
            return [book for book, count in self.books.items() if count == max(list(self.books.values()))][0]
    
    def highest_rated_book(self):
        """Returns the book that has been rated the highest"""
        if len(self.books) == 0:
            return None
        else:
            return [book for book in self.books.keys() if book.get_average_rating() == max(book.get_average_rating() for book in self.books.keys())][0]
                
    def most_positive_user(self):
        """Returns the most positive user"""
        return [user.name for user in self.users.values() if user.get_average_rating() == max([user.get_average_rating() for user in self.users.values()])][0]