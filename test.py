import unittest
from PythonGoogleBookSearchApp import GoogleBooks

class TestSum(unittest.TestCase):
    googleBook=GoogleBooks()
    def testSearch(self):
        self.assertEqual(len(self.googleBook.search("London"))>0 , True, "Search Result should be available for London keyword")
        self.assertEqual(len(self.googleBook.saveBook(1))>0 , True, "Reading list must be avaiable after saving a book to reading list")
        self.assertEqual(self.googleBook.printBooksToScreen(1) is not None , True, "Program should return  search result")
        self.assertEqual(self.googleBook.printBooksToScreen(2) is not None , True, "Program should return reading list")
        self.assertEqual(len(self.googleBook.selectCommand()) is not None , True, "Program should read command from console")
        self.assertEqual(len(self.googleBook.readCommand(0)) is not None , True, "Program should read command from console")

if __name__ == '__main__':
    unittest.main()