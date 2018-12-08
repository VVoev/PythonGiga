import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def ask_user_to_enter_input():
    print('please enter a word you are looking for')
    userChoise = input()
    return userChoise.lower()


def check_if_word_is_presented_in_dict(userEntered):
    while userEntered != 'EXIT':
        if userEntered in data:
            print(data[userEntered])
        elif len(get_close_matches(userEntered, data.keys())) > 0:
            print('did you mean {word}'.format(
                word=get_close_matches(userEntered, data.keys())[0]))
            yes_or_no = input()
            if yes_or_no.lower() == 'yes':
                res = get_close_matches(userEntered, data.keys())[0]
                print(data[res])
                print('are you looking for another word[yes/no]')
                another = input()
                if another.lower() == 'yes':
                    # Recursive call
                    choise = ask_user_to_enter_input()
                    check_if_word_is_presented_in_dict(choise)
                else:
                    exit()
            else:
                exit()
        else:
            print('The world doesnt exist,Please double check it')
        userEntered = ask_user_to_enter_input()


# INIT PROGRAM
userEntered = ask_user_to_enter_input()
check_if_word_is_presented_in_dict(userEntered)
