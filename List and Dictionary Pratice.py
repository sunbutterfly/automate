

'''inventory = {
    'gold': 500,
    'pouch': ['flint','twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')

inventory['gold'] = inventory['gold'] +50
inventory['pouch'].insert(0,'apple')

##print(inventory['backpack'])

##print(list(inventory.values()))

print(inventory)'''

def letter_counts(letters):
    lower =letters.lower()
    counts = {}
    for letter in lower:
        counts[letter] = counts.get(letter,0)+1
    del counts[' ']
    for k,v in sorted(counts.items()):
        print(str(k) + ' ' + str(v))




a = 'ThiS is String with Upper and lower case Letters'

letter_counts(a)