#!/usr/bin/env python3
# Alejo Pijuan
# 11/03/2016
# Binary Search

# Function to read the names and phones into lists
def getLists():
    infile = open("phones.txt",'r')
    line = infile.readline()

    names = []
    numbers = []

    while line != "":
        line = line.strip()
        name, number = line.split(',')
        names = names + [name]
        numbers = numbers + [number]
        line = infile.readline()

    infile.close()
    return names, numbers

# Function to find the name and return the associated phone number
# You must complete this function!
def binarySearch(names, phones, name):
    # left side of list    
    left = 0	
    # right side of the list				
    right = len(names) - 1
    
    while left<=right:
        middle = int(left+right)
        if names[middle]==name:
            return phones[middle]
        elif name>names[middle]:
            left=middle+1
        else:
            right=middle-1
    return ("not found")
        

# Main Function
def main():
    # Get the lists
    names, phones = getLists()
    # Get the name to search for
    theName = input("Enter the name to search for: ")

    # Find the phone number for the given name
    phoneNum = binarySearch(names, phones, theName)
    print("The phone number for ", theName, " is ", phoneNum)

if __name__ == "__main__":
    main()
