#! /usr/bin/env python3
# Alejo Pijuan  
# 11/10/16
# This program takes a list of names and creates usernames from that list.

def readDataFile(filename):
    # takes a filename as a parameter and reads that file (student names)
    # into a list or a dictionary

    a = open(filename, "r")
    b = a.read().splitlines()
    a.close
    FirstName = []
    LastName = []

    for i in b:
        NewList = i.split(" ")
        FirstName.append(NewList[0])
        LastName.append(NewList[1])

    return FirstName, LastName

def generateUsernames(firstName, lastName):
    # takes a list or dictionary of names and creates usernames, this function
    # returns a list or dictionary of usernames.


    UserNames = []

    for i in range(len(firstName)):
        x = firstName[i][0].lower() + lastName[i][0:4].lower()

        n = 1
        while x + "00" + str(n) in UserNames:
            n = n + 1
        UserNames.append(x + "00" + str(n))


    return UserNames

def writeUsernameFile(username, firstName, lastName):
    # takes a list or dictionary (or multiple) of usernames and writes the data
    # out to a file with the syntax

    file = open("usernames.txt", "w")

    for i in range(len(firstName)):
        file.write(username[i] + ": " + lastName[i] + ", " + firstName[i] + '\n')
    file.close()

def main():
    # Your code would be here

    # Calls the function to read a file into a list or dictionary and then
    # passes that list or dictionary to the functio that generates the
    # usernames.  Last, takes the returned usernames and passes it to the last
    # function that writes all the data out to a new file with the usernames
    # in it abiding by the above syntax.

    FirstName,LastName = readDataFile("students.txt")
    UserID = generateUsernames(FirstName,LastName)
    writeUsernameFile(UserID,FirstName,LastName)

if __name__ == "__main__":
    main()
    
