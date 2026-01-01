import random

def player(prev_play, opponent_history=[]):
    """
    Rock Paper Scissors AI player function.
    Uses multiple strategies to beat common bots.
    """
    
    # Save opponent history
    if prev_play != '':
        opponent_history.append(prev_play)

    # If first move, play randomly
    if len(opponent_history) == 0:
        return random.choice(['R', 'P', 'S'])
    
    # Count opponent's moves
    r_count = opponent_history.count('R')
    p_count = opponent_history.count('P')
    s_count = opponent_history.count('S')

    # Strategy 1: Beat the most common move
    if r_count > p_count and r_count > s_count:
        return 'P'  # Paper beats Rock
    elif p_count > r_count and p_count > s_count:
        return 'S'  # Scissors beats Paper
    elif s_count > r_count and s_count > p_count:
        return 'R'  # Rock beats Scissors

    # Strategy 2: If tied, random choice
    return random.choice(['R', 'P', 'S'])
