


import booksdatasource
import unittest

class BookTester(unittest.TestCase):
    def setUp(self):
        self.book_tester = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)

    def tearDown(self):
        pass

    def test_book_ID(self):
        self.assertEqual(self.book_tester.book(3), "Beloved")

    def test_author_ID(self):
        self.assertEqual(self.book_tester.author(1), "Connie Willis")

    def test_book_author_ID(self):
        self.assertEqual(self.book_tester.books(author_id = 1),
        ["All Clear", "Blackout", "To Say Nothing of the Dog"])

    def test_book_search_text(self):
        self.assertEqual(self.book_tester.books(search_text = "the"),
        ["Love in the Time of Cholera", "Murder on the Orient Express",
		"The Code of the Woosters", "The Satanic Verses", "The Tenant of Wildfell Hall", "To Say Nothing of the Dog",
		"The Life and Opinions of Tristram Shandy, Gentleman"])

    def test_start_year(self):
        self.assertEqual(self.book_tester.books(start_year = 2000), ["All Clear", "Blackout"])

    def test_end_year(self):
        self.assertEqual(self.book_tester.books(end_year = 1820), ["Emma", "Pride and Prejudice", "Sense and Sensibility"])

    def test_sortby_year(self):
        self.assertEqual(self.book_tester.books(author_id = 1, sort_by = "year"), ["To Say Nothing of the Dog", "All Clear", "Blackout"])

    def test_author_bookid(self):
        self.assertEqual(self.book_tester.authors(book_id = 3), ["Connie Willis"])

    def test_author_search_text(self):
        self.assertEqual(self.book_tester.authors(search_text = "Wode"), ["Pelham Grenville Wodehouse"])

    def test_author_start_year(self):
        self.assertEqual(self.book_tester.authors(start_year = 2014), ["Gabriel Garcia Marquez", "Terry Pratchett"])

    def test_author_end_year(self):
        self.assertEqual(self.book_tester.authors(end_year = 1812), ["Charles Dickens"])

    def test_sortby_birth_year(self):
        self.assertEqual(self.book_tester.authors(search_text = "p"), ["Pelham Grenville Wodehouse", "Daphne DuMaurier", "Terry Pratchett"])

    def test_right_books(self):
        self.assertEqual(self.book_tester.books_for_author(1), ["All Clear", "Blackout", "To Say Nothing of the Dog"])

    def test_right_authors(self):
        self.assertEqual(self.book_tester.authors_for_book(7), ["Neil Gaiman", "Terry Pratchett"])
