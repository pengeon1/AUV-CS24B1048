# CS24B1048 - Piyush Mishra
3. Create a publisher node where the user enters commands like "forward", "turn left" etc and the subscriber should print the position of the bot(x,y, facing direction, etc). The position data should be communicated through a custom message called "bot_pose". Assume bot starts from (0,0) and moves in the cartesian plane. Note: Extra points for simulating bot movement with a state machine.

Here is my approach:
1. Keep 2 states - "moving" and "idle
2. Under "moving" state, the bot moves 1 step/sec in the direction it is facing. Under "idle" state, there is no change in the position.
3. A subscriber node takes input from the user and publishes it and the subscriber node takes this input and calculates the position and direction and prints all these data.

Problems faced:
1. I had failed attempts to download python-statemachine
2. Also, I wasn't able to understand how the library works and had many errors while running it, so finally I manually coded the states.
