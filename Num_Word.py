"""


>>> num_words("The little brown fox ran fast")
brown 1
fast 1
fox 1
little 1
ran 1
the 1

>>> num_words("Red sky at night, sailors delight, red sky at morning, sailor take warning")
at 2
delight 1
morning 1
night 1
red 2
sailor 1
sailors 1
sky 2
take 1
warning 1



"""

def num_words(text):
    words = text.lower().split()
    from collections import Counter
    counts = Counter(words)
    for key,value in sorted(counts.items()):

        print(key,value)




num_words("The little brown fox ran fast")










