from functions.art import footprints_emoji, brain_emoji, blast_emoji, dice_emoji, zombie_emoji
from functions.draw_dice import draw_dice_func
from functions.roll_dice import roll_dice_func
from functions.main_menu import main_menu

drawn_dice = []
player_round_hp = 3
#player_database = {}
# main_menu()
#user_name = input("Please enter your name\n")
user_choice = main_menu()
user_brains = 0

if user_choice == "1":
    should_continue = True
    while should_continue == True:
        # draw_dice_func(drawn_dice)
        # rolled_result = roll_dice_func(drawn_dice)
        if player_round_hp <= 0:
            print("You got blasted! turn over!")
            break
        else:
            print(
                f"Press 1 roll again {dice_emoji}or 2 to keep brains{brain_emoji} ")
            round_continue = input("Please make a choice\n")
            if round_continue == 1:
                continue
            elif round_continue == 2:
                user_brains += 1
                break
elif user_choice == "2":
    print("thanks for playing zombie dice!\n Goodbye")
