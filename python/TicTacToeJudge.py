def is_solved(board):
    
    main_diagonals = []
    secundary_diagonals = []
    status = False
    
    while status != True:
        for i in board:

            if len(set(i)) == 1 and 1 in set(i):
                print('X Venceu')
                break

            elif len(set(i)) == 1 and 2 in set(i):
                print('O Venceu')
                break

            break
            
        for i in range(len(board)):
            for j in range(len(board)):
                if i == j:
                    main_diagonals.append(board[i][j])
                if (i+j) == (len(board) - 1):
                    secundary_diagonals.append(board[i][j])
            
        print(main_diagonals, secundary_diagonals)
                    
        if len(set(main_diagonals)) == 1 and 1 in set(main_diagonals):
            print('X Venceu')
        
        
board = [[1, 1, 1],
         [1, 1, 1],
         [1, 2, 1]]
         
is_solved(board)