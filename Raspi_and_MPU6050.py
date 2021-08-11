from mpu9250_i2c import *
from datetime import datetime
import pymysql.cursors
import time

def gathering_data():

    ax,ay,az,wx,wy,wz = mpu6050_conv()
    now = datetime.now()
    date_time = (now.strftime("%m/%d/%Y, %H:%M:%S"))

    return ax, ay, az, [ax, ay, az, date_time]


def data_gathered(array_ax, array_ay, array_az,ax,ay,az):

    array_ax.append (ax)
    array_ay.append (ay)
    array_az.append (az)

    length = len(array_ax)
    

    if (length == 100):
        max_x = max(array_ax)
        max_y = max(array_ay)
        max_z = max(array_ax)
        min_x = min(array_ax)
        min_y = min(array_ay)
        min_z = min(array_ax)
        array_ax.clear()
        array_ay.clear()
        array_az.clear()
        if (max_x >= 0.014 or max_y >= 0.014 or max_z >= 0.014 or min_x <= -0.014 or min_y <= -0.014 or min_z <= -0.014):
            return True
    

def sending_data(data_sent, connection, cursor):
    sql = "INSERT INTO BATSU_01 (X_axis,Y_axis,Z_axis,DATEandTIME) VALUES (%s,%s,%s,%s)"
    val = data_sent
    cursor.executemany(sql,val)
    connection.commit()
    print ("successfully inserted data")


def main():

    array_ax = []
    array_ay = []
    array_az = []
    connection = pymysql.connect (host='sql6.freemysqlhosting.net',user='sql6429124',password='6L7iZgEB2a',db ='sql6429124', cursorclass = pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    print ("successfully connected to database")
    major_array = []
    x = True
    
    while True:
        start_time = time.time()
        data = gathering_data()
        major_array.append(data[3])
        threshold = data_gathered (array_ax, array_ay, array_az, data[0], data[1], data[2])
        if (threshold == True):
            sending_data(major_array, connection, cursor)
            major_array.clear()
            print (time.time() - start_time)
            


if __name__ == "__main__":
    main()
    
