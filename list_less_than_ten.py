

a = [1,1,2,3,5,8,13,21,34,55,89]


userNum = int(input('please enter a number:'))
def newNum(nums):
    return [num for num in nums if num < userNum]
print(newNum(a))



