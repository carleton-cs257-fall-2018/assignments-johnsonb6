# tests.py
# Written by Alexis Engel, Brennan Johnson, and Silas Monahan
import booksdatasource
import unittest

class BooksDataSourceTest:

	# Book matches ID number
	def test_book_ID ():
		if book(3) == "Beloved":
			return True
		else:
			return False


	# Author matches ID number
	def test_author_ID ():
		if author(1) == "Connie Willis":
			return True
		else:
			return False

	# Each criteria for books() works (using ID number)
	def test_book_authorID():
		if books(author_id = 1) == ["All Clear", "Blackout", "To Say Nothing of the Dog"]:
			return True
		else:
			print("Author ID criteria insertion for books() does not work")
			return False
	#search_text param works for books()
	def test_book_search_text():

		if books(search_text = the) == ["Love in the Time of Cholera", "Murder on the Orient Express",
		"The Code of the Woosters", "The Satanic Verses", "The Tenant of Wildfell Hall", "To Say Nothing of the Dog",
		"The Life and Opinions of Tristram Shandy, Gentleman"]:
			return True
		else:
			print("Search_text criteria for books() does not function")
			return False


		# test for other criteria besides just author id
	def test_start_year():
		if books(start_year = 2000) == ["All Clear", "Blackout"]:
			return True
		else:
			print("Start_year criteria for books() not functional")
			return False

	def test_end_year():
		if books(end_year = 1820) == ["Emma", "Pride and Prejudice", "Sense and Sensibility"]:
			return True
		else:
			print("end_year criteria for books() not functional")
			return False

	def test_sortby_year():
		if books(author_id = 1, sort_by = "year") == ["To Say Nothing of the Dog", "All Clear", "Blackout"]:
			return True
		else:
			print("books() sort_by = 'year' param not functional")
			return False

	def test_so
	# Each criteria for authors() works (using ID number)

	# Books that have two authors yield two authors (authors_for_book())
	def test_two_authors ():
		if len(authors_for_book(7)) == 2:
			return True
		else:
			print("Multiple authors are not connecting to books with multiple authors")
			return False

	# Author yields right books (books_for_author())
	def test_right_books ():
		if books_for_author(1) == ["All Clear", "Blackout", "To Say Nothing of the Dog"]:
			return True
		else:
			print("does not return the correct books")
			return False


	# All author last names are one word
	def test_one_last_name ():
		last_name = author(18)[0].last_name
		space = False
		for i in last_name:
			if i == " ":
				space = True
				break
		if !space:
			return True
		else:
			print("This author has mulitple last names when it should only have one")
			return False

	# If the number of books is the same as the number of lines in the initial list
	def test_number_of_books():
		if len(database) == books():
			return True
		else:
			print("The data base is not the same length as the number of books. Something is wrong.")
			return False

	# If the input is the right length (has the right amount of information)
	def test_input_length():
		# run during the input stage, test and see how many bits of informantion have been inputted to one book/author
		pass




# check how many authors are alive and if that is correct
