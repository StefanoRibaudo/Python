## The waiting game challenge

### Desciption
The aim of this challenge is to write a function to play a game. The game should tell you any ammount of time to wait between two Enter key presses. After the first key press a timer should start and stop at the second key press. The code shows the difference between the target time and the achieved time.

### Solution
The solution involves the time module. time.time() outputs the time when called and one can easily call time.time() after input() to record the time at the key press.

### Usage
waiting_game() starts the game. Instructions are shown inside the console.