"""
Implement your AI here
Do not change the API signatures for __init__ or __call__
__call__ must return a valid action
"""

import numpy as np


class Submission:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size
        self.ai = AiHeuristic(board_size, win_size)

    def __call__(self, state):
        current, opponent = state.current_player(), 3 - state.current_player()
        optimal_score, optimal_move = -np.inf, None
        # Get  the best candidate moves considering central focus
        candidates = self.best_moves(state, central_focus=True)
        for r, c in candidates:
            if state.board[0, r, c] == 1:
                state.board[current, r, c] = 1
                score = self.ai.analyze_gomoku_board(state, current) - self.ai.analyze_gomoku_board(state, opponent)
                # Reset the board to the original state
                state.board[current, r, c] = 0
                # Update optimal move if the current score is better
                if score > optimal_score:
                    optimal_score, optimal_move = score, (r, c)
        return optimal_move

    # returns a list of positions for the empty cells, sorted in descending order of priority.
    def best_moves(self, state, central_focus=False):
        center = self.board_size // 2
        center_range = self.board_size // 4
        # Find empty cells on the board using NumPy
        empty_cells = np.where(state.board[0] == 1)  # Find empty cells using NumPy
        candidates = []
        for r, c in zip(*empty_cells):
            priority = 0
            # Increase priority for cells closer to the center if central focus is enabled
            if central_focus and abs(r - center) <= center_range and abs(c - center) <= center_range:
                priority += 10
            # Calculate proximity priority based on neighboring occupied cells
            proximity_priority = sum(
                1 for rd, cd in [(r1, c1) for r1 in range(-1, 2) for c1 in range(-1, 2)]
                if 0 <= r + rd < self.board_size and 0 <= c + cd < self.board_size and state.board[
                    0, r + rd, c + cd] != 1
            )
            priority += proximity_priority
            # Append the candidate move along with its priority to the list
            candidates.append(((r, c), priority))
        # Sort candidates based on priority in descending order
        candidates.sort(key=lambda x: x[1], reverse=True)
        return [pos for pos, _ in candidates]


class AiHeuristic:
    def __init__(self, board_size, win_size):
        self.board_size = board_size
        self.win_size = win_size

    # Calculates potential score considering various game scenarios
    def base_score_potential(self, single_score, open_ends):
        win_size = self.win_size
        # If achieving a winning move
        if single_score >= win_size - 1:
            return 2 * 10 ** 5
        # In case  of an imminent threat
        if single_score == win_size - 2:
            return 2 * 10 ** 4 if open_ends == 2 else 10 ** 3 if open_ends == 1 else 0
        central_bonus = 2 if single_score >= 2 else 1
        # Establish potential for future moves
        if single_score >= 2:
            score = 10 ** 2 * single_score * central_bonus
            return score * 2 if open_ends else score
        return 10 * (open_ends + 1) * central_bonus

    # returns the cumulative score obtained by evaluating the board state for a specific player.
    def analyze_gomoku_board(self, state, player):
        score = 0
        for r in range(self.board_size):
            for c in range(self.board_size):
                if state.board[player, r, c] == 1:
                    # Adding the score obtained from analyzing the player's position to the cumulative score
                    score += self.analyze_player_position(state, player, r, c)
        return score

    # Evaluating a direction from a given position on the game board.
    def analyze_direction(self, state, player, r, c, rd, cd):
        single_score = 0
        open_ends = 0

        # Forward and backward directions
        for direction in [1, -1]:
            for i in range(1, self.win_size):
                nr, nc = r + i * rd * direction, c + i * cd * direction
                # Check if the next position is within the bounds of the game board
                if not (0 <= nr < self.board_size and 0 <= nc < self.board_size):
                    break
                # Check if the next position contains a symbol belonging to the specified player
                if state.board[player, nr, nc] == 1:
                    single_score += 1
                # Check for an empty space (open end)
                elif state.board[0, nr, nc] == 1:
                    open_ends += 1
                    break
                else:
                    break
        return single_score, open_ends

    # Returns the overall evaluation score for the player's position in all directions
    def analyze_player_position(self, state, player, r, c):
        # Defining movement patterns representing different directions
        movement_patterns = [(1, 0), (0, 1), (1, 1), (1, -1)]
        overall_score = 0
        for rd, cd in movement_patterns:
            # Analyzing the player's position in the current direction
            single_score, open_ends = self.analyze_direction(state, player, r, c, rd, cd)
            # Convert directional scores into a combined potential score
            overall_score += self.base_score_potential(single_score, open_ends)
        return overall_score
