#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C # , OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor #,  GyroSensor, ColorSensor
# from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
front_motor = MediumMotor(OUTPUT_C)
# top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
# leds = Leds()
ts = TouchSensor()

ratio_degrees_to_inches = 360 / 8.44
rotate = 135.0 / 90.0

def m02_microphone_boom():
    # ####################################
    # Mission 2 - Turn the Microphone Boom
    # ####################################
    front_motor.off()
    tank_drive.on_for_degrees(SpeedPercent(62), SpeedPercent(62), ratio_degrees_to_inches * 36, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(62), SpeedPercent(62), ratio_degrees_to_inches * -18, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate *  92, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(62), SpeedPercent(62), ratio_degrees_to_inches * -36, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate *  -62, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(62), SpeedPercent(62), ratio_degrees_to_inches * -36, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * , brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 2, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * -92, brake=True)
    #tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 21.0, brake=True)

if __name__ == '__main__':
    m02_microphone_boom()
