def conversion(data):
    
    x = data
    smoots = x / 5.583
    return round(smoots,1)


def main():
    while True:
        y = float(input("please enter bridge lentgh in feet:"))
        
        if  y >= 0:
            
            print(conversion(y))

        elif y < 0:
            print("error number must be positive")
        
        z = input( "do you want to continue ? y/n:")
        if z == "y":
                  continue
        else:
                  break



        
if __name__ == "__main__":
    main()
