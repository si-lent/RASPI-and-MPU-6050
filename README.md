# RASPI-and-MPU-6050

Code for raspberry pi and MPU-6050 accelerometer sensor, from gathering of data to the sending of data to a database.

MPU 6050 library used:
https://makersportal.com/blog/2019/11/11/raspberry-pi-python-accelerometer-gyroscope-magnetometer

The Database I used for testing:
https://www.freemysqlhosting.net/

Installing Mysql connector for python:
sudo pip install pymysql

**Note:**

  1. The code and the library of MPU-6050 must be on the same directory
  2. The code is programmed to sent data if it reaches a certain threshold value
  3. The data is sent in batch of 100 data 
  4. If you are going to use the database hosting that I used in testing it is limited to a certain KB
 
