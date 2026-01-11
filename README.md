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

Object-Oriented Design: Separating the main aspects of the game for Card, Deck, Shuffler, and ComputerPlayer into classes adds modularity and separation of concerns. This will make it easier for any future additions to this code without having to rewrite the main functionalities.

Immutable Cards: Making the cards immutable prevents bugs related to the cards changing suit or rank whilst the game is going on. This is important for one deck but will be really important upon the implementation of multiple decks.

Shuffler Abstraction: Abstracting the shuffling into different classes allowed for separation of the shuffling from the deck, allowing the logic to be completely separate whilst having the benefit of different shuffling in different modes without affecting the Deck class. 

ComputerPlayer AI: Creating the ComputerPlayer allowed for an interactive game to be played without requiring a second player. The range of difficulties in the AI player makes the game more engaging for a range of users, and allows for future extension (probabilistic look for multiple deck card counting)

Testing: A wide range of manual and automated tests ensures that the key components of the game work as intended as well as making sure that the game still does as intended in edge case. The test plan listed inside of the Test_File.xlsx shows the test descriptions, expected and actual results as well as the required changes in the case of a bug found in testing.


Areas for future improvement:

Adding More Card Games: Implementing additional card games could be made easier with the OOP implementation. New games like poker and blackjack could be added without having to change the original logic. In additon for these kinds of games the use of multiple decks could be beneficial to avoid card counting.

Web Integration: In addition, connecting this to a web app could allow for online play. The seed based game could be used for this to allow for fair competitions and not reducing it to pure luck.

Additional Game Features: special cards such as an extra life or additional score given for runs of 5 or 10, etc. could be new fun ways to keep the game fresh. 

