class Roster(object):
    def __init__(self):
        self.studentCollection = {}
        self.studentCount = 0 #or just ask the dictionary its size

    def addStudent(self, student):




class Student(object):
    def __init__(self, info):
        self.last = info["Last"]
        self.first = info["First"]
        self.id = info["id"]
        self.quiz = info["Quizzes"]
        #self.quizScore = info["QuizScore"]
        self.labs = info["Labs"]
        #self.labScore = info["LabsScore"]
        self.group = info["GroupProject"]
        self.individual = info["IndividualProject"]
        #self.individualProjectScore = info["IndividualProjectScore"]
        self.midterm = info["Midterm"]
        self.final = info["Final"]
        #self.overall = info["Overallscore"]
        self.letterGrade = self.lettergrade(self.overall)

    #check to see if we have all the quizzes/labs/etc and inserts zeros if not
    def checkNumberOfScores(self):
        while (len(self.quiz) != 10):
            self.quiz.append(0)
        while (len(self.labs) != 10):
            self.labs.append(0)
        while (len(self.individual) != 5):
            self.labs.append(0)
        





    # self.quizscore = calculateFinalizedGradePoints(self, self.quiz OR self.labs)
    # calculateFinalizedGradePoints function drops 2 lowest scores
    def calculateFinalizedGradePoints(self, assignment):
        scorelist = sorted(assignment)
        scorelist = scorelist[2:]
        score = sum(scorelist)/8
        return score
    def calculateFinalizedGradePoints(self, assignment):
        scorelist = sorted(assignment)
        scorelist = scorelist[1:]
        score = sum(scorelist)/
        return score
"""

def calcQuizScore(stdict):  #takes the student dictionary as input
    quizList = (sorted(stdict["Quizzes"])) #sorts the list of numbes in ascending order
    quizList = (quizList[2:])       #drops 2 lowest score
    quizSum = sum(quizList)         #finds the sum of the list
    quizScore = quizSum/8           #calculates the weighted score
    return quizScore                #returns the weighted quiz score

def calcLabsScore(stdict):   #takes the student dictionary as input
    labList = (sorted(stdict["Labs"]))    #sorts the list of numbes in ascending order
    labList = (labList[2:])             #drops 2 lowest scores
    labSum = sum(labList)               #finds the sum of the list
    labScore = labSum/8                 #calculates the weighted score
    return labScore                     #returns the weighted labs score

def calcIndividualProjectScore(stdict):     #takes the student dictionary as input
    individualProjectsList = sorted(stdict["IndividualProject"])  #sorts the list of numbes in ascending order
    individualProjectsSum = sum(individualProjectsList[1:])     #drops 1 lowest scores and finds the sum of the scores
    return individualProjectsSum        #returns the sum
"""




    def lettergrade(self, grade): #converts integer grades into lettergrades
        if grade >= 94 and grade <= 100:
            return "A"
        elif grade < 94 and grade >= 90:
            return "A-"
        elif grade < 90 and grade >= 87:
            return "B+"
        elif grade < 87 and grade >= 84:
            return "B"
        elif grade < 84 and grade >= 80:
            return "B-"
        elif grade < 80 and grade >= 77:
            return "C+"
        elif grade < 77 and grade >= 74:
            return "C"
        elif grade < 74 and grade >= 70:
            return "C-"
        elif grade < 70 and grade >= 67:
            return "D+"
        elif grade < 67 and grade >= 64:
            return "D"
        elif grade < 64 and grade >= 60:
            return "D-"
        elif grade < 60:
            return "F"







