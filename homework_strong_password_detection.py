
'''HOMEWORK: Remove re.compile, and make
    is_strong work by using re.search instead
    (that's different from regex.search)'''


import re


def is_strong(password):
    patterns = [
        r'.{8}',
        r'\d',
        r'[A-Z]',
        r'[a-z]',
    ]
    for patern in patterns:
        match = re.search(patern, password)
        if match == None:
            return False
    return True


## do not edit below this line!

passwords = [
    'honkeydonky',
    'HonkyDonky42',
    '123Twinkie',
    'BADPASSWORD',
    'G00dPASSword',
    'youAreAD0RK',
    '5BLAHBLAHBLAH',
]

for password in passwords:
    if is_strong(password):
        print(password + " is a good password")
    else:
        print(password + " is NOT a good password")