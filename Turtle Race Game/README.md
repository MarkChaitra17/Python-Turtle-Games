🐢 Turtle Race\
A fun, interactive Python Turtle game where you bet on turtles and watch them race to the finish line!\
Try your luck, manage your winnings, and see if your favorite turtle crosses the finish line first.\

🎯 Game Objective\
Bet $10 on one of three turtles — Black, Red, or Orange — and watch them race across the screen.\
If your chosen turtle wins, you earn $40!\
Your balance is automatically saved between sessions using a simple CSV file.\

🎮 Gameplay Instructions\
🖱️ Controls\
Action &nbsp;&nbsp;How to Perform\
Place:   Bet	Click on one of the turtles before the race starts\
Start:   Race	Click the Start button\
Reset:   Race	Click the Reset button after a race\
Close:  Game	Closing the window automatically saves your money balance\

💰 Betting Rules\
Each race costs $10 to enter.\
Winning a race rewards $40.\
Your current balance is displayed on the screen.\
Balances are saved in money_val.csv between sessions.\

🧠 Game Logic Overview\
Three turtles (Black, Red, Orange) start from the same position.\
Each turtle moves forward by a random amount per update cycle.\
The first turtle to cross the finish line wins.\
The game uses:\
Mouse events for clicking buttons and placing bets\
CSV file I/O to store and load the player’s money\
Random module for unpredictable movement\
Turtle graphics for visuals and interaction\

🧑‍💻 Author\
Mark Chaitra
