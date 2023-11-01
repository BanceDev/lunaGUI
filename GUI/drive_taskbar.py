import imgui
from array import array
import psutil

# create main information bar on the bottom of the driver station
def drive_taskbar():
    
    io = imgui.get_io()
    imgui.set_next_window_position(io.display_size.x * 0.5, io.display_size.y, 1, pivot_x = 0.5, pivot_y = 0.5)
    imgui.set_next_window_size(io.display_size.x, io.display_size.y * 0.5)
    imgui.begin(
        "Robot Drive Control",
        flags =  imgui.WINDOW_NO_COLLAPSE |
        imgui.WINDOW_NO_MOVE
    )

    imgui.set_window_font_scale(0.0015 * imgui.get_window_size().x)
    # button controls for selecting drive mode and enable/disable
    imgui.begin_group()
    imgui.button("TeleOperation", imgui.get_window_size().x * 0.2)
    imgui.button("Autonomous", imgui.get_window_size().x * 0.2)
    imgui.button("Enable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15)
    imgui.same_line(spacing=imgui.get_window_size().x * 0.02)
    imgui.button("Disable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15)
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
    
    imgui.end_group()

    imgui.same_line(spacing=imgui.get_window_width() * 0.04)

    # Display for robot battery history and current voltage
    imgui.begin_group()
    imgui.text("Robot Battery")
    battery_values = array('f', [1 for _ in range(20)])
    imgui.plot_histogram("", battery_values, graph_size=(imgui.get_window_size().x * 0.07, imgui.get_window_size().y * 0.08))
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    imgui.text("0.0V")
    imgui.end_group()

    imgui.same_line(spacing=imgui.get_window_width() * 0.04)

    imgui.begin_group()
    imgui.text("Change Network Values")
    ip_val = "0.0.0.0"
    changed_ip, ip_val = imgui.input_text("", ip_val)
    imgui.end_group()

    imgui.end()