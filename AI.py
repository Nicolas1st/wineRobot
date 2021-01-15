import cv2
import numpy as np


class AI:

  """AI tailored for detecting people and bottles on images
  based on the YOLO algorithm"""

  def __init__(self, weight_file_name, config_file_name, confidence):
    self.NeuralNetwork = cv2.dnn.readNet(weight_file_name, config_file_name)
    self.output_layers = [self.NeuralNetwork.getLayerNames()[i[0] - 1] for i in self.NeuralNetwork.getUnconnectedOutLayers()]
    self.targets = {0: "Person", 39: "Bottle"}
    self.target_heights = {0: 800, 39: 120}
    self.confidence_level = confidence


  # def take_frame(self):
  #   # taking one frame of the video stream
  #   camera = cv2.VideoCapture(0)
  #   ret, frame = camera.read()
  #   if frame is None:
  #     raise TypeError("No input was detected from the camera, frame = None")
  #   camera.release()
  #   return frame


  def detect_object(self, frame):

    """
    input
      target: "Person" or "Bottle"
    return 
      True if found else False
      widtn and height of the bounding box
      The frame
    """

    frame_height, frame_width, _ = frame.shape

    # preparing the frame for the Neural Network
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    self.NeuralNetwork.setInput(blob)
    output_neurons = self.NeuralNetwork.forward(self.output_layers)
    
    for neuron in output_neurons:
      for output_params in neuron:

        scores = output_params[5:]
        object_detected = np.argmax(scores)
        confidence = scores[object_detected]

        if confidence >= self.confidence_level and object_detected in self.targets:

          # parameters of the bounding box
          width = int(output_params[2] * frame_width)
          height = int(output_params[3] * frame_height)
          center_x = int(output_params[0] * frame_width)
          center_y = int(output_params[1] * frame_height)
         

          # w, h = int(det[2]*wT), int(det[3]*hT)
          # x, y = int((det[0]*wT) -w/2), int(det[1]*hT -h/2)


          upper_left = (center_x - width // 2, center_y - height // 2)
          lower_right = (center_x + width // 2, center_y + height // 2)

          cv2.rectangle(frame, pt1=lower_right, pt2=upper_left, color=(0, 255, 0), thickness=2)
          cv2.putText(frame, f'{self.targets[object_detected]} {height / self.target_heights[object_detected]}cm', upper_left, cv2.FONT_HERSHEY_SIMPLEX, 1.7, (200, 255, 255), 2, cv2.LINE_AA)

          # return True, height, width, frame
          return frame, self.targets[object_detected], height, width

    return frame, False, None, None


if __name__ == "__main__":
  ai = AI('yolov3.weights', 'yolov3.cfg', 0.5) # the determine_object_location method won't work here because the robot class is not imported
  image = cv2.imread('image2.jpg')

  print(ai.detect_object(image))
