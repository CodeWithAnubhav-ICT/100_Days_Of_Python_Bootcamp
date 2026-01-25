def turn_right() :
    turn_left()
    turn_left()
    turn_left()    
while front_is_clear() is True:
    move()
turn_left()
while at_goal() is False :
    if right_is_clear() is True :
        turn_right()
        if front_is_clear() is True :
            move()            
    elif front_is_clear() is True :
        move()            
    else :
        turn_left()