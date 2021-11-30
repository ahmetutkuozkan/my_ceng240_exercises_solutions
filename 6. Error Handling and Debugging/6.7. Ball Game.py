def ball_game(list_of_child,times_of_turn):
    output=0
    for child_number in range(times_of_turn):
        try:
            output=list_of_child[output]
        except:
            break
    return output
