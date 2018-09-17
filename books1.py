import sys
import csv

def importFile(fileName):
    #takes in file object, reads csv into 2 lists
    #returns list of authors and list of books
    inFile = open(fileName, string)
    return inFile


def readFile(fileName, action):
    authorList = []
    titleList = []
    with open(fileName, newline = '') as bookfile:
        reader = csv.reader(bookfile, delimiter = ',', quotechar = '"')
        if action == "books":
            for row in reader:
                titleList.append(row[0])
            #return list of books
            #add another if for sort-direction
        return titleList
        elif action == "authors":
            for row in reader:
                authorList.append(row[2])
            #return list of authors
            #add another if for sort-direction
        return authorList
        else:
            #return error message?
            pass



def sort(sortDirectionBool, myList):
    #sorts list based on sortDirectionBool


def main():
    fileName = sys.argv[1]
    action = sys.argv[2]
    if sys.argv[].len() == 3:
        sortDirection = sys.argv[3]
        sortDirectionBool = False
        if (sortDirection.lower() == "reverse"):
            sortDirectionBool = True
        #sortDirectionBool = true means reverse. if the bool is false, it means
        #sort forwards
    action = action.lower()
    actionList = readFile(fileName, action)
