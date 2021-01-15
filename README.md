# wineRobot

Robot using computer vision powered by the YOLO Neural Network.
The robot is capable of recongnizing and measuring distance up to the following objects:
  1) Human;
  2) Bottle.


The robot can be controlled via an api.
The api can be accessed via the web page.

To run the program run the commands:
  pip3 install -r requirements.txt
  download cfg and weihths from https://pjreddie.com/darknet/yolo/
  mv cfg weights ./app
  cd ./app
  mv *.weights yolov3.weights
  mv *.cfg yolov3.cfg
  python3 app.py
  
Then follow the link in the terminal.
Making an order will cause the window to pop with the access to your webcam
Pressing any key will cause the webcam to take a new frame in.

To stop the application from running fill in the following field in the form or
let the program to take the 15 frames specified in the source code
