#!/usr/bin/python3

import os, random
import datetime
from datetime import timedelta


def wind_speed(date):
    f = open('Wind_Speed', 'w')
    d = datetime.datetime(1900, 1, 1, 0, 2, 57)
    delta = timedelta(0, 368)
    while(d.day == 1):
        f.write(date + ' ' + str(d.time()).replace('-', '_') + 
        ' ' + str(round(random.uniform(0.1, 1.5)*10, 1)) + '\r\n')
        d += delta
        
    f.close()


def barom_press(date):
    f = open('Barometric_Press', 'w')
    d = datetime.datetime(1900, 1, 1, 0, 2, 57)
    delta = timedelta(0, 368)
    while(d.day == 1):
        f.write(date + ' ' + str(d.time()).replace('-', '_') + 
        ' ' + str(round(random.uniform(20.0, 105.0), 1)) + '\r\n')
        d += delta
        
    f.close()


def air_temp(date):
    f = open('Air_Temp', 'w')
    d = datetime.datetime(1900, 1, 1, 0, 2, 57)
    delta = timedelta(0, 368)
    dt = int(date[5:7])

    while(d.day == 1):
        f.write(date + ' ' + str(d.time()).replace('-', '_') + ' ' + temp(dt) + '\r\n')
        d += delta
        
    f.close()

def temp(dt):
    if(dt == 1 or dt == 2 or dt == 12):
        t = str(round(random.uniform(-10.0, -2.0), 1))
    elif (dt in range(3, 6)):
        t = str(round(random.uniform(7.0, 15.0), 1))
    elif (dt in range(6, 9)):
        t = str(round(random.uniform(12.0, 25.0), 1))
    else:
        t = str(round(random.uniform(7.0, 12.0), 1)) 
    return t


d = datetime.date(2008, 1, 1)
while(d.year == 2008):
    data = str(d).replace('-', '_')
    os.makedirs(data)
    pth = data
    os.chdir(pth)
    wind_speed(data)
    air_temp(data)
    barom_press(data)
    os.chdir(os.pardir)
    d += timedelta(1)
