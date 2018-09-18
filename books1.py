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
            authorList.append(authorLast + ", " + authorFirst)

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


<<<<<<< HEAD
def sort(sortDirectionBool, myList):
    pass
=======

def sort(myList):
>>>>>>> 09cd522847dc995947634910897a3c6a052305dd
    #sorts list based on sortDirectionBool
    myList.sort()
    print(myList)
    myList.sort(reverse = True)
    print(myList)
    return myList
    pass



def main():
<<<<<<< HEAD
    print("running")
=======
    print("working")
>>>>>>> 09cd522847dc995947634910897a3c6a052305dd
    fileName = sys.argv[1]
    print(fileName)
    action = sys.argv[2]
<<<<<<< HEAD
    print(len(sys.argv))
    if len(sys.argv) == 4:
=======
    print(action)
    if len(sys.argv) > 3:
>>>>>>> 09cd522847dc995947634910897a3c6a052305dd
        sortDirection = sys.argv[3]
        sortDirectionBool = False
        if (sortDirection.lower() == "reverse"):
            sortDirectionBool = True
        #sortDirectionBool = true means reverse. if the bool is false, it means
        #sort forwards
    action = action.lower()
    actionList = readFile(fileName, action)
<<<<<<< HEAD

main()
=======
    sortedList = sort(actionList)

if __name__ == '__main__':
    main()
>>>>>>> 09cd522847dc995947634910897a3c6a052305dd
