def right():
    turn_left()
    turn_left()
    turn_left()


def around():
    turn_left()
    turn_left()


while not at_goal():
    if wall_in_front() and wall_on_right() != True:
        right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
        if front_is_clear():
            move()
    elif wall_in_front():
        right()
    elif right_is_clear() and front_is_clear() != True:
        right()
        move()
    elif front_is_clear():
        if right_is_clear():
            right()
            move()
        else:
            move()