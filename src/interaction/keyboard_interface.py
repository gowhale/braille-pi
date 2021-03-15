# Description: The aim of this file is to translate keyboard buttons into dots

# Inverses the value assigned to the key: 0 -> 1, 1 -> 0
def inverse_value(hashmap, key):
    if hashmap[key]:
        hashmap[key] = 0
    else:
        hashmap[key] = 1
    return hashmap


# Checks pygame's events to see what buttons have been pressed
# Returns the dotset
def check_keys(pg, key_presses):
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
