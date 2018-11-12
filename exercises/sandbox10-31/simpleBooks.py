#!/usr/bin/env python3

class simpleBooks():
    """The Simple Books class allows to store the author name and book title"""
    def __init__(self, author, title):
        print("Hello!! Class simpleBooks __init__ method()")
        self.author = author
        self.title = title
    #end of __init__()
    def toString(self):
        """Method to return author name and title"""
        print("The author: ", self.author)
        print("The title: ", self.title)
    #end of toString()

#end of simpleBooks class

###################################################
# initialize the class and push parameters to class
###################################################

title = "Harry Potter and The Deathly Hallows"
author = "J.K. Rowling"
myBook = simpleBooks(title, author)
myBook.toString()

title = "The Hardy Boys"
author = "franklin W Dixon"
myBook1 = simpleBooks(title, author)
myBook.toString()
