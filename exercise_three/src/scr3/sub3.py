#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from exercise_three.msg import custom_msg 

def subscriber():
	sub = rospy.Subscriber('raw_data',String,callback_function)
	pub = rospy.publisher('user_info', custom_msg, queue_size=10)
	rate = rospy.Rate(1)
	rospy.spin()
def callback_function(message):
	splitted_data= message.data.split(",")
	name= splitted_data[0].split()
	age= splitted_data[1].split()
	height= splitted_data[2].split()
	n_age=int(age[1])
	n_height=int(height[1])
	msg_to_publish=custom_msg()
	msg_to_publish.name=name
	msg_to_publish.age=n_age
	msg_to_publish.height=n_height
	pub.publish(msg_to_publish)
	rate = rospy.Rate(1)
	rospy.loginfo(msg_to_publish.name)
	rospy.loginfo(msg_to_publish.age)
	rospy.loginfo(msg_to_publish.height)
	
if __name__ == "__main__":
   rospy.init_node('data_processing')
   subscriber()
