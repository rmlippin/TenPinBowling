# TenPinBowling
Given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game.


**American Ten-Pin Bowling Rules**
- The game consists of 10 frames
- In each frame, the player has two opportunities to knock down all the pins. The score for the frame is the number of pins knocked down, plus the bonuses for strikes and spares.
- A spare is when the player knocks down all 10 pins in two tries. The bonus for that frame is the number of pins knocked down by the next roll.
- A strike is when the player knocks down all 10 pins on their first try. The bonus for that frame is the value of the next two balls rolled.
- In the tenth frame, a player who rolls a strike or spare is allowed to roll the extra balls to complete the frame. However, no more than three balls can be rolled in the tenth frame.


**Program Assumptions**
- The given rolls are valid.
- The number of rolls and the number of frames in the input are valid.
- No need to check for an intermediate score between frames.
- The game has one player.


**Input Format**
- This program accepts a relative text file path as a cmd argument.
- Each line in the text file represents one roll in the game, and contains the pin numbers for all knocked pins.
- There are no seperators for frames.
- A "gutter ball" is represented by a blank line.


**Test Cases**
- To run a test case on a Windows machine with Python3 installed, use the following format:
  - `py CalcBowlingScore.py unit-tests\test_3.txt`
- The included test cases have the following expected outputs:
  - test_1: 106
  - test_2: 136
  - test_3: 51
  - test_perfect: 300
  - test_worst: 0
