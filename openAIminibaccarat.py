import random

def simulate_mini_baccarat():
    shoe = initialize_shoe()
    outcome = ''
    player_wins = 0
    banker_wins = 0
    ties = 0
    
    while len(shoe) >= 6:
        player_cards, banker_cards = draw_initial_cards(shoe)
        winner = determine_winner(player_cards, banker_cards)
        outcome += winner
        if winner == 'P':
            player_wins += 1
        elif winner == 'B':
            banker_wins += 1
        elif winner == 'T':
            ties += 1
    
    total_games = player_wins + banker_wins + ties
    player_win_percentage = (player_wins / total_games) * 100
    banker_win_percentage = (banker_wins / total_games) * 100
    tie_percentage = (ties / total_games) * 100
    
    print("Outcome:")
    print(outcome)
    print()
    print("Player Win Percentage:", player_win_percentage)
    print("Banker Win Percentage:", banker_win_percentage)
    print("Tie Percentage:", tie_percentage)

def initialize_shoe():
    cards = ['0', '0', '0', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    shoe = cards * 4 * 6  # 6 decks in the shoe
    random.shuffle(shoe)
    return shoe

def draw_initial_cards(shoe):
    player_cards = []
    banker_cards = []
    for _ in range(2):
        player_cards.append(shoe.pop())
        banker_cards.append(shoe.pop())
    return player_cards, banker_cards

def determine_winner(player_cards, banker_cards):
    player_total = sum_card_values(player_cards)
    banker_total = sum_card_values(banker_cards)
    
    if player_total == 8 and banker_total == 8:
        return 'T'  # No further cards are drawn
    
    if player_total == 9 and banker_total == 9:
        return 'T' #No further cards drawn
        
    if player_total == 7 and banker_total == 7:
        return 'T'  # No further cards are drawn
        
    if player_total == 6 and banker_total == 6:
        return 'T'  # No further cards are drawn
    
    if player_total <= 5:
        player_total += draw_card(player_cards)
    
    if banker_total <= 5:
        if player_total >= 6:
            banker_total += draw_card(banker_cards)
        elif player_total <= 5:
            if banker_total == 3:
                if draw_card(player_cards) == 8:
                    return 'B'
                else:
                    banker_total += draw_card(banker_cards)
            elif banker_total == 4:
                if draw_card(player_cards) in [2, 3, 4, 5, 6, 7]:
                    return 'B'
                else:
                    banker_total += draw_card(banker_cards)
            elif banker_total == 5:
                if draw_card(player_cards) in [4, 5, 6, 7]:
                    return 'B'
                else:
                    banker_total += draw_card(banker_cards)
            elif banker_total == 6:
                if draw_card(player_cards) in [6, 7]:
                    return 'B'
                else:
                    banker_total += draw_card(banker_cards)
    
    if player_total > banker_total:
        return 'P'
    elif banker_total > player_total:
        return 'B'
    else:
        return 'T'

def draw_card(cards):
    card = cards.pop()
    return int(card) if card != '0' else 10

def sum_card_values(cards):
    total = 0
    for card in cards:
        total += int(card) if card != '0' else 10
    return total % 10

# Simulate the game
simulate_mini_baccarat()
