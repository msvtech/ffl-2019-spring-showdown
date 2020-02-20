#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, # OUTPUT_D # OUTPUT_C
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
rotate = 140.0 / 90.0 # 135.0

def m07_cgi():
    # ####################################
    # Mission 7 - Convert to CGI
    # ####################################

    # tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 1.0, brake=True)
    # tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 360, brake=True)
    # time.sleep(0.5)
    # tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * -360, brake=True)

    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 9.75, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 110, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 59.5, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * -90, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), ratio_degrees_to_inches * 15.5, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 280, brake=True)

    # top_motor.off()
    # top_motor.on(speed=SpeedPercent(50))
    # time.sleep(0.5)
    # top_motor.off()

if __name__ == '__main__':
    m07_cgi()
