import imgui

def camera_window():
    texture_id = imgui.get_io().fonts.texture_id

    imgui.begin("Robot Camera Feed")
    imgui.image(texture_id, imgui.get_window_width(), 132)
    imgui.end()