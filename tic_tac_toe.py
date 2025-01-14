import streamlit as st
import numpy as np

# Initialize the game
def initialize_game():
    return np.full((3, 3), ''), 'X'  # Create a 3x3 board and set the starting player

# Check for a win
def check_winner(board):
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != '':
            return board[i, 0]
        if board[0, i] == board[1, i] == board[2, i] != '':
            return board[0, i]
    if board[0, 0] == board[1, 1] == board[2, 2] != '':
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != '':
        return board[0, 2]
    return None

# Display the game board
def display_board(board):
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                button_key = f'button_{i}_{j}_{st.session_state.turn}'  # Unique key for each button
                if st.button(board[i, j] if board[i, j] else '', key=button_key):
                    return i, j
    return None, None

# Main function for the app
def main():
    if 'board' not in st.session_state:
        st.session_state.board, st.session_state.current_player = initialize_game()
        st.session_state.game_over = False
        st.session_state.turn = 0

    st.title("Tic-Tac-Toe Game")
    board = st.session_state.board
    current_player = st.session_state.current_player
    game_over = st.session_state.game_over

    if not game_over:
        i, j = display_board(board)
        if i is not None and j is not None and board[i, j] == '':
            board[i, j] = current_player
            winner = check_winner(board)
            if winner:
                st.success(f"Player {winner} wins!")
                game_over = True
                st.session_state.game_over = True
            elif '' not in board:
                st.warning("It's a draw!")
                game_over = True
                st.session_state.game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
                st.session_state.current_player = current_player
            
            # Update session state
            st.session_state.board = board

    if st.button("Restart Game"):
        st.session_state.board, st.session_state.current_player = initialize_game()
        st.session_state.game_over = False
        st.session_state.turn += 1  # Increment turn to ensure unique keys

if __name__ == "__main__":
    main()