"""
class student(object):
    def __init__(self, info):
        self.last = info["Last"]
        self.first = info["First"]
        self.id = info["id"]
        self.quiz = info["Quizzes"]
        self.labs = info["Labs"]
        self.group = info["GroupProject"]
        self.individual = info["IndividualProject"]
        self.midterm = info["Midterm"]
        self.final = info["Final"]
        self.overall = info["Overallscore"]
        self.letterGrade = lettergrade(self.overall)
    def getFirst(self):
        return self.first
    def getLast(self):
        return self.last
    def getId(self):
        return self.id
    def getQuiz(self):
        return


    def printInfo():
        print("Name: ", self.last.capitalize(), ", " , self.first.capitalize())  #capitalizes the first letter of the values on those variables
        print("Student ID: ", self.id)
        print("Scores: ", self.group,"% Group Project,", int(self.group/4),"% Individual Projects,\n",int(self.labs),"% Labs,", int(self.quiz), "% Quizzes,", self.midterm,"% Midterm, ", self.final,"% Final"
        print("Course grade: ", int(self.overall),"%, ", self.letterGrade)




    def lettergrade(self, grade): #converts integer grades into lettergrades

        if grade >= 94 and grade <= 100:
            return "A"
        elif grade < 94 and grade >= 90:
            return "A-"
        elif grade < 90 and grade >= 87:
            return "B+"
        elif grade < 87 and grade >= 84:
            return "B"
        elif grade < 84 and grade >= 80:
            return "B-"
        elif grade < 80 and grade >= 77:
            return "C+"
        elif grade < 77 and grade >= 74:
            return "C"
        elif grade < 74 and grade >= 70:
            return "C-"
        elif grade < 70 and grade >= 67:
            return "D+"
        elif grade < 67 and grade >= 64:
            return "D"
        elif grade < 64 and grade >= 60:
            return "D-"
        elif grade < 60:
            return "F"
"""

def calcAverage(database, keyname): #Calculates Averages and takes a database(list) and a name of the key
    runningTotal = 0
    for student in database:      #checks each student in the database(list)
        runningTotal = runningTotal + student[keyname] #adds each value on the keyname to runningTotal
    return (runningTotal/len(database))       #returns the sum divided by the number of student




def printing(student):  #printing function which prints in a certain way
    studentlastname = student["Last"]          #assigned a variable for the key
    studentfirstname = student["First"]        #assigned a vaiable for the key

    print("Name: ", studentlastname.capitalize(), ", " , studentfirstname.capitalize())  #capitalizes the first letter of the values on those variables
    print("Student ID: ", student['id'])
    print("Scores: ", student['GroupProject'],"% Group Project,", int(student["IndividualProjectScore"]/4),"% Individual Projects,\n",int(student["LabsScore"]),"% Labs,", int(student["QuizScore"]), "% Quizzes,", student['Midterm'],"% Midterm, ", student['Final'],"% Final")
    print("Course grade: ", int(student["Overallscore"]),"%, ", student["LetterGrade"])

def filereader(line, string): #this function helps to split the data from the file
        #takes the file as input and the particular name of the item in the file to be splitted
    beginning = line.find(string) #finds the index of the string in the file
    numList = line[beginning:]         #sets a variable to the data after the index
    checkpoint = numList.find(";")      #finds index of ";"
    numList = numList[:checkpoint]      #sets a variable to the data before the checkpoint index
    numList = numList.replace(" ","")   #takes out any blank spaces and replaces with no blanks
    numList = numList[len(string):]     #sets variable to the number list after the index of the length of the string
    return numList          #returns the list of number from the file

