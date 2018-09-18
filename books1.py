import sys
import csv

class Author:
    def __init__(self, name, book, publishDate, birthYear, deathYear = 0):
        self.name = name
        self.book = [book]
        self.publishDate = publishDate
        self.birthYear = birthYear
        self.deathYear = deathYear
        self.age = 0

    def getAge(self):
        if deathYear == 0:
            age = 2018 - birthYear
            return age
        age = deathYear - birthYear
        return age

def importFile(fileName):
    #takes in file object, reads csv into 2 lists
    #returns list of authors and list of books
    inFile = open(fileName, string)
    print("import file")
    return inFile


def readFile(fileName, action):
    print("read file")
    authorList = []
    titleList = []
    with open(fileName, newline = '') as bookfile:
        reader = csv.reader(bookfile, delimiter = ',', quotechar = '"')
        if action == "books":
            for row in reader:
                titleList.append(row[0])
                print(row[0])
            #return list of books
            #add another if for sort-direction
            print(titleList)
            return titleList
        elif action == "authors":
            for row in reader:
                authorList.append(row[2])
            #return list of authors
            #add another if for sort-direction
            print(authorList)
            return authorList
        else:
            #return error message?
            pass



def sort(sortDirectionBool, myList):
    #sorts list based on sortDirectionBool
    myList.sort()
    return myList
    pass


def main():
    print("start")
    fileName = sys.argv[1]
    print(fileName)
    action = sys.argv[2]
    print(action)
    if sys.argv.len() == 3:
        sortDirection = sys.argv[3]
        sortDirectionBool = False
        if (sortDirection.lower() == "reverse"):
            sortDirectionBool = True
        #sortDirectionBool = true means reverse. if the bool is false, it means
        #sort forwards
    action = action.lower()
    actionList = readFile(fileName, action)
