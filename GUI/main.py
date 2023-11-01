#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from imgui.integrations.pygame import PygameRenderer
import OpenGL.GL as gl
import imgui
import pygame
import sys

# GUI components imports
import drive_taskbar as drive
import styles
import camera_stream as cam
import motor_info as motor
import test

# main window for imgui context
# using pygame due to out of box OpenGL and Controller support
def main():
    # Initialize pygame and imgui
    pygame.init()
    pygame.joystick.init()
    size = 1600, 900

    display = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)


    imgui.create_context()
    impl = PygameRenderer()

    io = imgui.get_io()
    io.display_size = size
   
    default_font = io.fonts.add_font_from_file_ttf(
    "GUI/Roboto-Regular.ttf", 24,
    )
    impl.refresh_font_texture()
    # configure UI style
    styles.set_style()

    
    ip_val = "0.0.0.0"
    port_val = "0"

    # pygame event handler
    while True:
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            impl.process_event(event)
        impl.process_inputs()

        imgui.new_frame()

        imgui.push_font(default_font)

        # menu bar for imgui window
        if imgui.begin_main_menu_bar():
            if imgui.begin_menu("File", True):

                clicked_quit, selected_quit = imgui.menu_item(
                    "Quit", "Cmd+Q", False, True
                )

                if clicked_quit:
                    sys.exit(0)

                imgui.end_menu()
            imgui.end_main_menu_bar()

        # display elements to the screen
        ip_val, port_val = drive.drive_taskbar(ip_val, port_val, joysticks)
        cam.camera_window()
        motor.motor_window()


        #make sure this is after all elements are displayed
        imgui.pop_font()

        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(1, 1, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        impl.render(imgui.get_draw_data())

        pygame.display.flip()


if __name__ == "__main__":
    main()