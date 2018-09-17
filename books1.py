import sys
import csv

def importFile(fileName):
    #takes in file object, reads csv into 2 lists
    #returns list of authors and list of books
    inFile = open(fileName, string)
    return inFile
        

def readFile(fileName):
    authorList = []
    titleList = []
    with open(fileName, newline = '') as bookfile:
        reader = csv.reader(bookfile, delimiter = ',', quotechar = '"')
        for row in reader:
            titleList.append(row[0])
            authorList.append(row[2])
    return authorList, titleList


def sort(sortDirection, myList):
    #sorts list based on sortDirection


def main():
    filename = sys.argv[0]
    action = sys.argv[1]
    if sys.argv[].len() == 3:
        sortDirection = sys.argv[2]
    action = action.lower()
    if action == "books":
        #return list of books
        #add another if for sort-direction
    elif action == "authors":
        #return list of authors
        #add another if for sort-direction
    else:
        #return error message?
