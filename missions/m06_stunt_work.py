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
rotate = 135.0 / 90.0

def m06_stunt_work():
    # ####################################
    # Mission 6 - Stunt Work
    # ####################################

    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 11.75, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * 92, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 53.5, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * -45, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 13.25, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -14.25, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * 57, brake=True) # 105
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -70., brake=True)

if __name__ == '__main__':
    m06_stunt_work()
