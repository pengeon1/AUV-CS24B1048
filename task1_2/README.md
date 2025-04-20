# CS24B1048 - Piyush Mishra
2. Create a publisher node that sends multiples of 2. A subscriber node receives it, multiplies it by 10, and publishes the result to a new topic. A second subscriber node listens to this second topic, adds 5 to the number, and prints the final result.

Here is my approach:
1. A node "number_publisher" that constantly publishe multiples of 2 by using a while loop at a rate of 1 Hz to the rostopic "numbers".
2. A subriscriber node "number_processor" subscribed to "numbers" reads the data and multiplies 10 to it and publishes it to the topic "processed_numbers".
3. Another subscriber node "final_node" reads the data in "processed_numbers", adds 5 to it and finally prints them.

The only problem I faced was that the "number_processor" was not able to subscribe to "numbers"... later found a typo that was causing this issue.
