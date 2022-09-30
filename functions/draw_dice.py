from random import choice
# drawn_dice = ["Yellow die", "green die"]
dice_cup = ["green die", "green die", "green die", "green die", "green die", "green die",
            "yellow die", "yellow die", "yellow die", "yellow die", "red die", "red die"]
red_die = ["brain", "footsteps", "footsteps",
           "shotgun blast", "shotgun blast", "shotgun blast"]
green_die = ["brain", "brain", "brain",
             "footsteps", "footsteps", "shotgun blast"]
yellow_die = ["brain", "brain", "footsteps",
              "footsteps", "shotgun blast", "shotgun blast"]


def draw_dice_func(drawn_dice=[]):
    while len(drawn_dice) < 3:
        drawn_dice.append(choice(dice_cup))
    print(f"drawn dice = {drawn_dice}")
    return drawn_dice


# draw_dice_func()
