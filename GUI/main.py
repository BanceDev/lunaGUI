#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from imgui.integrations.pygame import PygameRenderer
import OpenGL.GL as gl
import imgui
import pygame
import sys
import psutil

# GUI components imports
import info_bar as info
import styles

# main window for imgui context
# using pygame due to out of box OpenGL and Controller support
def main():
    # Initialize pygame and imgui
    pygame.init()
    size = 800, 600

    display = pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)

    imgui.create_context()
    impl = PygameRenderer()

    io = imgui.get_io()
    io.display_size = size
    # configure UI style
    styles.set_style()

    # pygame event handler
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            impl.process_event(event)
        impl.process_inputs()

        imgui.new_frame()
        cpu = psutil.cpu_percent(interval=0.1)/100
        battery = psutil.sensors_battery()

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
        info.drive(cpu, battery)

        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(1, 1, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        impl.render(imgui.get_draw_data())

        pygame.display.flip()


if __name__ == "__main__":
    main()