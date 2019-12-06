import random
import numpy as np
from sys import exit

# The deck is represented by a list
poker_name = ['♦10', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦A', '♦J', '♦K', '♦Q',
              '♣10', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣A', '♣J', '♣K', '♣Q',
              '♥10', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥A', '♥J', '♥K', '♥Q',
              '♠10', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠A', '♠J', '♠K', '♠Q']

# Set the score for each card according to the name in the deck
poker_value = {'♣A': 1, '♥A': 1, '♠A': 1, '♦A': 1, '♦10': 10, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7,
               '♦8': 8, '♦9': 9, '♦J': 10, '♦K': 10, '♦Q': 10,
               '♣10': 10, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9, '♣J': 10, '♣K': 10,
               '♣Q': 10,
               '♥10': 10, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9, '♥J': 10, '♥K': 10,
               '♥Q': 10,
               '♠10': 10, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9, '♠J': 10, '♠K': 10,
               '♠Q': 10}


# It is used to determine whether there is an A in the hand,
# and to choose whether the score of A is 10 or 1 based on the score
Ace = {'♣A', '♥A', '♠A', '♦A'}


def dealing_poker(poker_database):
    # Deal a card and remove it from the deck
    return poker_database.pop(random.randint(0, len(poker_database) - 1))


def score_count(hand_poker):
    # Count the number of CARDS
    score = 0
    have_ace = False
    for k in hand_poker:
        score += poker_value[k]
    for i in hand_poker:
        if i in Ace:
            have_ace = True
            break
        else:
            continue
    if have_ace is True:
        if score + 10 <= 21:
            score += 10
    return score


def judgement(your_score, pc_score):
    # At the end of the card, calculate the number of points on both sides to determine whether to win or lose
    if your_score > 21 and pc_score > 21:
        print('PUSH')
        return np.array([0, 0])
    elif your_score > 21 and pc_score <= 21:
        print('YOU LOSE')
        return np.array([0, 1])
    elif your_score <= 21 and pc_score > 21:
        print('YOU WIN')
        return np.array([1, 0])
    elif your_score <= 21 and pc_score <= 21:
        if your_score < pc_score:
            print('*' * 20)
            print('Your Score:', your_score)
            print("Pc's Score:", pc_score)
            print('*' * 20)
            print('YOU LOSE')
            return np.array([0, 1])
        elif your_score > pc_score:
            print('*' * 20)
            print('Your Score:', your_score)
            print("Pc's Score:", pc_score)
            print('*' * 20)
            print('YOU WIN')
            return np.array([1, 0])
        else:
            print('*' * 20)
            print('Your Score:', your_score)
            print("Pc's Score:", pc_score)
            print('*' * 20)
            print('PUSH')
            return np.array([0, 0])


def hit_or_stand():
    # The player needs to decide whether to call again
    ask_poker = input('Would You Hit?(Y/N)>>:')
    if ask_poker.upper() == 'Y':
        return dealing_poker(poker_database)
    elif ask_poker.upper() == 'N':
        print('You stand')
        return False
    else:
        print('Wrong input, please input Y/y or N/n!>>')
        return hit_or_stand()


def continue_or_quit():
    # At the end of each round, determine whether to continue with the next round of the game.
    # When the number of CARDS in the deck is insufficient, automatically stop the game
    next_round = input('Would you like start next round?(Y/N)>>')
    if next_round.upper() == 'Y':
        if len(poker_database) < 10:
            print('The left pokers is not enough')
            input('Game Over')
            exit(1)
        else:
            return True
    elif next_round.upper() == 'N':
        input('Game Over')
        exit(1)
    else:
        print('Wrong Input, Please Try One More Time!')
        continue_or_quit()


def start_dealing(poker_database):
    # At the beginning, two CARDS are automatically dealt to the player and the computer
    return [poker_database.pop(random.randint(0, len(poker_database) - 1)),
            poker_database.pop(random.randint(0, len(poker_database) - 1))]


def one_round(poker_database):
    # A one-round game
    you_get = start_dealing(poker_database)
    pc_get = start_dealing(poker_database)
    print(f'Your hand poker:{you_get[0]} , {you_get[1]}')
    print(f'PC\'s hand poker:{pc_get[0]} , ?\n')
    your_hand_poker.extend(you_get)
    pc_hand_poker.extend(pc_get)
    score = np.array([score_count(your_hand_poker), score_count(pc_hand_poker)])
    if score[0] == 21 or score[1] == 21:
        print('BlackJack')
        return judgement(score[0], score[1])
    else:
        while score[0] <= 21:
            get_new_poker = hit_or_stand()
            if get_new_poker is not False:
                your_hand_poker.append(get_new_poker)
                print(f'You Hand Poker:{your_hand_poker}')
                score[0] = score_count(your_hand_poker)
                if score[0] > 21:
                    print('You Bust')
                    print(f'PC\'s Hand Poker:{pc_hand_poker}')
                    return judgement(score[0], score[1])
                else:
                    continue
            elif get_new_poker is False:
                while score[1] < score[0]:
                    pc_ask_poker = dealing_poker(poker_database)
                    pc_hand_poker.append(pc_ask_poker)
                    pc_score = score_count(pc_hand_poker)
                    score[1] = pc_score
                print(f'PC final hand poker:{pc_hand_poker}')
                return judgement(score[0], score[1])
                break
            else:
                continue


if __name__ == '__main__':
    poker_deck = 1  # There are several CARDS to play
    poker_database = poker_name * poker_deck  # The resulting deck
    total_score = np.array([0, 0])  # The scoreboard for the total score
    Round = 1
    while len(poker_database) > 10:
        your_hand_poker = []
        pc_hand_poker = []
        #  input('Start Dealing, good luck...<<Enter>>\n')
        print('Start Dealing, good luck...\n')
        print(f'Round {Round}:')
        print('.' * 60)
        score = one_round(poker_database)
        total_score += score
        print(f'Total score is:{total_score[0]}:{total_score[1]}')
        Round += 1
        continue_or_quit()
