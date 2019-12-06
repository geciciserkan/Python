import requests


class GoogleBooks():

    savedBookArr =[]
    searchedBookArr =[]
    searchApiUrl = 'https://www.googleapis.com/books/v1/volumes?q={}'     

    def search(self,keyword):
        self.searchedBookArr.clear()
        result= requests.get(self.searchApiUrl.format(keyword)).json()
        if result.get('items', None) is None:
           print("No result has been found for this keyword")
           self.restartCommand()
        else:
            size = len(result['items'])
            for i in range(5 if size >5  else size):
                bookInfo = {
                    'number': i,
                    'title' : result['items'][i]['volumeInfo'].get('title', 'Not Available'),
                    'author' : result['items'][i]['volumeInfo'].get('authors', 'Not Available'),
                    'publisher' : result['items'][i]['volumeInfo'].get('publisher', 'Not Available')
                }           
                self.searchedBookArr.append(bookInfo)

    def printBooksToScreen(self, type):  
        if len(self.savedBookArr)==0 and type!=1:
                print("You do not have saved book in your reading list”")
        else:
            ## type 1: print searchedBookArr else print savedBookArr
            print("{:<8} {:<70} {:<30} {:<100}".format('NUMBER','AUTHOR','PUBLISHER', 'TITLE'))
            for item in self.searchedBookArr  if type==1  else self.savedBookArr :
                print("{:<8} {:<70} {:<30} {:<100}".format(str(item['number']),str(item['author']),str(item['publisher']),str(item['title'])))

    def readCommand(self, commandType): 
        command=None
        #3: View reading list 0: Initiate program
        if commandType==0 or commandType==3: 
            while True:
                command = input('Enter your command [1:Search Books, 2:Save books to Reading List”, 3:View Reading List”] ? : ')
                if command.isdigit() and int(command)>0 and  int(command) <4 :
                    break
        #Search Book
        elif commandType==1:            
                command = input('Enter keyword to search book ? : ')
                return command
        #Save Book
        elif commandType==2:  
            if len(self.searchedBookArr)==0:
                print("Firstly,You have to search book to save")
                self.restartCommand()
            else:
                while True:
                    command = input('Enter the book number in the list to save ? : ')
                    if command.isdigit() and int(command)>=0 and int(command) < len(self.searchedBookArr) :
                        break
        return command


    def saveBook(self, number):
        for item in self.searchedBookArr:
            if item['number']==number:
                if item in self.savedBookArr:
                        print("Book with number "+str(number) +" had been saved previosly")
                else:
                    self.savedBookArr.append(item)
                    print("Book with number "+str(number) +" has been saved")
                break

    def selectCommand(self):  
        print("Press 1 to search books")
        print("Press 2 to save books")
        print("Press 3 to list saved books")
        command=self.readCommand(0)
        return command

    def restartCommand(self, command=None):
        command=self.readCommand(0)
        self.commandHandler(command)
       
    def commandHandler(self, command=None):
        if command is None:
            command=self.selectCommand()

        #search books
        if command=="1":
            keyword= self.readCommand(1)
            #check input size before search
            keyword = keyword if len(keyword)<100 else keyword[0:99] 
            self.search(keyword)
            self.printBooksToScreen(1)
            self.restartCommand(command)
        #save books
        elif command=="2":
            booknumber= self.readCommand(2)
            self.saveBook(int(booknumber))
            self.restartCommand(command)
        #list saved books
        elif command=="3":
            #list to saved books
            self.printBooksToScreen(2)
            self.restartCommand(command)


#Main Program
gb=GoogleBooks()
command=gb.commandHandler()


