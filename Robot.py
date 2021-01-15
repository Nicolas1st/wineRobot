from math import sin, cos
from AI import AI
from Manipulator import Manipulator
import cv2


class Robot:

  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.positions = [[x, y, direction]]
    self.AI = AI('yolov3.weights', 'yolov3.cfg', 0.5)
    self.tool = Manipulator()
    self.direction = direction


  def rotate(angle=None, direction=None):
    if angle is not None:
      self.direction += angle
    elif direciton is not None:
      self.direction = direction
    self.direction %= 360


  def move(distance):
    # always moves in the direction of self.direction
    self.x += distance * cos(self.direction)
    self.y += distance * sin(self.direction)
    self.positions.append([self.x, self.y, direction])


  def move_back(self):
    self.x = self.positions[-1][0]
    self.y = self.positions[-1][1]
    self.direciton = self.positions[-1][2]


  def turn_on_tool(self):
    self.tool.lock()
  

  def turn_off_tool(self):
    self.tool.unlock()


  def take_frame(self):
    # taking one frame of the video stream
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if frame is None:
      raise TypeError("No input was detected from the camera, frame = None")
    camera.release()
    return frame

  
  def identify(self, object_found):
    if object_found == "Person":
      print("Person was found")
    elif object_found == "Bottle":
      print("Bottle was found")
    else:
      print("Nothing was found")


  def search_objects(self):
    for i in range(15):
      frame = self.take_frame()
      frame, object_found, height, width = self.AI.detect_object(frame)
      self.identify(object_found)
      cv2.imshow('frame', frame)
      cv2.waitKey(0)
    

  def determine_object_location(self, target):
    """
    input
      target: "Person", "Bottle"
    return
      distance, direction
    """

    # looking around
    for d_angle in range(360):

      self.direction += d_angle
      self.direction %= 360
      found, width, height, frame = self.AI.detect_object(target)
      cv2.imshow("VideoInput", frame)
      
      print('Found')
      if found:
        distance = height / self.AI.target_heights[target]
        cv2.imshow(target, frame)
        return distance, self.direction


if __name__ == "__main__":
  robot = Robot(0, 0, 0)
  robot.search_objects()
