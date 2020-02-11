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

def m08_green_screen():
    # ####################################
    # Mission 8 - Act In Front of the Green Screen
    # ####################################



    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * 32.765, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 400, brake=True)
    front_motor.on(speed=SpeedPercent(-20))
    time.sleep(0.5)
    front_motor.off()

    front_motor.on(speed=SpeedPercent(20))
    time.sleep(0.5)
    front_motor.off()
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 560, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(60), SpeedPercent(60), ratio_degrees_to_inches * 16, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * -240, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(60), SpeedPercent(60), ratio_degrees_to_inches * 6, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), rotate * 70.75, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(60), SpeedPercent(60), ratio_degrees_to_inches * 10, brake=True)
    front_motor.on(speed=SpeedPercent(20))
    time.sleep(0.5)
    front_motor.off()

if __name__ == '__main__':
    m08_green_screen()
