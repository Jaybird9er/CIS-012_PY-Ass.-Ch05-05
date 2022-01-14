## Function determines the validity of user's input
def validateUserInput():
    checkInput = True
    while checkInput  == True:
        print("Enter two positive integer numbers.")
        print("First number must be less than the second number:")
        print("Enter numbers:", end = ' ')
        userInput = input()
        print('\n')
        nums1And2 = userInput.split()
    ## Not sure if using try/except bad form, but couldn't get it to work with if/else
        try:
            firstNum = int(nums1And2[0])
            secondNum = int(nums1And2[1])
            if firstNum < 0 or secondNum < 0:
                print("No negative numbers!\nPlease try again.\n")
            elif firstNum > secondNum:
                print("First number must be less than the second number!\nPlease try again.\n")
            else:
                checkInput = False
        except:
            print("Incorrect Input.\nPlease try again.\n")
    return nums1And2

## Resuts for the values below (odd nums, sum even nums, sum square of odd nums)
def oddNumbers(firstNum, secondNum):
    count = firstNum
    print("Odd integers between", firstNum, "and", secondNum, "are:")
    while count <= secondNum:
        if count % 2 == 1:
            print(count, end = ' ')
        count += 1
    print('\n')

def sumEvenNumbers(firstNum, secondNum):
    count = firstNum
    sumAllEven = 0
    while count <= secondNum:
        if count % 2 == 0:
            sumAllEven += count
        count += 1
    return sumAllEven

def sumSquareOddNumbers(firstNum, secondNum):
    count = firstNum
    sumOddSqrt = 0
    while count <= secondNum:
        if count % 2 == 1:
            sumOddSqrt += count * count
        count += 1
    return sumOddSqrt

## Function determines if the user will repeat program
def main():
    repeatProgram = True
    while repeatProgram == True:
        nums1And2 = validateUserInput()
        firstNum = int(nums1And2[0])
        secondNum = int(nums1And2[1])
        sumEven = sumEvenNumbers(firstNum, secondNum)
        sumSquareOdd = sumSquareOddNumbers(firstNum, secondNum)

        oddNumbers(firstNum, secondNum)
        print("Sum of even integers between", firstNum, "and", secondNum, "=", sumEven, '\n')
        print("Sum of the squares of odd integers between", firstNum, "and", secondNum, "=", sumSquareOdd, '\n\n')

        ## User decides to repeat program or not
        print("Do you want to repeat this program?\ny/n")
        userChoice = input()
        if userChoice == 'n' or userChoice == 'N':
           repeatProgram = False
        else:
            print('\n', end = '')

main()

print("\nBye!")
