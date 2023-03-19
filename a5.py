# a5.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Junyu Li
# junyul24@uci.edu
# 86676906
"""Module as entry"""
import sys
import ui
import a5gui


def main():
    """Run the mian function."""
    while True:
        ui.menu()
        user_input2 = ui.start()
        if user_input2 == 'L':
            user_lis = ui.path_interact(user_input2)
            user_lis = ui.L_option_interact(user_lis)
            if '-s' in user_lis or '-e' in user_lis:
                user_lis.append(ui.L_rest())
            ui.L_command(user_lis)
        if user_input2 == 'C':
            user_lis = ui.path_interact(user_input2)
            user_lis = ui.C_interact(user_lis)
            ui.C_command(user_lis)
        if user_input2 == 'D':
            user_lis = ui.path_interact(user_input2)
            ui.D_command(user_lis)
        if user_input2 == 'R':
            user_lis = ui.path_interact(user_input2)
            ui.R_command(user_lis)
        if user_input2 == 'O':
            user_lis = ui.path_interact(user_input2)
            ui.O_command(user_lis[1])
        if user_input2 == 'Q':
            sys.exit(0)
        if user_input2 == 'V':
            user_lis = ui.path_interact(user_input2)
            user_input2 = input('Do you want to publish bio '
                                'and post together?(Y/N): ')
            if user_input2 == 'Y':
                ui.publish_together(user_lis[1])
            else:
                print('\n1.Publish a post')
                print('2.Publish a bio')
                user_input3 = input('Please select a number: ')
                if user_input3 == '1':
                    ui.publish_change_post(user_lis[1])
                else:
                    ui.publish_bio(user_lis[1])


if __name__ == '__main__':
    main()  # PDOC, ui
