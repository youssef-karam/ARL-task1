#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def subscriber():
	sub = rospy.Subscriber('raw_data',String,callback_function)
	
	rospy.spin()
def callback_function(message):
	splitted_data= message.data.split(",")
	name= splitted_data[0].split()
	age= splitted_data[1].split()
	height= splitted_data[2].split()
	n_age=int(age[1])
	n_height=int(height[1])
	rospy.loginfo(name[1])
	rospy.loginfo(n_age)
	rospy.loginfo(n_height)
	
if __name__ == "__main__":
   rospy.init_node('data_processing')
   subscriber()
