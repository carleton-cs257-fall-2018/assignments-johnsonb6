


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
