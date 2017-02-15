grid = [[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def get_state(grid, row, col):
    occupant = grid[col-1][row-1]
    if occupant == 1:
    return 'X'
if occupant == 2:
    return 'O'
if occupant == 3:
    return 'Y'
return ' '

def set_state(grid, row, col, player):
if player == 'X':
    occupant = 1
elif player == 'O':
    occupant = 2
elif player == 'Y':
    occupant = 3
grid[col-1][row-1] = occupant

def is_winner(grid):
if grid[0][0] == grid[0][1] == grid [0][2]:
    return True
if grid[0][1] == grid[0][2] == grid [0][3]:
    return True
if grid[0][2] == grid[0][3] == grid [0][4]:
    return True
if grid[0][3] == grid[0][4] == grid [0][5]:
    return True
if grid[1][0] == grid[1][1] == grid [1][2]:
    return True
if grid[1][1] == grid[1][2] == grid [1][3]:
    return True
if grid[1][2] == grid[1][3] == grid [1][4]:
    return True
if grid[1][3] == grid[1][4] == grid [1][5]:
    return True
if grid[2][0] == grid[2][1] == grid [2][2]:
    return True
if grid[2][1] == grid[2][2] == grid [2][3]:
    return True
if grid[2][2] == grid[2][3] == grid [2][4]:
    return True
if grid[2][3] == grid[2][4] == grid [2][5]:
    return True
if grid[3][0] == grid[3][1] == grid [3][2]:
    return True
if grid[3][1] == grid[3][2] == grid [3][3]:
    return True
if grid[3][2] == grid[3][3] == grid [3][4]:
    return True
if grid[3][3] == grid[3][4] == grid [3][5]:
    return True
if grid[4][0] == grid[4][1] == grid [4][2]:
    return True
if grid[4][1] == grid[4][2] == grid [4][3]:
    return True
if grid[4][2] == grid[4][3] == grid [4][4]:
    return True
if grid[4][3] == grid[4][4] == grid [4][5]:
    return True
if grid[5][0] == grid[5][1] == grid [5][2]:
    return True
if grid[5][1] == grid[5][2] == grid [5][3]:
    return True
if grid[5][2] == grid[5][3] == grid [5][4]:
    return True
if grid[5][3] == grid[5][4] == grid [5][5]:
    return True
if grid[0][0] == grid[1][0] == grid [2][0]:
    return True
if grid[1][0] == grid[2][0] == grid [3][0]:
    return True
if grid[2][0] == grid[3][0] == grid [4][0]:
    return True
if grid[3][0] == grid[4][0] == grid [5][0]:
    return True
if grid[0][1] == grid[1][1] == grid [2][1]:
    return True
if grid[1][1] == grid[2][1] == grid [3][1]:
    return True
if grid[2][1] == grid[3][1] == grid [4][1]:
    return True
if grid[3][1] == grid[4][1] == grid [5][1]:
    return True
if grid[0][2] == grid[1][2] == grid [2][2]:
    return True
if grid[1][2] == grid[2][2] == grid [3][2]:
    return True
if grid[2][2] == grid[3][2] == grid [4][2]:
    return True
if grid[3][2] == grid[4][2] == grid [5][2]:
    return True
if grid[0][3] == grid[1][3] == grid [2][3]:
    return True
if grid[1][3] == grid[2][3] == grid [3][3]:
    return True
if grid[2][3] == grid[3][3] == grid [4][3]:
    return True
if grid[3][3] == grid[4][3] == grid [5][3]:
    return True
if grid[0][4] == grid[1][4] == grid [2][4]:
    return True
if grid[1][4] == grid[2][4] == grid [3][4]:
    return True
if grid[2][4] == grid[3][4] == grid [4][4]:
    return True
if grid[3][4] == grid[4][4] == grid [5][4]:
    return True
if grid[0][5] == grid[1][5] == grid [2][5]:
    return True
if grid[1][5] == grid[2][5] == grid [3][5]:
    return True
if grid[2][5] == grid[3][5] == grid [4][5]:
    return True
if grid[3][5] == grid[4][5] == grid [5][5]:
    return True
return False


def print_grid(grid):
print_row(grid,1)
print('-----------')
print_row(grid,2)
print('-----------')
print_row(grid,4)
print('-----------')
print_row(grid,4)
print('-----------')
print_row(grid,5)
print('-----------')
print_row(grid,6)




def print_row(grid, row):
output = get_state(grid,row,1)
output += '|' + get_state(grid, row, 2)
output += '|' + get_state(grid, row, 3)
output += '|' + get_state(grid, row, 4)
output += '|' + get_state(grid, row, 5)
output += '|' + get_state(grid, row, 5)
print (output)


ongoing = True
currentPlayer = 'X'
spaces = 36

while ongoing:
print_grid(grid)
print (currentPlayer + "'s turn")
print("Column?")
col = int(input())
print("Row?")
row = int(input())
current = get_state(grid,row,col)
if current != ' ':
    print ("That spot is taken!")
else:
    set_state(grid, row, col, currentPlayer)
    spaces -= 1
    if is_winner(grid):
        print (currentPlayer + "'s wins!")
        ongoing = False
    else:
        if currentPlayer == 'X':
            currentPlayer = 'O'
        elif currentPlayer == 'O':
            curentPlayer = 'Y'
        elif currentPlayer == 'Y':
            currentPlayer = 'X'

    if spaces == 0:
        print("Stalemate!")
        ongong = False
