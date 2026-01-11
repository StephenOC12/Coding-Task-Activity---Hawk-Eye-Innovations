from Games.higher_lower import play_higher_lower, play_higher_lower_vs_computer

if __name__ == "__main__":

    started_state = False
    #While loop used to restarts after games
    while started_state == False:
        game_selection = input("Would you like to play higher/lower(1) or quit(q): ").strip().lower()

        #Higher/lower selected
        if game_selection == "1":
            mode_selection = input("By yourself(1), against the computer(2) or quit(q): ").strip()
            #Single player mode
            if mode_selection == "1":
                seed_input = input("Enter a seed or just enter to continue: ").strip()
                seed = int(seed_input) if seed_input else None
                started_state = True
                play_higher_lower(seed=seed)
            
            #Vs computer mode
            elif mode_selection == "2":
                difficulty = input("Easy, Medium or Hard difficulty: ").strip().lower()
                #Ensuring valid input
                while difficulty not in ("easy", "medium", "hard"):
                    difficulty = input(
                        "Please enter a valid difficulty (easy / medium / hard): "
                    ).strip().lower()
                
                started_state = True
                play_higher_lower_vs_computer(difficulty=difficulty)

            #Quit
            elif mode_selection == "q":
                break

            #Ensuring valid input
            else:
                print("invalid option, pick (1/2)")
                continue
                
        elif game_selection == "q":
            break
        else:
            print("Please enter a valid option (1/q)")
            started_state = False
            continue

        replay = input("Would you like to play again (yes/no): ").strip().lower()
        if replay == "yes":
            started_state = False
