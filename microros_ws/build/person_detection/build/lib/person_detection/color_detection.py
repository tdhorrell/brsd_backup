import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import time
import numpy as np
import cv2
import urllib.request

url = 'http://192.168.0.137/cam-hi.jpg'
cv2.namedWindow("ESP32 Feed", cv2.WINDOW_AUTOSIZE)

class PersonDetectionNode(Node):
    def __init__(self):
        super().__init__('color_detector')

        self.publisher_ = self.create_publisher(Bool, 'person_detector', 10)

        self.startTime = time.time()
        self.detectionCount = 0
        self.frameCount = 0

        timer = .1
        self.timer = self.create_timer(timer, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Attempting to connect to URL")
        imgFromURL = urllib.request.urlopen(url)
        npImg = np.array(bytearray(imgFromURL.read()), dtype=np.uint8)
        frame = cv2.imdecode(npImg, -1)

        if self.isColorDetected(frame):
            self.detectionCount += 1
            self.get_logger().info("Blue Detected")
        else:
            self.get_logger().info("No Blue Detected")
        
        self.frameCount += 1
        cv2.imshow("ESP32 Feed", frame)

        if time.time() - self.startTime >= 5:
            # Calculate the detection rate over the past 5 seconds
            detection_rate = self.detectionCount / self.frameCount
            msg = Bool()
            msg.data = detection_rate >= .3

            if msg.data:
                self.get_logger().info("Majority Blue Detected")
            else:
                self.get_logger().info("Not Majority Blue")
            
            self.publisher_.publish(msg)
            
            # Reset for the next 5 seconds
            self.detectionCount = 0
            self.frameCount = 0
            self.start_time = time.time()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            rclpy.shutdown()

    def isColorDetected(self, frame, pixelThreshold=0.2):
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range of blue color in HSV
        lower = np.array([75, 75, 23])
        upper = np.array([110, 255, 230])

        
        hsv_blurred = cv2.GaussianBlur(hsv, (11, 11), 0)

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv_blurred, lower, upper)

        # Apply morphological operations to remove noise
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((20, 20), np.uint8))


        # Removes small components that is mainly noise
        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
        for i in range(1, num_labels):
            if stats[i, cv2.CC_STAT_AREA] < 500:  # Adjust the area threshold as needed
                mask[labels == i] = 0

        pixelCount = np.sum(mask > 0)
        total_pixel_count = mask.size
        pixelPercentage = pixelCount / total_pixel_count

        cv2.imshow("Masked Feed", mask)

        return pixelPercentage >= pixelThreshold

def main(args=None):
    rclpy.init(args=args)
    node = PersonDetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()