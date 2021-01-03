def enter_row(a):
    if a not in range(0, 3):
        while (1):
            print(a," is not a valid row.\n")
            a = int(input("choose a row number (0 to 2) :\n"))
            if (a < 3 and a >= 0):
                break
    return a
def enter_col(b):
    if b not in range(0, 3):
        while (1):
            print(b," is not a valid column\n")
            b = int(input("choose a column number (0 to 2) :\n"))
            if (b < 3 and b >= 0):
                break
    return b



def game(t,n1,n2,first_player):
    x,y='X','O';
    name_1,name_2=n1,n2
    if(first_player==n2):
        x,y='O','X';
        name_1,name_2=n2,n1

    for i in t:
        for j in i:
            print(j, end=" ")
        print()
    for s in range(0, 5):
        a = int(input("player of current turn : "+name_1+"\n\nchoose a row number (0 to 2) :\n"))
        a=enter_row(a)
        b = int(input("choose a column number (0 to 2): \n"))
        b=enter_col(b)

        if(t[a][b]!="."):
            while(1):
                print("slot is already occupied......\n")
                a=int(input("player of current turn : "+name_1+"\nchoose a row number (0 to 2) :\n"))
                a=enter_row(a)
                b = int(input("choose a column number (0 to 2) :\n"))
                b=enter_col(b)
                if(t[a][b]=='.'):
                    break
        t[a][b] =x

        for i in t:
            for j in i:
                print(j, end=" ")
            print()
        for i in t:       #horizontally
            c = 0
            for j in i:
                if (j == x):
                    c = c + 1
                    if (c == 3):
                        print("Game is over :\n "+name_1+" wins!\n")
                        return
        for i in range(0, 3):      #vertically
            c = 0
            for j in range(0, 3):
                if (t[j][i] == x):
                    c = c + 1
                    if (c == 3):
                        print("Game is over :\n "+name_1+" wins!\n")
                        return
        if ((t[0][0] == t[1][1] and t[0][0] == t[2][2]) and t[0][0] == x):    #diagonally
            print("Game is over :\n "+name_1+" wins!\n")
            return
        if ((t[0][2] == t[1][1] and t[0][2] == t[2][0]) and t[2][0] == x):
            print("Game is over :\n "+name_1+" wins!\n")
            return
        if (s < 4):
            a = int(input("player of current turn : " +name_2 +"\n\nchoose a row number (0 to 2) :\n"))
            a = enter_row(a)
            b = int(input("choose a column number (0 to 2): \n"))
            b = enter_col(b)

            if (t[a][b] != "."):
                while (1):
                    print("slot is already occupied......\n")
                    a = int(input("player of current turn : " + name_2 + "\nchoose a row number (0 to 2) :\n"))
                    a = enter_row(a)
                    b = int(input("choose a column number (0 to 2) :\n"))
                    b = enter_col(b)
                    if (t[a][b] == '.'):
                        break
            t[a][b] = y

            for i in t:
                for j in i:
                    print(j, end=" ")
                print()
            for i in t:
                c = 0
                for j in i:
                    if (j == y):
                        c = c + 1
                        if (c == 3):
                            print("Game is over :\n "+name_2+" wins!\n")
                            return
            for i in range(0, 3):
                c = 0
                for j in range(0, 3):
                    if (t[j][i] == y):
                        c = c + 1
                        if (c == 3):
                            print("Game is over :\n "+name_2+" wins!\n")
                            return
            if ((t[0][0] == t[1][1] and t[0][0] == t[2][2]) and t[0][0] == y):
                print("Game is over :\n "+name_2+" wins!\n")
                return
            if ((t[0][2] == t[1][1] and t[0][2] == t[2][0]) and t[2][0] == y):
                print("Game is over :\n "+name_2+" wins!\n")
                return

    else:
        print("it is a tie !\n")
        return

play="Y"
while(play=="Y"):
    n1=input("Enter a name for the X player :\n")
    n2=input("Enter a name for 0 player :\n ")
    first_player=input("Who plays first "+n1+ " or "+n2+" ?\n")

    if(first_player!=n1 and first_player!=n2):
      while(1):
        print(first_player+" is not registered player.\n")
        first_player = input("Who plays first "+n1+" or "+n2+" ?\n")
        if(first_player==n1 or first_player==n2):
            break

    t = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    game(t,n1,n2,first_player)

    while(1):
        play=input("Would you like tp play again ? (Y/N)\n")
        if(play=='N'):
           print("Bye !")
           break
        elif(play!='N' and play!='Y'):
           print(play+" is not a valid answer.")
        else:
            break