def studentDictionaryList(txtfile):
    database = [] #creates a list

    for item in txtfile: #checks each item in file
        item = item.replace("%","")
        stdict = {}  #creates a dictionary

        checkpoint0 = item.find(";") #finds ; and assigns a variable for that point
        name = item[0:checkpoint0]    #fullname between the beginning index and the found index
        checkpoint1 = name.find(",")       #finds index
        firstname = name[0 : checkpoint1]
        lastname = name[checkpoint1 + 2 : checkpoint0]
        stdict["First"] = firstname
        stdict["Last"] = lastname

        remainingitems1 = item[checkpoint0 + 2 :]
        checkpoint2 = remainingitems1.find(";")
        ids = remainingitems1[0 : checkpoint2]
        stdict["id"] = ids

        remainingitems2 = remainingitems1[checkpoint2 : ]

        quiz = filereader(remainingitems2, "Quizzes")   #calls the function and finds and returns the data after the string
        stdict["Quizzes"] = list(eval(quiz))   #lists and also evals the list of numbers

        stdict["QuizScore"] = calcQuizScore(stdict)  # calls function to drop the low two score and give a weighted score

        individualProjects = filereader(remainingitems2, "IndividualProjects")
        stdict["IndividualProject"] = list(eval(individualProjects))

        stdict["IndividualProjectScore"] = calcIndividualProjectScore(stdict)  #calls the function to drop one score

        Labs = filereader(remainingitems2,"Labs")
        stdict["Labs"] = list(eval(Labs))

        stdict["LabsScore"] = calcLabsScore(stdict)   #calls function to drop 2 score and give weighted score

        groupProject = filereader(remainingitems2,"GroupProjects")
        stdict["GroupProject"] = int(groupProject)

        midterm = filereader(remainingitems2,"Midterm")
        stdict["Midterm"] = int(midterm)

        final = filereader(remainingitems2,"Final")
        stdict["Final"] = int(final)

        stdict["Overallscore"] = calcOverallScore(stdict)

        newStudent = student(stdict)

        database.append(stdict)
    return database

def calcQuizScore(stdict):  #takes the student dictionary as input
    quizList = (sorted(stdict["Quizzes"])) #sorts the list of numbes in ascending order
    quizList = (quizList[2:])       #drops 2 lowest score
    quizSum = sum(quizList)         #finds the sum of the list
    quizScore = quizSum/8           #calculates the weighted score
    return quizScore                #returns the weighted quiz score

def calcLabsScore(stdict):   #takes the student dictionary as input
    labList = (sorted(stdict["Labs"]))    #sorts the list of numbes in ascending order
    labList = (labList[2:])             #drops 2 lowest scores
    labSum = sum(labList)               #finds the sum of the list
    labScore = labSum/8                 #calculates the weighted score
    return labScore                     #returns the weighted labs score

def calcIndividualProjectScore(stdict):     #takes the student dictionary as input
    individualProjectsList = sorted(stdict["IndividualProject"])  #sorts the list of numbes in ascending order
    individualProjectsSum = sum(individualProjectsList[1:])     #drops 1 lowest scores and finds the sum of the scores
    return individualProjectsSum        #returns the sum

def calcOverallScore(stdict):  #takes student dictionary as input and calculates the overall score



    overallGrade = stdict["QuizScore"] + stdict["LabsScore"] + stdict["IndividualProjectScore"] +(stdict["Final"]*1.5) + (stdict["Midterm"]*1.5) + stdict["GroupProject"]

    return overallGrade/10 #output the overall score

#####Project # 4

def bin_search(my_list, search,searchoption): #takes list, string and name of the key as input
    middle = len(my_list)//2 #returns a index
    if len(my_list) == 0:
        return None
    elif my_list[middle][searchoption] == search: #checks if the middle of the list has the search
        return my_list[middle]
    elif my_list[middle][searchoption] > search:
        answer = bin_search(my_list[middle+1:], search, searchoption) #calls the function again
        return answer
    elif my_list[middle][searchoption] < search:
        answer = bin_search(my_list[0:middle], search, searchoption) #calls the function again
        return answer


def merge(sorted1,sorted2):  # merges two unsorted list
    merged = []   #creates an empty list
    while (len(sorted1) > 0) and (len(sorted2) > 0):  #this loops run if the length of the list is more than zero
        if sorted1[0]["Last"] < sorted2[0]["Last"]:
            merged.append(sorted1[0])   # adds into the new list
            sorted1.remove(sorted1[0])  # removes from the list

        elif sorted1[0]["Last"] > sorted2[0]["Last"]:
            merged.append(sorted2[0])
            sorted2.remove(sorted2[0])
        else:
            merged.append(sorted1[0])
            #merged.append(sorted2[0])
            sorted1.remove(sorted1[0])
            sorted2.remove(sorted2[0])
    if len(sorted1) > 0:
        return merged + sorted1
    else:
        return merged + sorted2

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        middle = len(my_list)//2
        short1 = my_list[:middle]  #splits the list
        short2 = my_list[middle:]
        sorted1 = merge_sort(short1)  #calls the function again
        sorted2 = merge_sort(short2)
        print("test")
        return merge(sorted1, sorted2)

    #####

