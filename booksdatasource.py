#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''
import csv

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871


                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6

                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.

        '''
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
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''

        """book = self.books_list[book_id]

        book_title = book[1]
        pub_year = book[2] #not sure which index this is
        return book_title
        """
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



        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            See the BooksDataSource comment for a description of how a book is represented.
        '''


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
            sorted_list = sorted(authors_list_to_return, key = lambda k: k["birth year"])
        else:
            sorted_list = sorted(authors_list_to_return, key = lambda k: k["last name"])
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        return authors_list_to_return


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
    print(data_source.authors(start_year = 1840, end_year = 1850))
