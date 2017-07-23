

def addToInventory(inventory, addedItems):
    # structure: "for varname in sequence(sequence can be a list or tuple):"
    # wrong: "for inventory in addToInventory:"
    #inventory is dictionary
    #addedItems is a list of string
    #addedItem is a string
    for addedItem in addedItems:
        inventory.setdefault(addedItem,0)
        inventory[addedItem] = inventory[addedItem]+1
    return inventory



def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' '+ str(k))
        item_total = item_total + v
    print("Total number of items: "+ str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger','gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)