# description: This function searches for the specified student by exaustively walking through the database of all students and looking for the search term
# param (searchDict): The database dictionary to be searched
# param (search): The string to search for
# param (searchOption): This specifies if we are searching for a first name or an ID number
# return: the found entry if it exists or None if it does not
def searchFunction(searchlist, search, searchOption):
    if searchOption == 1:       #if search by last name
        for student in searchlist: #checks each item in the list
             if student["Last"] == search:     #checks if the key is equal to the searchvalue
                    return student         #returns the dictionary
    elif searchOption == 2:
        for student in searchlist:
             if student["First"] == search:
                    return student
    elif searchOption == 3:
        for student in searchlist:
            if student["id"] == search:
                return student
    return None  #returns None is student is not found

def sort_list(list_users):  #sorts dictionaries by student's last name
    sort = 'Last'  #assigns a variable to a key
    sorted_users = [(stdict[sort], stdict) for stdict in list_users]
    sorted_users.sort()    #sorts
    new_list = [stdict for (key, stdict) in sorted_users]
    return new_list

def classRange(database, key): #finds the max and min of the list and takes the list and key as input
    scoreList = []  #creates an empty list
    for student in database: #checks each dictionary in the list
         scoreList.append(student[key])  #adds the values from the key to the new list
    return "Highest Score : " + str(max(scoreList)) + "   Lowest Score : " + str(min(scoreList)) #returns the max and min

def classRange2(database, key): #finds the max and min of the list and takes the list and key as input
    scoreList = []  #creates an empty list
    for student in database:  #checks each dictionary in the list
         scoreList.extend(student[key]) #adds the items in the list inside the key to the new list
    return "Highest Score : " + str(max(scoreList)) + "   Lowest Score : " + str(min(scoreList))  #returns the max and min

def addNewStudent():
    with open("filename.txt", "a") as f:   #opens file and appends at the end of the line
        f.write('\n')  #give one line space
        stdict = {}    #creates  a dictionary
        stdict["First"] = input("First name: ").capitalize()
        stdict["Last"] = input("Last name: ").capitalize()

        stdict["id"] = input("Student ID: ")
        stdict["Quizzes"] = eval(input("Enter quizzes and separate by comma ',' for multiple scores:"))
        stdict["QuizScore"] = calcQuizScore(stdict)
        stdict["Labs"] = eval(input("Enter labs score and separate by comma ',' for multiple scores:"))
        stdict["LabsScore"] = calcLabsScore(stdict)
        stdict["IndividualProject"] = eval(input("Enter individual project scores and separate by comma ',' for multiple scores:"))
        stdict["IndividualProjectScore"] = calcIndividualProjectScore(stdict)
        stdict["Midterm"] = eval(input("Enter midterm score:"))
        stdict["Final"] = eval(input("Enter final score: "))
        stdict["GroupProject"] = eval(input("Enter group project score : "))
        stdict["Overallscore"] = calcOverallScore(stdict)
        stdict["Letter Grade"] = lettergrade((stdict["Overallscore"]))
        studentinfo = stdict["First"]+", "+stdict["Last"]+"; "+stdict["id"]+"; "+"Quizzes "+ prepareListForPrinting(stdict, "Quizzes")+\
        "; " +"IndividualProjects "+prepareListForPrinting(stdict, "IndividualProject")+"; " + "Labs " + prepareListForPrinting(stdict, "Labs")\
        + "; " + "GroupProjects " +  str(stdict["GroupProject"])+ "; " + "Midterm " + str(stdict["Midterm"]) + \
        "; " + "Final " + str(stdict["Final"]) + ";"
        f.write(studentinfo)   #writes the student information in the file
        f.close


def prepareListForPrinting(student, key): #this function takes student info and a key and returns the values on the key without space and adds comma
    output = ""  #with no space
    for item in student[key]:
        output = output + str(item) + ","  #adds string then a comma without spaces
    output = output[:-1]   #everything before the last character
    return output


