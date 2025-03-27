# Rock Paper Scissors
import os

while True:
    

    player_1 = input('player_1: pedra, papel ou tesoura? ')
    player_2 = input('player_2:pedra, papel ou tesoura? ')
    os.system('clear')
    if player_1 == 'pedra' and player_2 == 'tesoura':
        print(f'{player_1} x {player_2}: jogador 1 venceu!')
    elif player_1 == 'tesoura' and player_2 == 'papel':
        print(f'{player_1} x {player_2}: jogador 1 venceu!')
    elif player_1 == 'papel' and player_2 == 'pedra':
        print(f'{player_1} x {player_2}: jogador 1 venceu!')
    else:
        print(f'{player_1} x {player_2}: jogador 2 venceu!')
    
    if player_1 == 'sair' or player_2 == 'sair':
        break

