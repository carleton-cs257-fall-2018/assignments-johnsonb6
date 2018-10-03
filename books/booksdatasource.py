#!/usr/bin/env python3
#by Brennan Johnson, Silas Monahan, and Alexis Engel
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''
import csv

class BooksDataSource:

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):

        self.books_filename = books_filename
        self.authors_filename = authors_filename
        self.books_authors_link_filename = books_authors_link_filename
        self.books_list = self.read_book_file()
        self.authors_list = self.read_author_file()
        self.books_by_author = self.get_books_by_author()
        self.authors_by_book = self.get_authors_by_book()

    def read_book_file(self):
        book_dict_list = []
        with open(self.books_filename, newline = '') as bookfile:
            reader = csv.reader(bookfile, delimiter = ',')
            for row in reader:
                book_dict = {}
                book_dict["id"] = int(row[0])
                book_dict["title"] = row[1]
                book_dict["publication year"] = int(row[2])
                book_dict_list.append(book_dict)
        return book_dict_list

    def read_author_file(self):
        author_dict_list = []
        with open(self.authors_filename, newline = '') as bookfile:
            reader = csv.reader(bookfile, delimiter = ',')
            for row in reader:
                author_dict = {}
                author_dict["id"] = int(row[0])
                author_dict["last name"] = row[1]
                author_dict["first name"] = row[2]
                author_dict["birth year"] = int(row[3])
                if row[4] == None or row[4] == 'NULL':
                    author_dict["death year"] = None
                else:
                    author_dict["death year"] = int(row[4])
                author_dict_list.append(author_dict)
        return author_dict_list

    def get_books_by_author(self): # list of author dictionaries
        link_dict = {}
        with open(self.books_authors_link_filename, newline = '') as bookfile:
            reader = csv.reader(bookfile, delimiter = ',')
            for row in reader:
                row[1] = int(row[1])
                row[0] = int(row[0])
                val_list = []
                if row[1] in link_dict.keys(): #if row [1] = authorID. is already in list, add
                    link_dict[row[1]].append(row[0])
                else:
                    val_list.append(row[0])
                    link_dict[row[1]] = val_list
        return link_dict

    def get_authors_by_book(self): # list of book dictionaries
        link_dict = {}
        with open(self.books_authors_link_filename, newline = '') as bookfile:
            reader = csv.reader(bookfile, delimiter = ',')
            for row in reader:
                row[1] = int(row[1])
                row[0] = int(row[0])
                val_list = []
                val_list.append(row[1])
                link_dict[row[0]] = val_list
        return link_dict


    def book(self, book_id):

        book_list = self.books_list
        for dictionary in book_list:
            if dictionary["id"] == book_id:
                return dictionary

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        books_to_return = []


        for book in self.books_list:
            #search text check
            if search_text != None:
                if search_text.lower() not in book["title"].lower():
                    continue
            #author id check
            if author_id != None:
                to_continue = False
                for author in self.authors_by_book[book["id"]]:
                    if author_id == author:
                        to_continue = True
                        break
                if to_continue == False:
                    continue
            #start year check
            if start_year != None:
                if start_year > book["publication year"]:
                    continue
            #end year check
            if end_year != None:
                if end_year < book["publication year"]:
                    continue


            books_to_return.append(book)
        if sort_by == "year":
            sorted_list = sorted(books_to_return, key = lambda k: k["publication year"])
        else:
            sorted_list = sorted(books_to_return, key = lambda k: k["title"])


        return sorted_list

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.) '''
        unrefined_author = self.authors_list[author_id]
        author = unrefined_author[2] + " " + unrefined_author[1]
        return author

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        authors_list_to_return = []
        for author in self.authors_list:
            if search_text != None:
                if search_text.lower() not in author["first name"].lower():
                    if search_text.lower() not in author["last name"].lower():
                        continue

            if book_id != None:
                to_continue = False
                for book in self.books_by_author[author["id"]]:
                    if book_id == book:
                        to_continue = True
                        break
                if to_continue == False:
                    continue

            if start_year != None:
                if author["death year"] != None:
                    if author["death year"] < start_year:
                        continue
            #end year check
            if end_year != None:
                if end_year < author["birth year"]:
                    continue

            authors_list_to_return.append(author)

        if sort_by == "birth_year":
            sorted_list = sorted(authors_list_to_return, key = lambda k: k["first name"])
            sorted_list2 = sorted(sorted_list, key = lambda k: k["last name"])
            sorted_list3 = sorted(sorted_list2, key = lambda k: k["birth year"])
            sorted_list = sorted_list3
        else:
            sorted_list = sorted(authors_list_to_return, key = lambda k: k["birth year"])
            sorted_list2 = sorted(sorted_list, key = lambda k: k["first name"])
            sorted_list3 = sorted(sorted_list2, key = lambda k: k["last name"])
            sorted_list = sorted_list3
    
        return sorted_list


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)

    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.books(book_id=book_id)


if __name__ == '__main__':
    data_source = BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')