def findIndex(lst, key, value): #finds index of the student to delete
    #inputs is a list, key,
    for i, dic in enumerate(lst):   #hecks each index and dictionary in the list
        if dic[key] == value:
            return i   #returns a index
    return None   #if not found returns None

def menuPrint(): #this function prints the menu of the program
    print("\n") #gives one empty space
    print("Welcome to the class of Python Programming!!")
    print("\n") #gives one empty space
    print("Please make a selection by entering the number of the menu item you want")
    print("1. Search a student by last name")
    print("2. Search a student by first name")
    print("3. Search a student by student ID")
    print("4. Class Averages and Class Range")
    print("5. Sort dictionary by last name")
    print("6. Add a student")
    print("7. Delete a student")
    print("0. Exit")

def printClassAverageClassRange(database):  #prints the class average and class ranges and takes the database as input
    print("Class Averages with highest and lowest scores")
    print("\n")
    print("Midterm - ", int(calcAverage(database, "Midterm")))
    print(classRange(database, "Midterm"))
    print("\n")
    print("Final - ", int(calcAverage(database, "Final")))
    print(classRange(database, "Final"))
    print("\n")
    print("Individual Projects -", int(calcAverage(database, "IndividualProjectScore")))
    print(classRange2(database, "IndividualProject"))
    print("\n")
    print("Labs - ", int(calcAverage(database, "LabsScore")))
    print(classRange2(database, "Labs"))
    print("\n")
    print("Group Project - ", int(calcAverage(database, "GroupProject")))
    print(classRange(database, "GroupProject"))
    print("\n")
    print("Quizzes - ", int(calcAverage(database, "QuizScore")))
    print(classRange2(database, "Quizzes"))


def main():
    requestfile = input("Please input your file: ")
    openfile = open(requestfile,"r")  #opens a file to read
    readlines = openfile.readlines()   #reads each line of the textfile
    database = studentDictionaryList(readlines)  #calls function to keep all the info in file to a list
    menuPrint()    #calls the function to print the menu for the user
    userEntry = input("Please enter the number to make your selection: ")
    print("\n")
    while userEntry != "0":   # the loop will continue to run until the user inputs 0

        if userEntry == "1":
            search = input("Enter last name:").capitalize()    #prompts user to input lastname and inputs in lowercase
            searchResult = bin_search(database, search, "Last")

            if searchResult != None:  #when the search is not equal to not found

                printing(searchResult)#searches the input in the dictionary
                     #uses the printing function to print the student directory if found
            else:
                print("Student with Last name", search.capitalize(), " is not on file!!!!")     #if not found

        elif userEntry == "2":
            search = input("Enter firstname: ").capitalize()
            searchResult = bin_search(database, search, "First")

            if searchResult != None :
                printing(searchResult)
            else:
                print("Student with First name ", search.capitalize(), "is not on file!!")
        elif userEntry == "3":
            search = input("Enter the student ID: ")
            searchResult = bin_search(database, search, "id")
            if searchResult != None :
                printing(searchResult)
            else:
                print("Student with Student ID ", search.capitalize(), "is not on file!!")
        elif userEntry == "4":      ## calculates averages uses class average function and letter grade function.
            printClassAverageClassRange(database)

        elif userEntry == "5":

            sorting = merge_sort(database)

            print(sorting)

        elif userEntry == "6":
            database.append(addNewStudent())   #adds the dictionary to the list

        elif userEntry == "7":

            enterLast = input("Enter last name of the student you want to delete: ").capitalize()
            indexlast = findIndex(database, "Last" , enterLast)

            if indexlast != None or "0":
                database.pop(indexlast)   #deletes the given index in the list

        elif userEntry == "0" :
            print("Good Bye. Have a wonderful day")
                       #Exits if the users enters 0

        else:
            print("INVALID SELECTION!!! Selection only from 0 thru 7")   #prints if user inputs anything, not on the selection

        menuPrint()
        userEntry = input("Please enter the number to make your selection: ")
        print("\n")
    openfile.close    #closes the open file!
main()
