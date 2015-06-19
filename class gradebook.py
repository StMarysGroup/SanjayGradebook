# 6/3: finished classes
# 6/4: sql loading and unloading

# for sql parent child tables
# http://stackoverflow.com/questions/11285305/how-to-create-nested-tables-in-sqlite-database-android





'''
plan:

1. allow duplicate names, but not ids
2. class averages
3. ui



'''

import sqlite3


class Roster(object):
    def __init__(self):
        self.studentCollection = {}
        self.studentList = []
        self.studentCount = 0 #or just ask the dictionary its size

    def addStudent(self, student):
        #self.studentCollection.append(student)
        self.studentCollection[student.first] = student
        self.studentCollection[student.last] = student
        self.studentCollection[str(student.id)] = student
        self.studentList.append(student)

    def searchRoster(self, key):
        val = self.studentCollection.get(key, None)
        if val:
            return val
        else:
            print("search with " + key + " was not able to find a student!")


    #remember to check against duplicate last names or otherwise deal with them

    '''def addNewStudent():
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
    '''
    def writeToFile(self):
        print("out here")
        with open("filenametest.txt", "w") as f:
            print ("here")
            for student in self.studentList:
                studentinfo = student.first + ", " + student.last + "; " + str(student.id) + "; " + "Quizzes " + student.prepareListForPrinting("quiz")+\
                "; " +"IndividualProjects "+ student.prepareListForPrinting("individual")+"; " + "Labs " + student.prepareListForPrinting("labs")\
                + "; " + "GroupProjects " +  str(student.group)+ "; " + "Midterm " + str(student.midterm) + \
                "; " + "Final " + str(student.final) + ";" + "\n"
                f.write(studentinfo)
                f.close

    def sortRoster(self):
        self.studentList = sorted(self.studentList, key= lambda student:student.last)
        for student in self.studentList:
            print(student.last)


    def addNewStudent(self):
        with open("filename.txt", "a") as f:   #opens file and appends at the end of the line
            stdict = {}    #creates  a dictionary
            stdict["First"] = input("First name: ").capitalize()
            stdict["Last"] = input("Last name: ").capitalize()
            stdict["id"] = input("Student ID: ")
            # might not need eval

            stdict["Quizzes"] = list(eval(input("Enter quizzes and separate by comma ',' for multiple scores: ") + ","))
            stdict["Labs"] = list(eval(input("Enter labs score and separate by comma ',' for multiple scores:") + ","))
            stdict["IndividualProject"] = list(eval(input("Enter individual project scores and separate by comma ',' for multiple scores:") + ","))
            stdict["Midterm"] = eval(input("Enter midterm score:"))
            stdict["Final"] = eval(input("Enter final score: "))
            stdict["GroupProject"] = eval(input("Enter group project score : "))
            tempStudent = Student(stdict)
            self.addStudent(tempStudent)
            print(tempStudent)

            f.write(tempStudent.printForFileOutput())   #writes the student information in the file
            f.write('\n')  #give one line space
            f.close


            WriteStudentToTable(tempStudent)

    def deleteStudent(self, lastname):
        student = self.searchRoster(lastname)
        con = sqlite3.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM StudentInfo WHERE last= ?''', (student.last,))
            row = cur.fetchone()
            if row:
                # need to delete child tables also!
                # 1. fetch the id that we us
                # 2. delete the row in all four tables
                tempStudentID = row[2]
                cur.execute('''DELETE FROM StudentInfo WHERE id= ?''', (tempStudentID,))
                cur.execute('''DELETE FROM Quizzes WHERE id= ?''', (tempStudentID,))
                cur.execute('''DELETE FROM Labs WHERE id= ?''', (tempStudentID,))
                cur.execute('''DELETE FROM IndividualProject WHERE id= ?''', (tempStudentID,))
            else:
                print("student with last name " + lastname + " not found!")

    def calcClassAverage(self):
        classTotal = 0
        for student in self.studentList:
            classTotal += student.overallScore

        return classTotal/len(self.studentCollection)

    def editStudent(self, lastname):
        student = self.searchRoster(lastname)
        con = sqlite3.connect('test.db')
        with con:
            cur = con.cursor()
            cur.execute('''SELECT * FROM StudentInfo WHERE last= ?''', (student.last,))
            row = cur.fetchone()
            if row:
                # updates
                temp = ""
                temp = input ("Enter " + row[0] + "'s new first name, blank to keep it the same").capitalize()
                if temp:
                    cur.execute('''UPDATE StudentInfo SET first= ? WHERE first= ?''', (temp, student.first))
                    student.first = temp
                temp = ""
                temp = input ("Enter " + row[1] + "'s new last name, blank to keep it the same").capitalize()
                if temp:
                    cur.execute('''UPDATE StudentInfo SET last= ? WHERE last= ?''', (temp, student.last))
                    student.last = temp
                temp = ""
                temp = input ("Enter " + str(row[2]) + "'s new id, blank to keep it the same")

                if temp:
                    cur.execute('''UPDATE StudentInfo SET id= ? WHERE id= ?''', (temp, student.id))
                    student.id = temp

class Student(object):
    def __init__(self, info):
        self.last = info["Last"].capitalize()
        self.first = info["First"].capitalize()
        self.id = info["id"]
        self.quiz = info["Quizzes"]
        self.labs = info["Labs"]
        self.group = info["GroupProject"]
        self.individual = info["IndividualProject"]
        self.midterm = info["Midterm"]
        self.final = info["Final"]
        self.checkNumberOfScores()
        self.labScore = self.calculateFinalizedGradePointsForQuizAndLab(self.labs)
        self.quizScore = self.calculateFinalizedGradePointsForQuizAndLab(self.quiz)
        self.individualProjectScore = self.calculateFinalizedGradePointsForIndividualProjects(self.individual)
        self.overallScore = self.calcOverallScore()
        self.letterGrade = self.lettergrade(self.overallScore)




    def __repr__(self):
        listOfStudentStrings = []
        listOfStudentStrings.append("Name: " + self.last + ", " + self.first + "\n")
        listOfStudentStrings.append("Student ID: " + str(self.id) + "\n")
        listOfStudentStrings.append("Final Grade: " + self.letterGrade)

        return "".join(listOfStudentStrings)

    def prepareListForPrinting(self, key): #this function takes student info and a key and returns the values on the key without space and adds comma
        output = ""  #with no space
        if key == "quiz":
            for item in self.quiz:
                output = output + str(item) + ","  #adds string then a comma without spaces
        elif key == "individual":
            for item in self.individual:
                output = output + str(item) + ","  #adds string then a comma without spaces
        elif key == "labs":
            for item in self.labs:
                output = output + str(item) + ","  #adds string then a comma without spaces
        output = output[:-1]   #everything before the last character
        return output

    def printForFileOutput(self):
        '''studentinfo = stdict["First"]+", "+stdict["Last"]+"; "+stdict["id"]+"; "+"Quizzes "+ prepareListForPrinting(stdict, "Quizzes")+\
        "; " +"IndividualProjects "+prepareListForPrinting(stdict, "IndividualProject")+"; " + "Labs " + prepareListForPrinting(stdict, "Labs")\
        + "; " + "GroupProjects " +  str(stdict["GroupProject"])+ "; " + "Midterm " + str(stdict["Midterm"]) + \
        "; " + "Final " + str(stdict["Final"]) + ";"
        '''
        totalString = []
        totalString.append(self.first + ", " + self.last + "; " + self.id + "; ")
        totalString.append("Quizzes " + self.prepareListForPrinting("quiz") + "; ")
        totalString.append("IndividualProjects " + self.prepareListForPrinting("individual") + "; ")
        totalString.append("Labs " + self.prepareListForPrinting("labs") + "; ")
        totalString.append("GroupProjects " + str(self.group) + "; " + "Midterm " + str(self.midterm) + "; " + "Final " + str(self.final))
        print ("".join(totalString))
        return ("".join(totalString))




    def getSearchByType(self, type):
        if (type == "Last"):
            return self.last
        if (type == "First"):
            return self.first
        if (type == "id"):
            return self.id


    #check to see if we have all the quizzes/labs/etc and inserts zeros if not
    def checkNumberOfScores(self):
        while (len(self.quiz) < 10):
            self.quiz.append(0)
        while (len(self.labs) < 10):
            self.labs.append(0)
        while (len(self.individual) < 5):
            self.individual.append(0)
        '''
        if self.group:
            self.group = 0
        if (self.midterm):
            self.midterm = self.midterm # test, might not be necessary, depending on how python initializes stuff
        else:
            self.midterm = 0
        if (self.final <= 0):
              self.final = 0

        '''

    def calcOverallScore(self):  #takes student dictionary as input and calculates the overall score
        overallGrade = self.quizScore + self.labScore + self.individualProjectScore + (self.final*1.5) + (self.midterm*1.5) + self.group
        return overallGrade/10 #output the overall score


    # self.quizscore = calculateFinalizedGradePoints(self, self.quiz OR self.labs)
    # calculateFinalizedGradePoints function drops 2 lowest scores
    def calculateFinalizedGradePointsForQuizAndLab(self, assignment):
        scorelist = sorted(assignment)
        scorelist = scorelist[2:]
        score = sum(scorelist)/8
        return score
    def calculateFinalizedGradePointsForIndividualProjects(self, assignment):
        scorelist = sorted(assignment)
        scorelist = scorelist[1:]
        return sum(scorelist)

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



def writeTableHeaders():
    # establish connection
    con = sqlite3.connect('test.db')
    #with the connection open
    with con:
        # get the cursor
        cur = con.cursor()
        #check to see if the tables exist
        stmt = "PRAGMA table_info(StudentInfo)"
        cur.execute(stmt)
        result = cur.fetchone()
        #if they do, do nothing
        if result:
            print("table exists")
        #otherwise make em
        else:
            cur.execute('''create table StudentInfo(first Text, last Text, id integer, midterm integer, final integer, groupScore integer)''')


        stmt = "PRAGMA table_info(Quizzes)"
        cur.execute(stmt)
        result = cur.fetchone()
        if result:
            print("table exists")
        else:
            cur.execute('''create table Quizzes(id integer, G1 integer, G2 integer, G3 integer, G4 integer,G5 integer, G6 integer,G7 integer, G8 integer,G9 integer, G10 integer)''')

        stmt = "PRAGMA table_info(Labs)"
        cur.execute(stmt)
        result = cur.fetchone()
        if result:
            print("table exists")
        else:
            cur.execute('''create table Labs(id integer, G1 integer, G2 integer, G3 integer, G4 integer,G5 integer, G6 integer,G7 integer, G8 integer,G9 integer, G10 integer)''')

        stmt = "PRAGMA table_info(IndividualProject)"
        cur.execute(stmt)
        result = cur.fetchone()
        if result:
            print("table exists")
        else:
            cur.execute('''create table IndividualProject(id integer, G1 integer, G2 integer, G3 integer, G4 integer,G5 integer)''')

        con.commit()

def WriteStudentToTable(student):

    con = sqlite3.connect('test.db')

    with con:

        cur = con.cursor()
        cur.execute('''SELECT * from StudentInfo where last= ?''', (student.last,))
        if cur.fetchone():
            print("student with the same last name already seen! skipping!")
        else:
            cur.execute('''Insert into StudentInfo(first, last, id, midterm, final, groupScore) Values(?,?,?,?,?,?)''', (student.first, student.last, student.id, student.midterm, student.final, student.group))
            tempList = []
            tempList.append(student.id)
            for quiz in student.quiz:
                tempList.append(quiz)

            while (len(tempList) < 11):
                tempList.append(0)

            print (len(tempList))

            cur.execute('''insert into Quizzes Values(?,?,?,?,?,?,?,?,?,?,?)''', (tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5], tempList[6], tempList[7], tempList[8], tempList[9], tempList[10]))

            tempList = []
            tempList.append(student.id)
            for lab in student.labs:
                tempList.append(lab)
            while (len(tempList) < 11):
                tempList.append(0)

            cur.execute('''insert into Labs Values(?,?,?,?,?,?,?,?,?,?,?)''', (tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5], tempList[6], tempList[7], tempList[8], tempList[9], tempList[10]))

            tempList = []
            tempList.append(student.id)
            for project in student.individual:
                tempList.append(project)
            while (len(tempList) < 6):
                tempList.append(0)

            cur.execute('''insert into IndividualProject Values(?,?,?,?,?,?)''', (tempList[0], tempList[1], tempList[2], tempList[3], tempList[4], tempList[5]))

            con.commit()

def ReadStudentFromTable():

    classRoster = Roster()
    con = sqlite3.connect('test.db')

    with con:

        cur = con.cursor()

        # required for selecting multiple rows
        cur.execute('SELECT * FROM StudentInfo')
        rows = cur.fetchall()

        for row in rows: #ORDER BY id

            stdict = {}
            stdict["First"] = row[0]
            stdict["Last"] = row[1]
            stdict["id"] = row[2]
            stdict["Midterm"] = row[3]
            stdict["Final"] = row[4]
            stdict["GroupProject"] = row[5]

            # returns only a single quiz row
            for quiz in cur.execute('SELECT * FROM Quizzes where id = ?', (stdict["id"],)):
                tempList = []
                k = 1
                while k < 11:
                    tempList.append(quiz[k])
                    k+=1

            stdict["Quizzes"] = tempList

            for lab in cur.execute('SELECT * FROM Labs where id = ?', (stdict["id"],)):
                tempList = []
                k = 1
                while k < 11:
                    tempList.append(lab[k])
                    k+=1

            stdict["Labs"] = tempList

            for project in cur.execute('SELECT * FROM IndividualProject where id = ?', (stdict["id"],)):
                tempList = []
                k = 1
                while k < 6:
                    tempList.append(project[k])
                    k+=1

            stdict["IndividualProject"] = tempList

            classRoster.addStudent(Student(stdict))

    return classRoster

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
    classRoster = Roster()

    for item in txtfile: #checks each item in file
        item = item.replace("%","")
        stdict = {}  #creates a dictionary

        #pokeman1 = Pokeman("Blasto", 3, 5, 11)


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

        #stdict["QuizScore"] = calcQuizScore(stdict)  # calls function to drop the low two score and give a weighted score

        individualProjects = filereader(remainingitems2, "IndividualProjects")
        stdict["IndividualProject"] = list(eval(individualProjects))

        #stdict["IndividualProjectScore"] = calcIndividualProjectScore(stdict)  #calls the function to drop one score

        Labs = filereader(remainingitems2,"Labs")
        stdict["Labs"] = list(eval(Labs))

        #stdict["LabsScore"] = calcLabsScore(stdict)   #calls function to drop 2 score and give weighted score

        groupProject = filereader(remainingitems2,"GroupProjects")
        stdict["GroupProject"] = int(groupProject)

        midterm = filereader(remainingitems2,"Midterm")
        stdict["Midterm"] = int(midterm)

        final = filereader(remainingitems2,"Final")
        stdict["Final"] = int(final)

        #stdict["Overallscore"] = calcOverallScore(stdict)

        #newStudent = student(stdict)
        #classStudent = Student()
        database.append(stdict)
        classRoster.addStudent(Student(stdict))
        WriteStudentToTable(Student(stdict))
    return classRoster

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

'''
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

