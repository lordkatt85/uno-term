import gamelogic.cards
import gamelogic.players

#for cards.py
#this is for you le

#for players.py
n = 2 #number of players
Player_list = ['PLayer1', 'Player2', 'Player3', 'Player4']

for i in range(n):
    Player_list[i] = gamelogic.players.Player("suren")
    Player_list[i].draw_initial_cards(gamelogic.cards.deck)

print(len(Player_list[0].hand))