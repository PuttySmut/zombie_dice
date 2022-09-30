from functions.art import zombie_emoji, dice_emoji, running_man_emoji


def main_menu():
    print("==============ZOMBIE DICE==============")
    print(f"{running_man_emoji}{zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}{zombie_emoji}{dice_emoji}{running_man_emoji}")
    print("   1)play zombie dice")
    print("   2)exit zombie dice")
    user_choice = input("Please make a choice 1 or 2")
    return user_choice


# main_menu()
