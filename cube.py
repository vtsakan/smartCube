#!/usr/bin/python
import smbus
import math
import web
import socket
import sys

import os
#Date and time module
import time
#Music import
from pygame import mixer


# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

gyro_scale = 131.0
accel_scale = 16384.0
address = 0x68  # This is the address value read via the i2cdetect command
bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards

def read_all():
    raw_gyro_data = bus.read_i2c_block_data(address, 0x43, 6)
    raw_accel_data = bus.read_i2c_block_data(address, 0x3b, 6)

    gyro_scaled_x = twos_compliment((raw_gyro_data[0] << 8) + raw_gyro_data[1]) / gyro_scale
    gyro_scaled_y = twos_compliment((raw_gyro_data[2] << 8) + raw_gyro_data[3]) / gyro_scale
    gyro_scaled_z = twos_compliment((raw_gyro_data[4] << 8) + raw_gyro_data[5]) / gyro_scale

    accel_scaled_x = twos_compliment((raw_accel_data[0] << 8) + raw_accel_data[1]) / accel_scale
    accel_scaled_y = twos_compliment((raw_accel_data[2] << 8) + raw_accel_data[3]) / accel_scale
    accel_scaled_z = twos_compliment((raw_accel_data[4] << 8) + raw_accel_data[5]) / accel_scale

    return (gyro_scaled_x, gyro_scaled_y, gyro_scaled_z, accel_scaled_x, accel_scaled_y, accel_scaled_z)
    
def twos_compliment(val):
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a, b):
    return math.sqrt((a * a) + (b * b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


def speak(msg):
	os.system('espeak " ' + msg +'" --stdout | aplay -D sysdefault:CARD=0');
	print(msg);
	time.sleep(2);



#Assign week days
week=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#Assign classes per day
MonProgram = ['Greek Language', 'Greek Language', 'Computer Science',      'Maths',                  'Physics',         'Gymnastics',              'English language'];
TueProgram = ['Greek Language', 'Greek Language', 'Maths',                 'History',                'Geography',        'English',                'Music'];
WenProgram = ['Greek Language', 'Greek Language', 'Maths',                 'Physics',                'Religion studies', 'French-German language', 'Civil Education'];
ThuProgram = ['Greek Language', 'Greek Language', 'Maths',                 'French-German language', 'English language', 'History',                'Gymnastics'];
FriProgram = ['Greek Language', 'Greek Language', 'French-German laguage', 'Geography',              'Relegion studies', 'English language',       'Arts'];

#Assign school break
school_brake=["08:21", "09:44", "10:11", "11:39", "11:56", "12:34", "12:46", "13:24", "13:31", "14:09"]

#Assign day and month
day = time.strftime("%A")
month = time.strftime("%B")
t = time.strftime("%H:%M")

print(str(day), str(month))
print(t)

hour, minute = t.split(":");
print(minute)

#Main

client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("00:22:43:CD:96:E6", 4))

speak("Hello!");
while (True):
	time.sleep(60);
	
	
	values = read_all()
	temp =  float(values[0])
	speak('Outside temprature is', temp);
	
	day = time.strftime("%A")
	month=time.strftime("%B")
	t = time.strftime("%H:%M")
	print(str(day), str(month))
	print(t)

	hour, minute = t.split(":");

	nowDay = str(day);
	nowHour = int(hour);
	nowMin = int(minute);
	if (nowDay == 'Monday'):
		todayProgram = MonProgram;
	if (nowDay == 'Tuesday'):
            todayProgram = TueProgram;
	if (nowDay == 'Wednesday'):
            todayProgram = WenProgram;
	if (nowDay == 'Thursday'):
            todayProgram = ThuProgram;
	if (nowDay == 'Friday'):
            todayProgram = FriProgram;
	
	if ((nowHour == 8) and (nowMin == 30)):
		speak("Good morning! I wish you all a nice week");
		speak("Let's remember our program for today");
		speak("Today is " + nowDay);

		if (nowDay == 'Monday'):
			todayProgram = MonProgram;
			for course in MonProgram:
				speak(course);
		if (nowDay == 'Tuesday'):
			todayProgram = TueProgram;
			for course in TueProgram:
				speak(course);
		if (nowDay == 'Wednesday'):
			todayProgram = WenProgram;
			for course in WenProgram:
				speak(course);
		if (nowDay == 'Thursday'):
			todayProgram = ThuProgram;
			for course in ThuProgram:
				speak(course);
		if (nowDay == 'Friday'):
			todayProgram = FriProgram;
			for course in FriProgram:
				speak(course);
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()
	#First break
	if ((nowHour == 9) and (nowMin == 43)):
		speak("Break in one minute");
		speak("Next hour, we will be studing " + todayProgram[2]);

	if ((nowHour == 9) and (nowMin == 45)):
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()

	#Second break
	if ((nowHour == 10) and (nowMin == 59)):
		speak("Break in one minute");
		speak("Next hour, we will be studing " + todayProgram[3]);

	if ((nowHour == 11) and (nowMin == 1)):
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()

	#Third break
	if ((nowHour == 11) and (nowMin == 38)):
		speak("Break in one minute");
		speak("Next hour, we will be studing " + todayProgram[4]);

	if ((nowHour == 11) and (nowMin == 40)):
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()


	#Forth break
	if ((nowHour == 12) and (nowMin == 33)):
		speak("Break in one minute");
		speak("Next hour, we will be studing " + todayProgram[5]);

	if ((nowHour == 12) and (nowMin == 35)):
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()


	#Sixth break
	if ((nowHour == 13) and (nowMin == 23)):
		speak("Break in one minute");
		speak("Next hour, we will be studing " + todayProgram[6]);

	if ((nowHour == 13) and (nowMin == 25)):
		mixer.init()
		mixer.music.load('/home/pi/Desktop/Sia_Flames.mp3')
		mixer.music.play()

	#Seventh break
	if ((nowHour == 14) and (nowMin == 9)):
		speak("That's all for today!");

