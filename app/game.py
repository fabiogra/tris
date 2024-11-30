import streamlit as st
import numpy as np
import numpy as np
import uuid
import streamlit as st
import random

@st.cache_resource
def get_game_sessions():
    return {}


def initialize_game(mode='pvp'):
    session = {
        'board': np.zeros((3, 3), dtype=int),
        'current_player': 1,
        'player_x': str(uuid.uuid4()),
        'player_o': 'AI' if mode == 'ai' else None,
        'game_over': False,
        'winner': None,
        'mode': mode,
        'ai_player': AIPlayer() if mode == 'ai' else None
    }
    return session
    
def check_winner(board):
    for i in range(3):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != 0:
            return board[i, 0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != 0:
            return board[0, i]
    if np.all(np.diag(board) == board[0, 0]) and board[0, 0] != 0:
        return board[0, 0]
    if np.all(np.diag(np.fliplr(board)) == board[0, 2]) and board[0, 2] != 0:
        return board[0, 2]
    if not np.any(board == 0):
        return 0
    return None

# Function to handle a move
def make_move(session_id, row, col):
    game_sessions = get_game_sessions()
    session = game_sessions[session_id]
    
    if session['board'][row, col] == 0 and not session['game_over']:
        session['board'][row, col] = session['current_player']
        session['winner'] = check_winner(session['board'])
        
        if session['winner'] is not None:
            session['game_over'] = True
        else:
            session['current_player'] = 3 - session['current_player']
            
            # If it's AI's turn and the game isn't over
            if session.get('mode') == 'ai' and session['current_player'] == 2 and not session['game_over']:
                ai_move = session['ai_player'].make_move(session['board'])
                if ai_move:
                    ai_row, ai_col = ai_move
                    session['board'][ai_row, ai_col] = 2
                    session['winner'] = check_winner(session['board'])
                    if session['winner'] is not None:
                        session['game_over'] = True
                    else:
                        session['current_player'] = 1
        
        game_sessions[session_id] = session

@st.fragment(run_every=1)
def game_board(session): 
    board_message = st.empty()       
    if st.session_state.wait_to_start:
        if session['player_o'] and session['player_x']:
            st.session_state.wait_to_start = False
            st.toast("Players have joined! Game is starting...", icon="🎉")
        else:
            board_message.markdown("Waiting for the other player to join...")
            return
    elif session['current_player'] == 1 and st.session_state.player_id == session['player_x']:
        board_message.markdown("#### It's your turn, Player X")
    elif session['current_player'] == 2 and st.session_state.player_id == session['player_o']:
        board_message.markdown("#### It's your turn, Player O")
    else:
        board_message.markdown("#### Waiting for the other player...")
    # Display the game board
    board = session['board']
    
    for i in range(3):
        with st.container():
            cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                disabled = not (
                    (session['current_player'] == 1 and st.session_state.player_id == session['player_x']) or
                    (session['current_player'] == 2 and st.session_state.player_id == session['player_o'])
                )
                if board[i, j] == 0:
                    st.button("", key=f"{i}-{j}", on_click=make_move, args=(st.query_params['session_id'], i, j), help="Click to make a move", disabled=disabled)
                elif board[i, j] == 1:
                    st.button("❌", key=f"{i}-{j}", disabled=True)
                elif board[i, j] == 2:
                    st.button("⭕", key=f"{i}-{j}", disabled=True)
    # Display the result
    if session['game_over']:
        if session['winner'] == 0:
            board_message.markdown("## It's a draw!")
        else:
            if session['winner'] == 1 and st.session_state.player_id == session['player_x']:
                board_message.markdown("## You won! 🎉")
            elif session['winner'] == 2 and st.session_state.player_id == session['player_o']:
                board_message.markdown("## You won! 🎉")
            else:
                winner = "X" if session['winner'] == 1 else "O"
                board_message.markdown(f"## You lost! Player {winner} wins!")

class AIPlayer:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
    
    def make_move(self, board):
        if self.difficulty == 'easy':
            return self._make_random_move(board)
        else:  # medium/hard
            return self._make_smart_move(board)
    
    def _make_random_move(self, board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) 
                      if board[i, j] == 0]
        if empty_cells:
            return random.choice(empty_cells)
        return None
    
    def _make_smart_move(self, board):
        # First check if AI can win
        winning_move = self._find_winning_move(board, 2)  # AI is player 2 (O)
        if winning_move:
            return winning_move
            
        # Then block player from winning
        blocking_move = self._find_winning_move(board, 1)  # Human is player 1 (X)
        if blocking_move:
            return blocking_move
            
        # Otherwise make a random move
        return self._make_random_move(board)
    
    def _find_winning_move(self, board, player):
        for i in range(3):
            for j in range(3):
                if board[i, j] == 0:
                    # Try the move
                    board[i, j] = player
                    if check_winner(board) == player:
                        board[i, j] = 0  # Reset the cell
                        return (i, j)
                    board[i, j] = 0  # Reset the cell
        return None
