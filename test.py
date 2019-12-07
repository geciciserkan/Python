import unittest
from PythonGoogleBookSearchApp import *

class TestSum(unittest.TestCase):
    googleBook=GoogleBooks()
    def testSearch(self):
        self.assertEqual(len(self.googleBook.search("London"))>0 , True, "Search Result should be available for London keyword")
        self.assertEqual(self.googleBook.printBooksToScreen(PrintType.SEARCH_RESULT) is not None , True, "Program should return  search result")
        self.assertEqual(len(self.googleBook.saveBook(1))>0 , True, "Reading list must be avaiable after saving a book to reading list")
        self.assertEqual(self.googleBook.printBooksToScreen(PrintType.READING_LIST) is not None , True, "Program should return reading list")

if __name__ == '__main__':
    unittest.main()