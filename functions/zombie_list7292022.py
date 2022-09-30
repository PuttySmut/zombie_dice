# July 29,2022 2313
import random
dice_emoji = "\U0001f3b2"
zombie_emoji = "\U0001f9df"
# blast emoji unicode
blast_emoji = "\U0001f4a5"
# foot emoji unicode
foot_emoji = "\U0001f9B6"
# brain emoji unicode
brain_emoji = "\U0001f9e0"


def roll_dice_func():
    red_die = ["brain", "footsteps", "footsteps",
               "shotgun blast", "shotgun blast", "shotgun blast"]
    green_die = ["brain", "brain", "brain",
                 "footsteps", "footsteps", "shotgun blast"]
    yellow_die = ["brain", "brain", "footsteps",
                  "footsteps", "shotgun blast", "shotgun blast"]
    dice_cup = ["green die", "green die", "green die", "green die", "green die", "green die",
                "yellow die", "yellow die", "yellow die", "yellow die", "red die", "red die"]
    roll_results = []
    drawn_dice = []
    while len(drawn_dice) != 3:
        drawn_dice.append(random.choice(dice_cup))
    for die in drawn_dice:
        if "green die" in drawn_dice:
            roll_results.append(random.choice(green_die))
        elif "yellow die" in drawn_dice:
            roll_results.append(random.choice(yellow_die))
        elif die == "red die":
            roll_results.append(random.choice(red_die))
    print(f"{dice_emoji}current dice :{drawn_dice}")
    print(f"{dice_emoji}roll results:{roll_results}")
    return roll_results


def computer_turn_func():
    computer_scores = [3, 6, 3, 5, 5, 1, 0, 0, 0, 2, 3, 1, 0]
    computer_brains = random.choice(computer_scores)
    print(f"computer scored {computer_brains} brains{brain_emoji}")
    print("player turn")
    return computer_brains


player_brains = 0
user_round_hp = 3
round_brains = 0
computer_total_brains = 0
print(
    f"          {zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}")
print(f"{dice_emoji}{zombie_emoji}{dice_emoji} ===Welcome to zombie dice==={zombie_emoji}{dice_emoji}{zombie_emoji}")
print("=============please make a choice================     ")
print(
    f"           {zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}")
choice = input("    1:roll dice 3:exit\n")
if choice == "1":
    if player_brains == 13:
        print("you win")
    while player_brains < 13 and computer_total_brains < 13:
        while user_round_hp >= 1:
            if user_round_hp <= 0:
                print("you got blasted! round over!")
                break
            roll_dice = roll_dice_func()

            for item in roll_dice:
                if item == "brain":
                    round_brains += 1

            for item in roll_dice:
                if item == "shotgun blast":
                    user_round_hp -= 1

            print(f"current round brains {round_brains}{brain_emoji}")
            print(f"current HP {user_round_hp}")
            print(f"total current brains:{player_brains}{brain_emoji}")
            choice = input("1:roll dice 2:keep brains ")
            if choice == "2":
                player_round_hp = 3
                player_brains += round_brains
                print("=================================================")
                print(f"total current brains:{player_brains}{brain_emoji}")
                print("=================================================")
                if player_brains >= 13:
                    print(f"{player_brains} brains scored! YOU WIN!")
                    break
                computer_turn = True
                while computer_turn == True:
                    computer_brains = computer_turn_func()
                    computer_total_brains += computer_brains
                    print("=============computer turn==========================\n")
                    print(
                        f"computer total brains:{computer_total_brains}{brain_emoji}\n")
                    print("=================================================")
                    if computer_total_brains == 13:
                        print(
                            f"computer wins with {computer_total_brains}{brain_emoji}\n")
                        computer_turn = False
                    else:
                        computer_turn = False
                        break
            else:
                continue
    print("game over")
    if player_brains >= 13:
        print("player wins!")
    elif computer_total_brains >= 13:
        print("computer won")
elif choice == "3":
    print(
        f" Final scores\nplayer:{player_brains}{brain_emoji}\n computer:{computer_total_brains}{brain_emoji}\n")
    print(f"{zombie_emoji}Goodbye{dice_emoji}")
