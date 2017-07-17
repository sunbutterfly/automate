
def collatz(num):
    even_number = (num % 2 ==0)
    odd_number = (num % 2==1)
    if even_number:
        return (int(num)//2)
    else: 
        return((3*int(num))+1)

User_input = input('Enter Number:')
User_input = int(User_input)
New_num = User_input

while True:
    New_num = collatz(New_num)
    if New_num <=1:
        print(New_num)
        break
    else:
       print(New_num)
        
