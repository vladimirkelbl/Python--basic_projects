import random

def new_game():
    A = []
    for i in range (4):
        A.append([0] * 4)
    A = add_new_2_or_4(A)
    A = add_new_2_or_4(A)
    
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    
    return A

def add_new_2_or_4(mat):
    flag = False                #check if grid contains zero field
    for i in range(4):
        if flag == True:
            break
        for j in range (4):
            if mat[i][j] == 0:
                flag = True
                break                
    while flag:                 #puts new 2 or 4 into random zero field
        x = random.choice(range(4))
        y = random.choice(range(4))
        if mat[x][y] == 0:
            cond_for_4 = random.choice(range(5))        #probability 20 % for new 4
            if cond_for_4 == 2:
                mat[x][y] = 4
            else:
                mat[x][y] = 2
            break;
    return mat
        
def get_current_state(mat):
    #checking if player has won
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return "\tYOU WON"
                
    
    #checking if player may continue due to zero field
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 0                
    
    #checking if player may continue due to addition of two fields
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1] or mat[i][j] == mat[i+1][j]):
                return 0
            
    for i in range(3):
        if (mat[i][3] == mat[i+1][3]):
            return 0
        if (mat[3][i] == mat[3][i+1]):
            return 0
    
    return "\tGAME OVER"

def show_matrix(mat):
    print()
    print("\t|", end="")
    for i in range(4):
            print("-" * 9 + "|", end = "")
    for i in range(4):
        print()
        print("\t|", end="")
        for j in range(4):
            if mat[i][j] != 0:
                print("%6d%4s" % (mat[i][j], "|"), end="")
            else:
                print("%6s%4s" % (" ", "|"), end="")
        print()
        print("\t|", end="")
        for i in range(4):
            print("-" * 9 + "|", end = "")    
    print("\n")

def compress(mat):      #compress to left
    changed = False
    new_mat = [[0] * 4 for i in range(4)]
    
    for i in range(4):
        position = 0
        for j in range(4):
            if (mat[i][j] != 0):
                new_mat[i][position] = mat[i][j]
                if (j != position):
                    changed = True
                position += 1
                                
    return new_mat, changed

def merge(mat):         #merge to left
    changed = False
    new_mat = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(3):
            if (mat[i][j] != 0 and mat[i][j] == mat[i][j+1]):   #if addition is possible, it adds
                new_mat[i][j] = mat[i][j] + mat[i][j+1]
                mat[i][j] = 0
                mat[i][j+1] = 0
                changed = True
            else:
                new_mat[i][j] = mat[i][j]
                #check if in the end of columns (j on column 2; 3 is not influded in range                                                          of for cycle) and not adding; if true there's need to retain value of last (third) column
                if (j == 2):
                    new_mat[i][j+1] = mat[i][j+1]
    #better to change passed matrix, not to create new
    return new_mat, changed

def reverse_right_left(mat):       #miroring of matrix on middle diagonal line
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
                              
    return new_mat

def reverse_up_down(mat):       #miroring of matrix on middle horizontal line
    new_mat = []
    
    for i in range(4):
        new_mat.append(mat[3-i])
            
    return new_mat

def rotate(mat):       #rotation of matrix mathematically possitive
    new_mat = []
    for j in range(4):
        new_mat.append([])
        for i in range(4):
            new_mat[j].append(mat[i][3-j])
                              
    return new_mat

def transpose(mat):
    new_mat = []
    
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
            
    return new_mat

def move_left(mat):
    new_mat, cond1 = compress(mat)
    new_mat, cond2 = merge(new_mat)
    cond = cond1 or cond2
    if cond2:
        new_mat, temp = compress(new_mat)
    
    return new_mat, cond
    
def move_right(mat):
    new_mat = reverse_right_left(mat)
    
    new_mat, cond1 = compress(new_mat)
    new_mat, cond2 = merge(new_mat)
    cond = cond1 or cond2
    if cond2:
        new_mat, temp = compress(new_mat)
    
    new_mat = reverse_right_left(new_mat)
    return new_mat, cond
    
def move_up(mat):
    #mat = rotate(mat)
    #~      #or not
    new_mat = transpose(mat)       
    
    new_mat, cond1 = compress(new_mat)
    new_mat, cond2 = merge(new_mat)
    cond = cond1 or cond2
    if cond2:
        new_mat, temp = compress(new_mat)
    
    new_mat = transpose(new_mat)
    #~
    #mat = rotate(mat)
    #mat = reverse_up_down(mat)
    return new_mat, cond
    
def move_down(mat):
    new_mat = transpose(mat)
    new_mat = reverse_right_left(new_mat)
    
    new_mat, cond1 = compress(new_mat)
    new_mat, cond2 = merge(new_mat)
    cond = cond1 or cond2
    if cond2:
        new_mat, temp = compress(new_mat)
        
    new_mat = rotate(new_mat)    
    return new_mat, cond
