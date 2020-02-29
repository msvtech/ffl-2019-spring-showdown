#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B #, OUTPUT_C # , OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor #,  GyroSensor, ColorSensor
# from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
# front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
# leds = Leds()
ts = TouchSensor()

ratio_degrees_to_inches = 360 / 8.44
rotate = 140.0 / 90.0

def m07_cgi():
    # ####################################
    # Mission 7 - Convert to CGI
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 11.75, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * 92, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 44, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * -59, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 26., brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-100), SpeedPercent(100), rotate * -360, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 26., brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * -120, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 55, brake=True)

if __name__ == '__main__':
    m07_cgi()
