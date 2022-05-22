def main():
    fileName = input("Please enter the name of the file: ")
    theFile = open(fileName, 'r')
    line = theFile.readline()
    numInputs = int(line)
    codeList = []
    amountList = []

    for i in range(numInputs):
        code = theFile.readline()
        amount = theFile.readline()

        codeList.append(int(code))
        amountList.append(int(amount))

    for i in range(numInputs):
        checkCode = int(input("What is the id code you would like to check first: "))
        userAmount = int(input("What is the amount of this iteam you counted: "))

        for i in range(numInputs):
            if(checkCode == codeList[i]):
                checkList = i
                if (userAmount == amountList[i]):
                    print("No Error :)")
                    break
                else:
                    print("Error :(")
                    break
                    
            else:
                print("That id number was not found please input it again or try another one.")
                checkCode = int(input("What is the id code you would like to check first: "))
                userAmount = int(input("What is the amount of this iteam you counted: ")) 

        

        

main()