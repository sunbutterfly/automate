
def collatz(num):
    even_number = (num % 2 ==0)
    odd_number = (num % 2==1)
    if even_number:
        return (int(num)//2)
    else: 
        return((3*int(num))+1)

User_input = input('Enter Number:')
User_input = int(User_input)

while True:
    if collatz(User_input) <=1:
        print(collatz(User_input))
        break
    else:
        User_input = collatz(User_input)
        print(User_input)
        
