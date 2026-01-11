Coding Task Activity - Hawk-Eye Innovations

This project entails of a higher or lower card game implemented in Python. There are multiple different modes, you can play alone, with a friend who uses the same seed or against the computer with a range of difficulties.

Features:
- Single Player: Play individually and get aim to get a long streak through continued correct answers
- Seeded Mode: Play with a friend on another computer or on different sessions by entering in the same seed. You will each get  the same shuffle and ordering of the cards.
- Mode vs the computer: Play against an AI with multiple different difficulties
    - Easy: Random guessing approach
    - Medium: Simple strategy based on the card rank
    - Hard: More strategic difficulty that considers what cards remain in the deck

Requirements:
- Python 3.8 or higher
- Docker

Steps to run the Code:

1. Clone the repository:
git clone <your-repo-url>
cd Higher_Lower_Game

2. Run the game (2 options)
2a. 
python main.py

2b.
docker build -t card-game .
docker run -it card-game

3. How to play the game
Follow the commands on screen

3a. 1 to play higher or lower or q to quit
3b. 1 to play by yourself or with a friend using a seed, 2 for against the computer or q to quit

3bi. Enter a seed or just press enter if selected 1
3bii. Enter easy medium or hard

3c. Select higher or lower inside of the game


Why I made certain decisions:

OOP adds modularity and means it could be reusable/extended for future added games. Making the cards immutable prevents bugs related to cards changing when not wanted. Abstracting the shuffling into different classes allowed for different shuffling in different modes without affecting the Deck class. Creating the ComputerPlayer allowed for an interactive game to be played without requiring a second player. A range of tests, as well as a test plan their results and any further changes are listed inside of the Test_File.xlsx.

Areas for future improvement:

Implementing additional card games could be made easier with the OOP implementation. In additon for card games like blackjack or poker the use of multiple decks could be beneficial to avoid card counting.

In addition, connecting this to a web app and using the seed based game for online play could be another potential addition. 

