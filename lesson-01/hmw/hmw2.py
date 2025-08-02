rows = 9

for i in range(1, rows + 1):
    stars = '* ' * i 
    stars = stars.rstrip()
    line = stars + ' ' + stars  
    print(line.center(rows * 4))