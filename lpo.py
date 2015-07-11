#!/usr/bin/python3
#

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

def populate(year):
    d = datetime.date(int(year), 1, 1)
    while(d.year == year):
        data = str(d).replace('-', '_')
        os.makedirs(data, exist_ok=True)
        pth = data
        os.chdir(pth)
        wind_speed(data)
        air_temp(data)
        barom_press(data)
        os.chdir(os.pardir)
        d += timedelta(1)

end_year = 2014
year = 2008

while(year <= end_year):
    os.makedirs(str(year), exist_ok=True)
    os.chdir(str(year))
    populate(int(year))
    year += 1
    os.chdir(os.pardir)
