import requests
import enum

class OperationType(enum.Enum):
   INITIATE = 0
   SEARCH_BOOK = 1
   SAVE_BOOK = 2
   VIEW_READING_LIST = 3
   
class PrintType(enum.Enum):
   SEARCH_RESULT = 1
   READING_LIST = 2
   

class GoogleBooks():
    savedBookArr =[]
    searchedBookArr =[]
    maxNumberOfList=4
    minNumberOfList=0
    maxCharacterSizeForSearch=100
    searchApiUrl = 'https://www.googleapis.com/books/v1/volumes?q={}'     
    def search(self,keyword):
        self.searchedBookArr.clear()
        result= requests.get(self.searchApiUrl.format(keyword)).json()
        if result.get('items', None) is None:
           print("No result has been found for this keyword")
           self.restartCommand()
        else:
            size = len(result['items'])
            for i in range(self.maxNumberOfList+1 if size >self.maxNumberOfList+1  else size):
                bookInfo = {
                    'number': i,
                    'title' : result['items'][i]['volumeInfo'].get('title', 'Not Available'),
                    'author' : result['items'][i]['volumeInfo'].get('authors', 'Not Available'),
                    'publisher' : result['items'][i]['volumeInfo'].get('publisher', 'Not Available')
                }           
                self.searchedBookArr.append(bookInfo)
        return self.searchedBookArr

    def printBooksToScreen(self, type):  
        if len(self.savedBookArr)==0 and type!=PrintType.SEARCH_RESULT:
                print("You do not have saved book in your reading list”")
                return None
        else:
            ## type 1: print searchedBookArr else print savedBookArr
            print("{:<8} {:<70} {:<30} {:<100}".format('NUMBER','AUTHOR','PUBLISHER', 'TITLE'))
            for item in self.searchedBookArr  if type==PrintType.SEARCH_RESULT  else self.savedBookArr :
                print("{:<8} {:<70} {:<30} {:<100}".format(str(item['number']),str(item['author']),str(item['publisher']),str(item['title'])))
        return True

    def readCommand(self, commandType): 
        command=None
        #3: View reading list 0: Initiate program
        if OperationType(commandType)==OperationType.INITIATE or OperationType(commandType)==OperationType.VIEW_READING_LIST: 
            while True:
                command = input('Enter your command [1:Search Books, 2:Save books to Reading List”, 3:View Reading List”] ? : ')
                if command.isdigit() and int(command)>=self.minNumberOfList and  int(command) <= self.maxNumberOfList :
                    break
        #Search Book
        elif  OperationType(commandType)==OperationType.SEARCH_BOOK:            
                command = input('Enter keyword to search book ? : ')
                return command
        #Save Book
        elif  OperationType(commandType)==OperationType.SAVE_BOOK:  
            if len(self.searchedBookArr)==0:
                print("Firstly,You have to search book to save")
                self.restartCommand()
            else:
                while True:
                    command = input('Enter the book number in the list to save ? : ')
                    if command.isdigit() and int(command)>=self.minNumberOfList and int(command) < len(self.searchedBookArr) :
                        break
        return int(command)

    def saveBook(self, number):
        for item in self.searchedBookArr:
            if item['number']==number:
                if item in self.savedBookArr:
                        print("Book with number "+str(number) +" had been saved previosly")
                else:
                    self.savedBookArr.append(item)
                    print("Book with number "+str(number) +" has been saved")
                break
        return self.savedBookArr

    def selectCommand(self):  
        print("Press 1 to search books")
        print("Press 2 to save books")
        print("Press 3 to list saved books")
        command=self.readCommand(OperationType.INITIATE)
        return command

    def restartCommand(self, command=None):
        command=self.readCommand(0)
        self.commandHandler(command)
       
    def commandHandler(self, command=None):
        if command is None:
            command=self.selectCommand()
        #search books
        if OperationType(command)==OperationType.SEARCH_BOOK:
            keyword= self.readCommand(OperationType.SEARCH_BOOK)
            #check input size before search
            keyword = keyword if len(keyword)<self.maxCharacterSizeForSearch else keyword[0:self.maxCharacterSizeForSearch-1] 
            self.search(keyword)
            self.printBooksToScreen(PrintType.SEARCH_RESULT)
            self.restartCommand(command)
        #save books
        elif OperationType(command)== OperationType.SAVE_BOOK :
            booknumber= self.readCommand(OperationType.SAVE_BOOK)
            self.saveBook(int(booknumber))
            self.restartCommand(command)
        #list saved books
        elif OperationType(command)==OperationType.VIEW_READING_LIST :
            #list to saved books
            self.printBooksToScreen(PrintType.READING_LIST)
            self.restartCommand(command)

if __name__ == '__main__':
    gb=GoogleBooks()
    command=gb.commandHandler()



