import random
from ascii_art import blackjack_logo

cards_dictionary = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}

def deal_card(card):
    """Add a random new card value to the card list."""
    card.append(random.choice(list(cards_dictionary.keys())))

def calculate_score(cards_in_hand):
    """
    Calculate the total score of the cards in hand.

    If there is at least one 'Ace' in the hand and the total score exceeds 21,
    the value of an Ace will be reduced from 11 to 1.

    :param cards_in_hand: List of card names (strings) in the hand.
    :return: The calculated score as an integer.
    """

    score = sum(cards_dictionary[card] for card in cards_in_hand)
    ace_count = cards_in_hand.count("Ace")
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def show_hand(player_cards, player_score, com_cards, com_score, reveal_all = False):
    """
    Print the player's and computer's cards.

    When reveal_all is False, only the player's cards and score are shown along with the computer's first card.
    When reveal_all is True, both the player's and computer's full hands are displayed.

    :param reveal_all: Boolean flag to indicate whether to reveal the computer's full hand.
    """

    if reveal_all:
        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {com_cards}, final score: {com_score}")
    else:
        print(f"Your cards:{player_cards}, current score: {player_score}")
        print(f"Computer first card: {com_cards[0]}")

def check_game_over(player_cards, com_cards):
    """
    Check if the game should end based on the player's hand.

    Game-ending conditions include:
      - BlackJack (score equals 21)
      - Bust (score exceeds 21)
      - Five-Card Charlie (five cards in hand without busting)

    :return: True if the game should end, False otherwise.
    """

    player_score = calculate_score(player_cards)
    com_score = calculate_score(com_cards)
    if player_score == 21:
        show_hand(player_cards, player_score, com_cards, com_score, reveal_all=True)
        print("Black Jack! You Win!")
        return True
    if player_score > 21:
        show_hand(player_cards, player_score, com_cards, com_score, reveal_all=True)
        print("Bust! You lose.")
        return True
    if len(player_cards) == 5 and player_score <= 21:
        show_hand(player_cards, player_score, com_cards, com_score, reveal_all=True)
        print("You've got Five Card Charlie! You Win!")
        return True
    return False

def computer_turn(com_cards):
    """If player doesn't bust and doesn't want to hit, then change to computer's turn.

    If the computer's total score is less than 17, then it must keep dealing.
    """
    while calculate_score(com_cards) < 17 and len(com_cards) < 5:
        deal_card(com_cards)

def final_comparison(player_cards, com_cards):
    """
    Compare the final scores of the player and the computer and print the result.

    Displays both the player's and the computer's final hands and scores,
    then determines the outcome based on the rules:
      - If the computer busts, the player wins.
      - If the computer has a BlackJack, the player loses.
      - Otherwise, the higher score wins. In case of a tie, it's a "push".

    :param player_cards: List of player's cards.
    :param com_cards: List of computer's cards.
    """

    player_score = calculate_score(player_cards)
    com_score = calculate_score(com_cards)
    show_hand(player_cards, player_score, com_cards, com_score, reveal_all=True)
    if com_score > 21:
        print("Computer busts! You win!")
    elif com_score == 21:
        print("Computer has Black Jack! You lose.")
    else:
        if player_score > com_score:
            print("You win!")
        elif player_score < com_score:
            print("You lose.")
        else:
            print("-- Push --")

def game_play():
    """
    Main game loop for playing multiple rounds of Blackjack.

    Displays the game logo, repeatedly asks users if they want to play,
    initializes the hands for both the player and the computer, manages the game flow
    including player actions, checking game-ending conditions, executing the computer's turn,
    and final score comparison.

    The game loop continues until the player decides not to play another round.
    """

    print(blackjack_logo)
    is_continue = True
    while is_continue:
        player_cards = []
        com_cards = []
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() != "y":
            is_continue = False
            break

        for _ in range(2):
            deal_card(player_cards)
            deal_card(com_cards)

        game_over = False
        player_score = calculate_score(player_cards)
        show_hand(player_cards, player_score, com_cards, calculate_score(com_cards), reveal_all=False)

        while not game_over:
            if check_game_over(player_cards, com_cards):
                game_over = True
                break
            hit_or_not = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hit_or_not == "y":
                deal_card(player_cards)
                player_score = calculate_score(player_cards)
                show_hand(player_cards, player_score, com_cards, calculate_score(com_cards), reveal_all=False)
            else:
                game_over = True
                computer_turn(com_cards)
                final_comparison(player_cards, com_cards)

        print("--- ROUND OVER ---\n")

game_play()