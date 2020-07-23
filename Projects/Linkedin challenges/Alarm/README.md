## Set an alarm challenge

### Desciption
The aim of this challenge is to write a function that sets an alarm at a given time and both plays a sound and prints a message when the timer is up.

### Solution
To solve this challenge I've used the time and the winsound modules. As an added feature the sound keeps playing until Enter is pressed. Works in Windows.

### Usage
alarm(timer_in_seconds,wav_name,message) plays wav_name and prints message after a number of seconds equal to timer_in_seconds. wav_name must be the name of a .wav file.