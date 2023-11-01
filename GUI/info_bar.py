import imgui

# create main information bar on the bottom of the driver station
def drive(cpu, battery):
    io = imgui.get_io()
    imgui.set_next_window_position(io.display_size.x * 0.5, io.display_size.y, 1, pivot_x = 0.5, pivot_y = 0.5)
    imgui.set_next_window_size(io.display_size.x, io.display_size.y * 0.5)
    imgui.begin(
        "Robot Drive Control",
        flags =  imgui.WINDOW_NO_COLLAPSE |
        imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_RESIZE
    )

    

    imgui.begin_group()
    imgui.button("Controler Operation", imgui.get_window_size().x * 0.2)
    imgui.button("Autonomous", imgui.get_window_size().x * 0.2)
    imgui.button("Enable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15)
    imgui.same_line(spacing=imgui.get_window_size().x * 0.02)
    imgui.button("Disable", imgui.get_window_size().x * 0.09, imgui.get_window_size().y * 0.15)
    imgui.end_group()

    imgui.same_line(spacing=50)

    imgui.begin_group()
    imgui.text("Elapsed Uptime: ")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.04)
    imgui.text("0:00.0")
    imgui.text("PC Battery")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    if battery != None:
        imgui.progress_bar(battery, (100, 20), "")
    else:
        imgui.progress_bar(100, (100, 20), "")
    imgui.text("PC CPU %  ")
    imgui.same_line(spacing=imgui.get_window_size().x * 0.01)
    imgui.set_next_item_width(100)
    imgui.progress_bar(cpu, (100, 20), "")
    imgui.end_group()

    imgui.same_line(spacing=50)

    imgui.begin_group()
    imgui.text("placeholder")
    imgui.end_group()

    imgui.end()