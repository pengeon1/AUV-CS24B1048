# CS24B1048 - Piyush Mishra
Here is my approach:
1. Keep a publisher to publish the data recieved from the sender rosnode to the reciever rosnode.
2. Subscribe the rosnodes to the same rostopic.
3. At first get the name of the user and use that to identify between the two.
4. Use a keyword like "exit" to exit the chat.

Some problems I faced were:
1. I was confused as to why the question said to keep them in the same rosnode (it didn't make sense to read the data and publish it in the same place), so I made two rosnodes (1 for each member to chat).
2. I had multiple errors while trying to run it, but with the help of internet I was able to resolve them.
