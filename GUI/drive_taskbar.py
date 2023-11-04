import imgui
from array import array
import psutil

#
# Creates the UI for the bottom taskbar for the driver station
#
# :param joysticks: a list object of joysticks given from a pygame instance
# :param robot_battery: a string containing the voltage of the robot battery
# :param connected: a boolean to display the connection status of the server
#
def drive_taskbar(joysticks, robot_battery, connected):
    
    io = imgui.get_io()
    imgui.set_next_window_position(io.display_size.x * 0.5, io.display_size.y, 1, pivot_x = 0.5, pivot_y = 0.5)
    imgui.set_next_window_size(io.display_size.x, io.display_size.y * 0.5)
    imgui.begin(
        "Robot Drive Control",
        flags =  imgui.WINDOW_NO_COLLAPSE |
        imgui.WINDOW_NO_MOVE
    )
    # button controls for selecting drive mode and enable/disable
    imgui.begin_group()
    if imgui.button("TeleOperation", imgui.get_window_size().x * 0.2):
        print("teleop callback")
    if imgui.button("Autonomous", imgui.get_window_size().x * 0.2):
        print("auto callback")
    if imgui.button("Enable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15):
        print("enable callback")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.02)
    if imgui.button("Disable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15):
        print("disable callback")
    imgui.end_group()

    imgui.same_line(spacing=imgui.get_window_width() * 0.04)

    # Display for elapsed uptime and driver station battery
    imgui.begin_group()
    imgui.text("Elapsed Uptime: ")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.04)
    imgui.text("0:00.0")
    imgui.text("PC Battery")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    battery = psutil.sensors_battery()
    if battery != None:
        imgui.progress_bar(battery.percent/100, (imgui.get_window_size().x * 0.125, imgui.get_window_size().y * 0.05), "")
    else:
        imgui.progress_bar(100, (imgui.get_window_size().x * 0.125, imgui.get_window_size().y * 0.05), "")
    imgui.text("Comms     ")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    if connected:
        imgui.color_button("Comms Enabled", 0, 1, 0, 1, 0, imgui.get_window_size().x * 0.04, imgui.get_window_size().y * 0.05)
    else:
        imgui.color_button("Comms Disabled", 1, 0, 0, 1, 0, imgui.get_window_size().x * 0.04, imgui.get_window_size().y * 0.05)
    imgui.text("Controller")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.014)
    if len(joysticks) > 0:
        imgui.color_button("Joystick Enabled", 0, 1, 0, 1, 0, imgui.get_window_size().x * 0.04, imgui.get_window_size().y * 0.05)
    else:
        imgui.color_button("Joystick Disabled", 1, 0, 0, 1, 0, imgui.get_window_size().x * 0.04, imgui.get_window_size().y * 0.05)
    
    imgui.end_group()

    imgui.same_line(spacing=imgui.get_window_width() * 0.04)

    # Display for robot battery history and current voltage
    imgui.begin_group()
    imgui.text("Robot Battery")
    imgui.progress_bar(float(robot_battery)/12.0, (imgui.get_window_size().x * 0.05, imgui.get_window_size().y * 0.07), "")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    imgui.text(f"{robot_battery}V")
    imgui.end_group()

    imgui.same_line(spacing=imgui.get_window_width() * 0.04)


    imgui.end()