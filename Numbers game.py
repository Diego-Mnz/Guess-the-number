import random

attemps_list = []

def show_score():
    if not attemps_list:
        print("There is currently no high score,"
              'it\'s yours for the taking!')
        
    else:
        print(f'The current High Score is'
              f'{min(attemps_list)} attempts')    
        
def start_game():
    attempts = 0
    rand_num = random.randint(1, 20)
    print('Hello bon ami! Welcome to the magical number guessing game')
    player_name = input("List your name")
    lets_play = input(
        f'Hi {player_name}, how about a game?'
        f'the guessing  game (Enter yes/no):')
    
    if lets_play.lower() != 'yes':
        print('See ya next time')
        exit()
    else:
        show_score()
        
    while lets_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 20: ')) 
            if guess < 1 or guess > 20:
                raise ValueError(
                    "please guess a number within 1 and 20")
            
            attempts += 1
            attemps_list.append(attempts)
            
            if guess == rand_num:    
                print('Nice work')
                print(f'it only took you {attempts} attempts')
                lets_play = input(
                    'Ready for the next round? (Enter yes or no): ')
                if lets_play.lower() != 'yes':
                    print("Maybe next time")
                    break               
                else:
                    attempts = 0
                    rand_num = random.randint(1, 20)
                    show_score()
                    continue
    
            else:
                if guess > rand_num:
                    print("A little to high")
                elif guess < rand_num:
                    print('Too low')
        
        except ValueError as err:
            print('Oh no!, that is not a valid number. Try again....')
            print(err)
    
if __name__ == '__main__':
    start_game()     