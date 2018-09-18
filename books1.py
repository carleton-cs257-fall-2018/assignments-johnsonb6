import sys
import csv

class Author:
    def __init__(self, firstName, lastName, book, publishDate, birthYear, deathYear = 0):
        self.firstName = firstName
        self.lastName = lastName
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

    def getLastName(self):
        return self.lastName

    def __str__(self):
        fullName = self.firstName + " " + self.lastName
        return fullName

    def getFullName(self):
        fullName = self.firstName + " " + self.lastName
        return fullName


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
        for row in reader:
            book = row[0]
            publishDate = row[1]
            authorFirst = ""
            authorLast = ""
            birthYear = ""
            deathYear = ""
            deathDone = False
            birthDone = False
            lastDone = False
            firstDone = False

            i = len(row[2])-1
            while i >= 0:
                if deathDone == False:
                    if row[2][i-1] == "-":
                        deathYear = 0
                        i = i - 1
                    else:
                        deathYear = "" + row[2][i-4] + row[2][i-3] + row[2][i-2] + row[2][i-1]
                        i = i - 5
                    deathDone = True
                if birthDone == False and deathDone == True:
                    birthYear = row[2][i-4] + row[2][i-3] + row[2][i-2] + row[2][i-1]
                    i = i - 7
                    birthDone = True

                if lastDone == False and birthDone == True and deathDone == True:
                    authorLast = authorLast + row[2][i]
                    if row[2][i-1] == " ":
                        i = i - 2
                        lastDone = True

                if firstDone == False and lastDone == True and birthDone == True and deathDone == True:
                    authorFirst = authorFirst + row[2][i]
                i = i - 1

            authorFirst = switcharoo(authorFirst)
            authorLast = switcharoo(authorLast)

            newAuth = Author(authorFirst, authorLast, book, publishDate, birthYear, deathYear)

            titleList.append(book)
            authorList.append(newAuth)

        if action == "books":
            #return list of books
            #add another if for sort-direction
            return titleList
        elif action == "authors":
            #return list of authors
            #add another if for sort-direction
            return authorList
        else:
            #return error message?
            pass

def switcharoo(word):
    correctWord = ""
    for i in range(len(word)-1,-1,-1):
        correctWord = correctWord + word[i]
    return correctWord



def sort(action, myList):
    #sorts list based on sortDirectionBool
    if action == "books":
        myList.sort()
        print(myList)
        myList.sort(reverse = True)
        print(myList)
    if action == "authors":
        authList = sorted(myList, key=lambda Author: Author.lastName)
        for i in authList:
            print(i.getFullName())
        #authList.sort(reverse = True)

        return authList
    return myList
    pass



def main():
    fileName = sys.argv[1]
    print(fileName)
    action = sys.argv[2]
    print(action)
    if len(sys.argv) > 3:
        sortDirection = sys.argv[3]
        sortDirectionBool = False
        if (sortDirection.lower() == "reverse"):
            sortDirectionBool = True
        #sortDirectionBool = true means reverse. if the bool is false, it means
        #sort forwards
    action = action.lower()
    actionList = readFile(fileName, action)
    sortedList = sort(action, actionList)

if __name__ == '__main__':
    main()
