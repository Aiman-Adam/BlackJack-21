import random as r
import os
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_arr = []
    pc_arr = []

    clearConsole()
    start = input("Welcome to blackjack, would you like to start?:\n").lower()
    if start == "y":
        clearConsole()
        run = True
        while run:
            def totalforpc():       
                total = 0
                for i in pc_arr:
                    total += i
                return total

            def totalforuser():       
                total = 0
                for i in user_arr:
                    total += i
                return total


            user_1card = r.choice(cards)
            user_2card = r.choice(cards)
            user_arr.append(user_1card)
            user_arr.append(user_2card)

            pc_1card = r.choice(cards)
            pc_2card = r.choice(cards)
            pc_arr.append(pc_1card)

            print(f"\nHere is your deck {user_arr} = {totalforuser()}")
            print(f'Here is dealers first card {pc_arr}')
            pc_arr.append(pc_2card)


            def repeating():
                if totalforpc() == 21 or totalforuser() > 21 :
                    clearConsole()
                    print(f"Dealer won \nDealers deck = {pc_arr} = {totalforpc()}\nyour deck = {user_arr} = {totalforuser()}")
                    return "stop"
                elif totalforpc() > 21:
                    clearConsole()
                    print(f"You won \nDealers deck = {pc_arr} = {totalforpc()}\nyour deck = {user_arr} = {totalforuser()}")
                    return "stop"

                elif totalforuser() == 21:
                    clearConsole()
                    print(f"You won \nDealers deck = {pc_arr} = {totalforpc()}\nyour deck = {user_arr} = {totalforuser()}")
                    return "stop"

            hitlogic = True
            if repeating() == "stop":
                hitlogic = False
                run = False
            while hitlogic:
                hit = input(f"\nWould you like to hit or stand? if hit, please type hit, vice versa:\n").lower()
                while hit == "hit":
                    user_3card = r.choice(cards)
                    if user_3card == 11:
                        if totalforpc() + 11 > 21:
                            user_3card = 1
                    user_arr.append(user_3card)
                    clearConsole()
                    print(f'\nDealers first card = {pc_1card}\nyour deck = {user_arr} = {totalforuser()}')
                    repeat = repeating()
                    secrun = True
                    if repeat == "stop":
                        run = False
                        secrun = False
                        break
                    else:
                        secrun = True
                    if secrun:
                        hit = input(f"\nWould you like to hit or stand? if hit, please type hit, vice versa:\n").lower()
                if hit == "stand":
                    clearConsole()
                    while totalforpc() < 17:
                        pc_3card = r.choice(cards)
                        if pc_3card == 11:
                            if totalforpc() + 11 > 21:
                                pc_3card == 1
                        pc_arr.append(pc_3card)
                        totalforpc()

                    if totalforuser() > totalforpc():
                        clearConsole()
                        print(f"You won \nDealers deck = {pc_arr} = {totalforpc()} \nyour deck = {user_arr} = {totalforuser()}")
                        run = False
                    elif totalforpc() > totalforuser():
                        clearConsole()
                        print(f"Dealer won \nDealers deck = {pc_arr} = {totalforpc()}\nyour deck = {user_arr} = {totalforuser()}")
                        run = False
                    else:
                        clearConsole()
                        print(f"Both you and dealer drawn\nDealers deck = {pc_arr} = {totalforpc()}\nyour deck = {user_arr} = {totalforuser()}")
                        run = False
                    hitlogic = False
game()
startover = input("\nWould you like to play again?\n").lower()
while startover == "y":
    game()