'''
def main():
    writeTableHeaders()
    #requestfile = input("Please input your file: ")
    openfile = open("filename.txt","r")  #opens a file to read
    readlines = openfile.readlines()   #reads each line of the textfile

    # database is a roster of students
    database = studentDictionaryList(readlines)  #calls function to keep all the info in file to a list



    database = ReadStudentFromTable()


    userEntry = ""
    print("\n")
    while userEntry != "exit":   # the loop will continue to run until the user inputs 0
        menuPrint()
        userEntry = input("Please enter the number to make your selection: ")
        if userEntry == "1":
            search = input("Enter last name:").capitalize()    #prompts user to input lastname and inputs in lowercase
            #print (search)
            searchResult = database.searchRoster(search)


            if searchResult != None:  #when the search is not equal to not found
                print ("student found")
                print (searchResult)
                #printing(searchResult)#searches the input in the dictionary
                     #uses the printing function to print the student directory if found

        elif userEntry == "2":
            search = input("Enter firstname: ").capitalize()
            searchResult = database.searchRoster(search)

            if searchResult != None :
                #printing(searchResult)
                print (searchResult)
                print("student found!")

        elif userEntry == "3":
            search = input("Enter the student ID: ")
            searchResult = database.searchRoster(search)
            if searchResult != None :
                print("student found!")
                print (searchResult)
                #printing(searchResult)

        elif userEntry == "4":      # calculates averages uses class average function and letter grade function.
            #printClassAverageClassRange(database)
            print ("averages")
            print(database.calcClassAverage())

        elif userEntry == "5":

            print("sorting")
            database.sortRoster()
        elif userEntry == "6":
            print ("sdfsdf")
            database.addNewStudent()

        elif userEntry == "7":

            enterLast = input("Enter last name of the student you want to delete: ").capitalize()
            database.deleteStudent(enterLast)
        elif userEntry == "8":
            print("thing")
            enterLast = input("Update student: What is the last name of the student that you want to change? ").capitalize()
            database.editStudent(enterLast)
        elif userEntry == "0" :
            database.writeToFile()
            print("Good Bye. Have a wonderful day")
            userEntry = "exit"
        else:
            print("INVALID SELECTION!!! Selection only from 0 thru 7")   #prints if user inputs anything, not on the selection



        print("\n")
    openfile.close    #closes the open file!
main()
