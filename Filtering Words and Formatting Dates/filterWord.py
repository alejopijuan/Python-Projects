#! /usr/bin/env python3
# Alejo Pijuan
# 10/20/16  
# Replace a certain word with one dash for each letter in the word

def filterWord():
    n=input("Enter a sentence: ")
    m=input("Enter a word to replace: ")
    nn=n.split()
    nnn=''
    for i in nn:
        if i==m:
            nnn=nnn+"-"*len(i)+" "           
        else:
            nnn=nnn+i+" "
    return("The resulting string is: " + nnn)



            # o="-"*count OR use length and multiply "-" times length


def main():
    print(filterWord())

if __name__ == "__main__":
    main()
