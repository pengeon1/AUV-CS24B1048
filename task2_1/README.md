# CS24B1048 - Piyush Mishra
1. Create a pipeline to show the camera output with the help of OpenCV.

Here is my approach:
1. A publisher node that takes the camera video data using opencv puts it through the ros_bridge converter and then publishes it to a rostopic.
2. A subscriber node of this rostopic then uses the ros_bridge again to convert it to the form that opencv can display it using its GUI.

I had multiple problems in enabling permission to allow my VitualMachine to access my camera and even after that opencv had problems in accessing the camera. With some troubleshooting ideas from the internet I was able to resolve it.
