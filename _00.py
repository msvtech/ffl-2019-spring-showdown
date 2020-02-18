#!/usr/bin/env micropython
import time
from missions.utility import wait_for_button_with_message, reset_console, set_cursor, set_font, OFF

# from missions.m01_red_carpet            import m01_red_carpet
# from missions.m02_microphone_boom       import m02_microphone_boom
from missions.m03_costume               import m03_costume
# from missions.m04_move_the_set          import m04_move_the_set
# from missions.m05_rigging               import m05_rigging
from missions.m06_stunt_work            import m06_stunt_work
# from missions.m07_cgi                   import m07_cgi
# from missions.m08_green_screen          import m08_green_screen
# from missions.m09_camera                import m09_camera
# from missions.m10_dress_the_set         import m10_dress_the_set
# from missions.m11_deliver_the_movie     import m11_deliver_the_movie

def main(startAt):
    reset_console()
    set_cursor(OFF)
    set_font('Lat15-TerminusBold32x16')

    # if startAt <=  1 : wait_for_button_with_message('Carpet');          m01_red_carpet()
    # if startAt <=  2 : wait_for_button_with_message('Boom');            m02_microphone_boom()
    if startAt <=  3 : wait_for_button_with_message('Costume');         m03_costume()
    # if startAt <=  4 : wait_for_button_with_message('Move Set');        m04_move_the_set()
    # if startAt <=  5 : wait_for_button_with_message('Rigging');         m05_rigging()
    # if startAt <=  6 : wait_for_button_with_message('Stunt Work');      m06_stunt_work()
    # if startAt <=  7 : wait_for_button_with_message('CGI');               m07_cgi()
    # if startAt <=  8 : wait_for_button_with_message('Green Screen');    m08_green_screen()
    # if startAt <=  9 : wait_for_button_with_message('Camera');          m09_camera()
    # if startAt <= 10 : wait_for_button_with_message('Dress Set');       m10_dress_the_set()
    # if startAt <= 11 : wait_for_button_with_message('Deliver Movie');   m11_deliver_the_movie()

if __name__ == '__main__':
    main(0)
