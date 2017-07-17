
def collatz(num):
    even_number = (num % 2 ==0)
    odd_number = (num % 2==1)
    if even_number:
        print(int(num)//2)
    else: 
        print((3*int(num))+1)

User_input = input('Enter Number:')
User_input = int(User_input)
collatz(User_input)

