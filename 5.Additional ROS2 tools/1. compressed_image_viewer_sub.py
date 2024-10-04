#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import cv2
from cv_bridge import CvBridge

from sensor_msgs.msg import CompressedImage



class CompressedImageSubscriber(Node):
    def __init__(self, topic):
        super().__init__("image_view_sub_node")
        qos_policy = rclpy.qos.QoSProfile(reliability=rclpy.qos.ReliabilityPolicy.BEST_EFFORT,
                                          history=rclpy.qos.HistoryPolicy.KEEP_LAST,
                                          depth=1)
        self.sub = self.create_subscription(CompressedImage, topic,
                                            self.subscriber_callback, qos_profile=qos_policy)
        self.received_msg = False

    def subscriber_callback(self, image_msg):
        if self.received_msg == False:
            print("Image Data Received... Displaying Image in CV2 window")
            self.received_msg = True

        image = CvBridge().compressed_imgmsg_to_cv2(image_msg, desired_encoding="passthrough")
        cv2.imshow("CompressedImage", image)
        cv2.waitKey(1)


def main():
    rclpy.init()

    topic_name = input("What is the topic name: ")

    print("Waiting for data to be publisher over topic...")

    my_sub = CompressedImageSubscriber(topic_name)

    try:
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        my_sub.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()
