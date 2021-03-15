# Description: The aim of this file is to translate keyboard buttons into dots

#
def inverse_value(key_presses, key):
    """Inverses the value assigned to the key: 0 -> 1, 1 -> 0
    
    Parameters:
        key_presses (Dict)      Dictionary which counts amount of times keys pressed.
        key         (String)    Letter of key which has been pressed.

    Returns:
        key_presses (Dict)      Dictionary which counts amount of times keys pressed."""

    if key_presses[key]:
        key_presses[key] = 0
    else:
        key_presses[key] = 1
    return key_presses


#
# Returns the dotset
def check_keys(pg, key_presses):
    """Checks pygame's events to see what buttons have been pressed.

    Parameters:
        pg          (Pygame)    Pygame Module contains actions from pygame.
        key_presses (Dict)      Dictionary which counts amount of times keys pressed.

    Returns:
        current_dots_hash   (String)    The hash calculated after inversing each key press."""

    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_f:
                key_presses = inverse_value(key_presses, "F")

            if event.key == pg.K_d:
                key_presses = inverse_value(key_presses, "D")

            if event.key == pg.K_s:
                key_presses = inverse_value(key_presses, "S")

            if event.key == pg.K_j:
                key_presses = inverse_value(key_presses, "J")

            if event.key == pg.K_k:
                key_presses = inverse_value(key_presses, "K")

            if event.key == pg.K_l:
                key_presses = inverse_value(key_presses, "L")

    current_dots_hash = str(key_presses["F"]) + str(key_presses["J"]) + str(
        key_presses["D"]) + str(key_presses["K"]) + str(key_presses["S"]) + str(key_presses["L"])

    return current_dots_hash
