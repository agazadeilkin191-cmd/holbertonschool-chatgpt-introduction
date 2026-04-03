def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("-" * 11)

def check_winner(board):
    # Sətirlər üzrə yoxlama
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Sütunlar üzrə yoxlama
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diaqonallar üzrə yoxlama
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Oyunçu {current_player}, sətir daxil et (0, 1, 2): "))
            col = int(input(f"Oyunçu {current_player}, sütun daxil et (0, 1, 2): "))
            
            if row not in range(3) or col not in range(3):
                print("Səhv daxiletmə! 0, 1 və ya 2 yazın.")
                continue
                
            if board[row][col] == " ":
                board[row][col] = current_player
                
                # Qalib varmı?
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f"Təbriklər! Oyunçu {winner} qazandı!")
                    break
                
                # Heç-heçə yoxlanışı
                if is_full(board):
                    print_board(board)
                    print("Oyun heç-heçə bitdi!")
                    break
                
                # Növbəni dəyiş
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Bu xana artıq doludur! Yenidən cəhd edin.")
                
        except ValueError:
            print("Xahiş olunur rəqəm daxil edin!")

if __name__ == "__main__":
    tic_tac_toe()
