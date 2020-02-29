#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, MoveTank, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import TouchSensor #,  GyroSensor, ColorSensor
# from ev3dev2.led import Leds
import time
# from math import cos, radians, degrees
# import os
# import sys

tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
front_motor = MediumMotor(OUTPUT_C)
top_motor = MediumMotor(OUTPUT_D)
# gs = GyroSensor()
# leds = Leds()
ts = TouchSensor()

ratio_degrees_to_inches = 360 / 8.44
rotate = 135.0 / 90.0

# On the spot mission start

tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 22, brake=True)
tank_drive.on_for_degrees(SpeedPercent(-15), SpeedPercent(15), rotate * 96, brake=True)
tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 30, brake=True)
front_motor.on(speed=SpeedPercent(-20))
time.sleep(0.5)
front_motor.off()
top_motor.on(speed=SpeedPercent(-20))
time.sleep(0.5)
top_motor.off()
