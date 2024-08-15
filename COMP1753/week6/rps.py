MIN_BALANCE = 10
MAX_BALANCE = 100
BET = 5

ROCK = 1
SCISSOR = 2
PAPER = 3

import random as comp

def enter_balance():
    balance = float(input(f'Type in the initial balance, it should be from {MIN_BALANCE} to {MAX_BALANCE}: '))
    while balance < MIN_BALANCE or balance > MAX_BALANCE:
        print('Impossible Selection!')
        if balance < MIN_BALANCE: print(f'The initial balance should be above ${MIN_BALANCE}!')
        elif balance > MAX_BALANCE: print(f'The initial balance should not be above ${MAX_BALANCE}!')
        balance = float(input('Type in the initial balance again: '))
    return balance
    
def random_rsp():
    comp_choice = comp.randint(1,3)
    if comp_choice == 1: return ROCK
    if comp_choice == 2: return SCISSOR
    if comp_choice == 3: return PAPER

def get_rsp():
    print(f'[{ROCK}] as Rock, [{SCISSOR}] as Scissor, [{PAPER}] as Paper.')
    user_choice = int(input('Type in your choice: '))
    while not 1 <= user_choice <= 3:
        print('Impossible Selection!')
        user_choice = int(input('Type in your choice again: '))
    if user_choice == 1: return ROCK
    if user_choice == 2: return SCISSOR
    if user_choice == 3: return PAPER
    # TODO: get user input for rock, paper, or scissors.
    # Validate input until user enters a valid choice (rock, paper, or scissors) and return it

def compare_result(comp_choice, user_choice):
    # TODO: print the computer's choice and the user's choice
    if comp_choice == 1: print('COMP pick Rock!')
    if comp_choice == 2: print('COMP pick Scissor!')
    if comp_choice == 3: print('COMP pick Paper!')

    if user_choice == 1: print('You pick Rock!')
    if user_choice == 2: print('You pick Scissor!')
    if user_choice == 3: print('You pick Paper!')
    
    # Compare user choice and computer choice folowing the rule: rock > scissors > paper > rock
    if comp_choice == user_choice:
        result = "tie"
    elif user_choice == ROCK:
        if comp_choice == PAPER: result = "lose"
        elif comp_choice == SCISSOR: result = "win"
    elif user_choice == PAPER:
        if comp_choice == ROCK: result = "win"
        elif comp_choice == SCISSOR: result = "lose"
    elif user_choice == SCISSOR:
        if comp_choice == ROCK: result = "lose"
        elif comp_choice == PAPER: result = "win"

    # Print the result of the game for user (win, lose, or tie)
    print(f'It is a {result} for player!')
    # Return the result of the game ('win', 'lose', or 'tie')
    return result

def update_balance(result, balance):
    # TODO: update the user's balance based on the result of the game
    # If the user wins, add $5 to their balance
    if result in ("win"):
        balance += BET
    # If the user loses, subtract $5 from their balance
    elif result in ("lose"):
        balance += -BET
    # If the user ties, do not change their balance
    elif result in ("tie"):
        balance += 0
    # Show user's new balance and return it
    print(f'Your new balance: ${balance}')
    return balance

def is_continue(balance):
    # Balance Failsafe
    if balance <= 0:
        print('Sorry! You have spent all your money on gambling!')
        print('We have to end this program abruptly to avoid any further consequences!')
        return False

    # TODO: ask the user if they want to play again
    replay = input('Play again? [y/n] ').lower()
    while replay not in ("y", "yes", "n", "no"):
        print('Impossible Selection!')
        replay = input('Play again? [y/n] ').lower()
    # return True if the user enters "y" or "yes" and False otherwise
    if replay in ("y", "yes"): return True
    elif replay in ("n", "no"): return False

#### MAIN PROGRAM ####
balance = enter_balance()
playing = True
while playing:
    comp_choice = random_rsp()
    user_choice = get_rsp()
    result = compare_result(comp_choice, user_choice)
    balance = update_balance(result, balance)
    playing = is_continue(balance)