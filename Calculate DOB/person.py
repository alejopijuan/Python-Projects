#! /usr/bin/env python3

# Alejo Pijuan
# 11/19/2016
# Calculate date of birth and name in a class

from datetime import date

class Person:
    def __init__(self,name,day,month,year):
        today = date.today()
        if (year > today.year) or (year == today.year and month > today.month) or (year == today.year and month == today.month and day > today.day):
            raise ValueError ("{0},{1},{2} Date you have entered is in future.".format(day,month,year)) 
        
        self.name = name
        self.day = day
        self.month = month
        self.year = year


    def getAge(self):
        today = date.today()
        year_difference = today.year - self.year
        is_birthday_early_or_not = (self.month, self.day)>(today.month,self.day)
        age = year_difference - is_birthday_early_or_not
        return age

    def setName(self,name1):
        self.name = name1

    def printName(self):
        print(self.name)
        
def main():
    person1 = Person ("Alejo Pijuan",30, 3, 1997)
    person1.printName()
    print(person1.getAge())
    person1.setName("Alejo L Pijuan")
    person1.printName()
    person2 = Person("Someone Great", 4, 18, 1998)
    person2.printName()
    print(person2.getAge())
    person2.setName ("Alejo Great")
    person2.printName()
       

    
if __name__ == '__main__':
    main()


