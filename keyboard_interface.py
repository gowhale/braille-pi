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
def check_keys(pg, dot_has_test):
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:

            if event.key == pg.K_f:
                dot_has_test = inverse_value(dot_has_test, "F")

            if event.key == pg.K_d:
                dot_has_test = inverse_value(dot_has_test, "D")

            if event.key == pg.K_s:
                dot_has_test = inverse_value(dot_has_test, "S")

            if event.key == pg.K_j:
                dot_has_test = inverse_value(dot_has_test, "J")

            if event.key == pg.K_k:
                dot_has_test = inverse_value(dot_has_test, "K")

            if event.key == pg.K_l:
                dot_has_test = inverse_value(dot_has_test, "L")

    current_dots_hash = str(dot_has_test["F"]) + str(dot_has_test["J"]) + str(
        dot_has_test["D"]) + str(dot_has_test["K"]) + str(dot_has_test["S"]) + str(dot_has_test["L"])

    return current_dots_hash
