import pprint


spam = ['apples', 'bananas', 'tofu', 'cats']

def print_items(items):
    items.insert(-1,'and')

    print(','.join(items))

print_items(spam)


