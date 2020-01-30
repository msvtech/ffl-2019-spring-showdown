
    front_motor.on(speed=SpeedPercent(40))
    time.sleep(0.5)
    front_motor.off()


    # Drive Forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), ratio_degrees_to_inches * 17.6, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(40), ratio_degrees_to_inches * 27, brake=True)

    # Drive Backwards
    tank_drive.on_for_degrees(SpeedPercent(-40), SpeedPercent(-40), ratio_degrees_to_inches * 18, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(100), SpeedPercent(100), ratio_degrees_to_inches * -10, brake=True)

    # Turn Right 45 degrees
    tank_drive.on_for_degrees(SpeedPercent(-50), SpeedPercent(50), rotate * 45, brake=True)
    tank_drive.on_for_degrees(SpeedPercent(40), SpeedPercent(-40), rotate * 48, brake=True)


