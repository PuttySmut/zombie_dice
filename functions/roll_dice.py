import random
blast_emoji = "\U0001f4a5"
# foot emoji unicode
foot_emoji = "\U0001f9B6"
# brain emoji unicode
brain_emoji = "\U0001f9e0"

drawn_dice = ["yellow die", "red die", "green die"]


def roll_dice_func(drawn_dice):
    zombie_dict = {
        "red_die": ["brain", "footsteps", "footsteps", "shotgun blast", "shotgun blast", "shotgun blast"],
        "green die": ["brain", "brain", "brain", "footsteps", "footsteps", "shotgun blast"],
        "yellow die": ["brain", "brain", "footsteps", "footsteps", "shotgun blast", "shotgun blast"]
    }
    rolled_results = []
    while True:
        for key, value in zombie_dict.items():
            rolled_side = random.choice(value)
            rolled_results.append(rolled_side)
        if len(rolled_results) == 3:
            break
    print("roll results are")
    print(f"die one- {drawn_dice[0]} rolled- {rolled_results[0]}")
    print(f"die two- {drawn_dice[1]} rolled-{rolled_results[1]}")
    print(f"die three- {drawn_dice[2]} rolled-{rolled_results[2]}")
    return rolled_results


roll_dice_func(drawn_dice)
