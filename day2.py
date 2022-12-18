def get_score(fp):
    opp_score, user_score = 0, 0
    opp_moves = {
        "A": 1, # Rock
        "B": 2, # Paper
        "C": 3  # Scissors
    }
    user_moves = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    for line in fp:
        moves = line.strip('\n').split()
        opp_move = moves[0]
        user_move = moves[1]

        # Opp chose Rock
        if opp_move == 'A':
            # User chose Rock - Draw
            if user_move == 'X':
                opp_score += 3
                user_score += 3
            # User chose paper - User Won
            elif user_move == 'Y':
                user_score += 6
            # User chose scissors - User Lost
            else:
                opp_score += 6
        # Opp chose paper
        elif opp_move == 'B':
            # User chose Rock - User Lost
            if user_move == 'X':
                opp_score += 6
            # User chose paper - Draw
            elif user_move == 'Y':
                user_score += 3
                opp_score += 3
            # User chose scissors - User Won
            else:
                user_score += 6
        # Opp chose scissors
        else:
            # User chose Rock - User Won
            if user_move == 'X':
                user_score += 6
            # User chose paper - User Lost
            elif user_move == 'Y':
                opp_score += 6
            # User chose scissors - Draw
            else:
                opp_score += 3
                user_score += 3

        user_score += user_moves[user_move]
        opp_score += opp_moves[opp_move]

    print("user:", user_score, "\nopponent:", opp_score)


def find_move(fp):
    opp_score, user_score = 0, 0
    opp_moves = {
        "A": 1,  # Rock
        "B": 2,  # Paper
        "C": 3  # Scissors
    }
    user_moves = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    # parse the file
    for line in fp:
        moves = line.strip('\n').split()
        opp_move = moves[0]
        user_move = moves[1]

        # Create points
        if opp_move == 'A': # Rock
            if user_move == 'X': # Lose
                user_score += user_moves['Z']
            elif user_move == 'Y': # Draw
                user_score += 3
                user_score += user_moves['X']
            else:   # Win
                user_score += 6
                user_score += user_moves['Y']

        elif opp_move == 'B':   # Paper
            if user_move == 'X': # Lose
                user_score += user_moves['X']
            elif user_move == 'Y': # Draw
                user_score += 3
                user_score += user_moves['Y']
            else:   # Win
                user_score += 6
                user_score += user_moves['Z']

        else:   # Scissors
            if user_move == 'X': # Lose
                user_score += user_moves['Y']
            elif user_move == 'Y': # Draw
                user_score += 3
                user_score += user_moves['Z']
            else:   # Win
                user_score += 6
                user_score += user_moves['X']
    print(user_score)


if __name__ == "__main__":
    # Get input file
    with open("input/day2_test", "r") as file:
        # get_score(file)
        find_move(file)
    with open("input/day2_input", "r") as file:
        # get_score(file)
        find_move(file)
