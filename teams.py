#!/bin/python3

from random import choice

# Creating a list of global players which will be obtained from the "players.txt" and will be saved in a "players" array.
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players:', players)

# Creating the Teams for sorting
teamA = []
teamB = []

# loop until there are no players left in the global players list.
while len(players) > 0:
  
  # Choosing a random player for team A
  playerA = choice(players)
  teamA.append(playerA)

  # Remove the player from the players list so it does not repeat. 
  players.remove(playerA)
  
  # Break the loop if their are no players left
  if players == []: 
    break
  
  # Choosing a random player for team B
  playerB = choice(players)
  teamB.append(playerB)

  # Remove the player from the players list so it does not repeat. 
  players.remove(playerB)

# Printing the teams that were sorted. 
print('\nHere are your teams:\n')
print("Team A is: ", teamA)
print("Team B is: ", teamB)