
###Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
###(If you don’t know what a divisor is, it is a number that divides evenly into another number.
###For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


userNum = int(input('please enter a number:'))

def numDivisor(num):
    numList = []
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            numList.append(divisor)
        divisor +=1

    return numList

print(numDivisor(userNum))


