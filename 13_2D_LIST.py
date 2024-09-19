#Program 13 - 2D LIST (MATRIX) CREATION

cols=int(input("Enter the number of columns you need: "))
rows=int(input("Enter the number of rows you need: "))
column=[]
for r in range(rows):
    row=[]
    for c in range(cols):
        rowelem=eval(input(f"Enter the value for row {r+1} and column {c+1}: "))
        row.append(rowelem)
    column.append(row)
print("\nYour 2D List:")
print(column)
