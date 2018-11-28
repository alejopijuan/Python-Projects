#! /usr/bin/env python3
# Alejo Pijuan
# 10/20/16
"""This program should ask for the user to
input the date as month day, year.The program
should then convert it to the day month year format and display its output."""

def formatDate(us):
    
    eu=us.split()
    
    month=eu[0]
    day=eu[1][:-1]
    year=eu[2]
    
    return(day +' '+ month+' ' + year)
    


def main():
    us=input("Please enter a date in US format (month day, year): ")
    print("The date converted to European format is: " + formatDate(us))

if __name__ == "__main__":
    main()
