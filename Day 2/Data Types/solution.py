def turn_right():
    turn_left()
    turn_left()
    turn_left()


def guide_wall():
    turn_left()
    move()
    if wall_in_front():
        turn_left():
    move()


while not at_goal():
    if not wall_in_front():
        move()
    else:
        guide_wall()





