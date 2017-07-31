
defaultTableData = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for rownum, row in enumerate(tableData):
        for item in row:
            if len(item) > colWidths[rownum]:
                colWidths[rownum] = len(item)


    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]+1), end = '')
        print()



printTable(defaultTableData)

